# SillyTavern Theme Assets

这个公开仓库存放 SillyTavern 酒馆美化的最终图片素材，以及经过许可证核对的公共字体库，用于生成稳定的 Raw/CDN 链接。

## 目录规则

- `assets/<固定主题名>/`：按主题隔离最终素材。
- `font-library/v1/`：30 个可复用开放字体家族、逐字体许可证、来源记录、字样预览、清单和 `@font-face` CSS。
- A/B/C 未选草案、过程图、私人聊天截图、密钥、Cookie 和含敏感信息的文件不得上传。
- 主题正式引用固定到提交哈希，不直接依赖会变化的分支链接。

## 新芽

最终批准素材位于 `assets/xinya/`。

## 公共字体库

字体清单、使用方式和许可说明见 [`font-library/v1/README.md`](font-library/v1/README.md)。主题正式使用时应引用固定提交哈希版本的 `library.css` 或单个 WOFF2 文件。
