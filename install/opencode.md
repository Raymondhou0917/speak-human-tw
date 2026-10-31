# OpenCode 安裝指南

OpenCode 會自動掃 `~/.config/opencode/skills/*/SKILL.md`，把這個 repo 直接 clone 進去就能用，不用裝插件、不用改設定。

> 之前文件推薦的社群打包版 `@jimmyyen/opencode-speak-human-tw` 從 1.6.6 起少了插件檔，OpenCode 認不到，已停止推薦。舊裝法怎麼清掉，見下方[從舊插件換過來](#從舊插件換過來)。（感謝 [#8](https://github.com/Raymondhou0917/speak-human-tw/issues/8) 回報與整理替代做法）

## 安裝

macOS／Linux：

```bash
git clone --depth 1 https://github.com/Raymondhou0917/speak-human-tw.git ~/.config/opencode/skills/speak-human-tw
```

Windows（PowerShell）：

```powershell
git clone --depth 1 https://github.com/Raymondhou0917/speak-human-tw.git "$env:USERPROFILE\.config\opencode\skills\speak-human-tw"
```

資料夾名稱一定要是 `speak-human-tw`：OpenCode 要求資料夾名稱跟 `SKILL.md` 裡的 `name` 一致，改名就讀不到。

裝完重開 OpenCode。

> 已經幫 Claude Code 裝在 `~/.claude/skills/speak-human-tw` 的話，OpenCode 也會掃那裡，不用再裝一份。兩邊都放會變成同名 skill 重複。

## 加上 `/speak-human-tw` 指令（選用）

不加指令也能用，直接說「幫我說人話」就會命中。想要斜線指令的話，建一個指令檔：

macOS／Linux：

```bash
mkdir -p ~/.config/opencode/commands && cat > ~/.config/opencode/commands/speak-human-tw.md <<'EOF'
---
description: 說人話：繁體中文去 AI 味改寫
---
載入 speak-human-tw skill，照它的流程處理 $ARGUMENTS。沒給內容就先問我要改哪一段。
EOF
```

Windows（PowerShell 7）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.config\opencode\commands" | Out-Null
@'
---
description: 說人話：繁體中文去 AI 味改寫
---
載入 speak-human-tw skill，照它的流程處理 $ARGUMENTS。沒給內容就先問我要改哪一段。
'@ | Set-Content "$env:USERPROFILE\.config\opencode\commands\speak-human-tw.md" -Encoding utf8NoBOM
```

## 確認裝好了

終端機跑：

```bash
opencode debug skill
```

清單裡有 `speak-human-tw` 就是裝對了。也可以開新對話說「這段好 AI，幫我說人話」，看到它先列出建議清單等你點頭才改稿。

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
git -C ~/.config/opencode/skills/speak-human-tw pull
```

Windows 把路徑換成 `"$env:USERPROFILE\.config\opencode\skills\speak-human-tw"`。

## 從舊插件換過來

以前用 `opencode plugin @jimmyyen/opencode-speak-human-tw --global` 裝過的話：

1. 打開 `~/.config/opencode/opencode.jsonc`（或 `opencode.json`），把 `plugin` 陣列裡的 `"@jimmyyen/opencode-speak-human-tw"` 刪掉。
2. 照上面的[安裝](#安裝)步驟 clone 一份。
3. 重開 OpenCode。

## lite / full 兩種範圍

- **full（預設）**：clone 整包，OpenCode 會自己讀 `references/` 裡的完整規則（38 種痕跡、台灣用語表、誤殺防護）
- **lite**：只留 `SKILL.md` 也能跑，但沒有完整模式庫，誤殺率會高一點

## 常駐專案（選用）

在某個專案想每次都過這一關，在專案根目錄的 `AGENTS.md` 加這段：

```markdown
## 寫作風格
所有對外文字（貼文、電子報、文案、回信）輸出前，遵循 speak-human-tw skill 的規則做去 AI 味檢查。
程式碼、log、設定檔不套用。
```
