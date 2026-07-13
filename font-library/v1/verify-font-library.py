from __future__ import annotations

import json
import sys
from pathlib import Path

from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parent
manifest_path = ROOT / "fonts-manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
families = manifest.get("families", [])
errors: list[str] = []

if len(families) != 30:
    errors.append(f"Expected 30 families, found {len(families)}")

seen: set[str] = set()
for item in families:
    slug = item["id"]
    if slug in seen:
        errors.append(f"Duplicate id: {slug}")
    seen.add(slug)
    font_path = ROOT / item["woff2_path"]
    license_path = font_path.parent / "OFL.txt"
    metadata_path = font_path.parent / "METADATA.pb"
    preview_path = ROOT / item["preview_path"]
    for required in (font_path, license_path, metadata_path, preview_path):
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

for text_file in ROOT.rglob("*.json"):
    text = text_file.read_text(encoding="utf-8", errors="replace")
    if "C:\\Users\\" in text or "gho_" in text or "github_pat_" in text:
        errors.append(f"Sensitive/local path marker in {text_file.relative_to(ROOT)}")

if errors:
    print("FONT_LIBRARY_VALIDATION_FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

total = sum((ROOT / item["woff2_path"]).stat().st_size for item in families)
print("FONT_LIBRARY_VALIDATION_OK")
print(f"families={len(families)}")
print(f"woff2_total_mib={total / 1024 / 1024:.2f}")
print("licenses=30")
print("previews=30")
