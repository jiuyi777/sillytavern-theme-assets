from __future__ import annotations

import json
import sys
from pathlib import Path

from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / "fonts-manifest.json").read_text(encoding="utf-8"))
families = manifest.get("families", [])
errors: list[str] = []

if manifest.get("version") != "v2":
    errors.append("Manifest version must be v2")
if len(families) != 3:
    errors.append(f"Expected 3 selected families, found {len(families)}")

seen: set[str] = set()
for item in families:
    slug = item["id"]
    if slug in seen:
        errors.append(f"Duplicate id: {slug}")
    seen.add(slug)
    font_path = ROOT / item["woff2_path"]
    family_dir = font_path.parent
    preview_path = ROOT / item["preview_path"]
    for required in (
        font_path,
        family_dir / "OFL.txt",
        family_dir / "METADATA.pb",
        family_dir / "source.json",
        preview_path,
    ):
        if not required.is_file():
            errors.append(f"Missing: {required.relative_to(ROOT)}")
    if font_path.is_file():
        if font_path.stat().st_size >= 100 * 1024 * 1024:
            errors.append(f"GitHub size limit risk: {font_path.name}")
        try:
            font = TTFont(font_path, lazy=True)
            font.close()
        except Exception as exc:
            errors.append(f"Invalid WOFF2 {slug}: {exc}")
        if item.get("woff2_bytes") != font_path.stat().st_size:
            errors.append(f"Size mismatch: {slug}")
    coverage = item.get("coverage", {})
    if not coverage.get("has_ascii") or coverage.get("cjk_unified_ideographs", 0) < 6000:
        errors.append(f"Insufficient Chinese/ASCII coverage: {slug}")

for text_file in ROOT.rglob("*"):
    if not text_file.is_file() or text_file.suffix.lower() not in {".json", ".md", ".css", ".pb", ".txt", ".py"}:
        continue
    if text_file.resolve() == Path(__file__).resolve():
        continue
    text = text_file.read_text(encoding="utf-8", errors="replace")
    local_path_marker = "C:" + "\\Users\\"
    if local_path_marker in text or "gho_" in text or "github_pat_" in text:
        errors.append(f"Sensitive/local path marker in {text_file.relative_to(ROOT)}")

if errors:
    print("FONT_LIBRARY_V2_VALIDATION_FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

total = sum((ROOT / item["woff2_path"]).stat().st_size for item in families)
print("FONT_LIBRARY_V2_VALIDATION_OK")
print(f"families={len(families)}")
print(f"woff2_total_mib={total / 1024 / 1024:.2f}")
print("licenses=3")
print("previews=3")
