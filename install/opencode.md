# OpenCode 安裝指南

> [Raymondhou0917/speak-human-tw](https://github.com/Raymondhou0917/speak-human-tw) 的 OpenCode 社群打包版。

```bash
opencode plugin @jimmyyen/opencode-speak-human-tw --global
```

裝完重開 OpenCode，`/speak-human-tw` 指令就會出現。

## 確認裝好了

開新對話，輸入 `/speak-human-tw`，或直接說「這段好 AI，幫我說人話」。看到它先列出建議清單等你點頭才改稿，就是裝對了。

## 怎麼用

**讓它自己命中**（不用打指令）：

- 「這段好 AI，幫我說人話」
- 「幫我校對這篇電子報，去掉 AI 味再發」
- 「這則貼文改自然一點」

**只想看問題，不要它動手**：

- 「先標問題不要改，這段哪裡像 AI？」

**改檔案**：

- 「幫我校對 newsletter-draft.md，走一遍去 AI 味流程」

## 更新

```bash
opencode plugin @jimmyyen/opencode-speak-human-tw --global --force
```

## lite / full 兩種範圍

- **full（預設）**：裝整包，OpenCode 會自己讀 `references/` 裡的完整規則（38 種痕跡、台灣用語表、誤殺防護）
- **lite**：只留 `SKILL.md` 也能跑，但沒有完整模式庫，誤殺率會高一點

## 常駐專案（選用）

在某個專案想每次都過這一關，在專案根目錄的 `AGENTS.md` 加這段：

```markdown
## 寫作風格
所有對外文字（貼文、電子報、文案、回信）輸出前，遵循 speak-human-tw skill 的規則做去 AI 味檢查。
程式碼、log、設定檔不套用。
```
