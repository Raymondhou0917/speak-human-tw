<div align="center">

# 說人話 speak-human-tw

### *字都對，卻不像人講的話？那就是 AI 味。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.4.0-brightgreen.svg)](CHANGELOG.md)
[![Benchmark](https://img.shields.io/badge/benchmark-42_cases-blue.svg)](evals/benchmark.md)
[![zh-TW](https://img.shields.io/badge/zh--TW-Taiwan-e4002b.svg)](references/taiwan-localization.md)
[![GitHub stars](https://img.shields.io/github/stars/Raymondhou0917/speak-human-tw?style=social)](https://github.com/Raymondhou0917/speak-human-tw/stargazers)

<br>

<img src="assets/readme/speak-human-tw-light-visuals-banner-v1.png" alt="說人話 speak-human-tw：繁體中文的去 AI 味改寫 skill" width="820">

<br>

<table>
<tr><td align="left">

🤖 &nbsp;AI 幫你把稿子寫好了，你自己讀一遍卻覺得哪裡怪，但又說不出來哪裡怪？<br>
📮 &nbsp;電子報資訊全對，讀起來卻像新聞稿，不像你在跟讀者講話？<br>
😮‍💨 &nbsp;每次都要一句一句抓「這句好 AI 味」，叫它重寫，改到最後比自己從頭寫還累？

</td></tr>
</table>

### ✨ 這些，`說人話.skill` 都能解決。

<br>

一個專門校對繁體中文的 skill：抓出 35+ 種 AI 中文寫作痕跡，順手把中國用語和半形標點改成台灣的寫法，改寫成讀起來像人寫的版本，還附一份交稿前能自己打分數的檢核表。

給 Claude Code、Codex、Cursor 和任何能讀 Markdown 的 AI agent 用。

**內容創作 · 行銷文案 · 日常辦公** —— 電子報 · 社群貼文 · 銷售頁 · 客服回信 · 簡報 · 公告 · Email

<br>

**先保住事實 → 再清掉 AI 味 → 最後才加人味**

不是把你的稿子洗成機器人，是把 AI 味洗掉、把你洗回來。

</div>

<div align="center">

---

### 應用說明：真人手寫 vs. AI 代寫辨識

<table width="100%">
<tr>
<td width="50%" valign="top" align="center">

**案例一：2024 年手寫電子報 → 那年根本沒有 AI 幫忙。丟進去使用 /speak-human-tw，它說沒有 AI 痕跡，感動。**

<img src="assets/readme/speak-human-tw-case-real-newsletter-2024.jpg" alt="說人話 skill 檢查 2024 年真人手寫的雷蒙週報，判定不用改" width="100%">

</td>
<td width="50%" valign="top" align="center">

**案例二：AI 代寫的回覆 → 抓到 6 處 AI 味＆提供建議修改方向**

<img src="assets/readme/speak-human-tw-case-ai-comment-reply.jpg" alt="說人話 skill 檢查 AI 代寫的 YouTube 留言回覆，逐條列出 6 處 AI 味" width="100%">

</td>
</tr>
</table>

</div>

**這個對比只能證明一件事：同一份 skill，能助你分得出 AI 味，它不代表你可以拿來當「萬用內容寫作」skill 用。**

它做的是校對，不是創作：拿一篇你已經寫好的稿子，抓出裡面的 AI 常見寫作模式，列出「哪裡可以怎麼改」的建議，要不要採用、怎麼改，還是你自己拍板。

**正確應用是先用你自己的風格寫初稿 → 用說人話抓 AI 味、拿改寫建議 → 自己判斷取捨、補回你的經驗和語氣，這樣才算定稿。** 
📌 完整說明見下方[〈在你的寫作流程中，適合在哪個位置？〉](#-在你的寫作流程中適合在哪個位置)。

---

## 說人話，能把你的 AI 味，改成什麼樣？

### 社群貼文：emoji 轟炸＋勸誡收尾

**改寫前**

> 🚀 重磅消息！AI 寫作工作坊正式上線啦！💡 這不僅僅是一堂課，更是一場思維的革命。與其在原地焦慮，不如現在就出發。畢竟，機會永遠留給準備好的人，不是嗎？🔥

**改寫後**

> AI 寫作工作坊開放報名了。三個小時，教你三件事：怎麼讓 AI 抓到你的語氣、怎麼建自己的改稿流程、怎麼把重複的產文工作自動化。上一梯 40 個名額，三天就額滿，這梯加開到 60 個，別錯過了。

### 電子報：價值上升詞＋解說導引句

**改寫前**

> 值得注意的是，上個月我們進行了一次意義深遠的實驗——把電子報的發送時間從週五早上改到週日晚上——這個決定標誌著我們對讀者行為的重新思考。
>
> 結果，開信率從 31% 掉到 14%。這個數據深刻地印證了內容產業瞬息萬變的本質，也提醒我們：真正的成長不是盲目嘗試，而是持續學習。
>
> 把這些數字擺在一起，你會讀到一件很重要的事：讀者的習慣比我們想像的更頑固。

**改寫後**

> 上個月我們做了一個實驗：電子報從週五早上改到週日晚上發。
>
> 結果開信率從 31% 掉到 14%。
>
> 讀者的習慣比我想像的頑固。你們就是習慣週五早上配咖啡看信是吧。好，那我下一期改回週五發，然後把「發送時間」正式排進 A/B 測試清單，用數據說話，不能在自以為我喜歡週日看就改到週日。

### 台灣在地化：中國用語校正改寫

**改寫前**

> 這個視頻的質量真的很高，信息量很大，博主講得特別接地氣。

**改寫後**

> 這支影片品質很高，資訊量很大，創作者把抽象概念講得很生活化。

更多場景（銷售頁、客服回信、公告）的完整 before/after 見 [references/examples.md](references/examples.md)。

<p align="center">
  <img src="assets/readme/speak-human-tw-bento-demo-final.jpg" alt="說人話在社群貼文、文章撰寫、Email 與行銷文案中偵測 AI 味並提出改寫建議" width="100%">
</p>
<p align="center">
  <a href="https://github.com/Raymondhou0917/speak-human-tw/stargazers">
    <img src="assets/readme/speak-human-tw-ui-buttons-star-fork.webp" alt="覺得說人話有用，幫我點一顆星" width="100%">
  </a>
</p>

---
## 30 秒上手

**Claude Code**：

```bash
git clone https://github.com/Raymondhou0917/speak-human-tw.git ~/.claude/skills/speak-human-tw
```

裝好後在對話裡說「幫這段去 AI 味」「這段好 AI，說人話」就會自動觸發。

**Codex（單次使用）**：

```bash
git clone https://github.com/Raymondhou0917/speak-human-tw.git && cd speak-human-tw
codex exec -C . "讀取 ./SKILL.md，按規則改寫以下文字，這次直接套用不用先問我：（貼上你的文字）"
```

**只想先看問題、不要改稿**：指令加一句「先標問題不要改」，會切到 annotation mode，只列出 1 到 5 個問題點。

各平台完整安裝方式（含 Cursor、symlink 跟隨更新）見下方[安裝](#安裝)。

### 第一次用會遇到的事：它不會直接改你的稿

預設行為是**兩輪**，不是一輪：

1. **第一輪**它只給你一張編號清單，每一條寫明：在哪一行、原句是什麼、為什麼要改（對應哪一種 AI 痕跡）、建議改成什麼。列完問你一句「以上 12 處有什麼地方是你覺得需要修改的嗎？」然後停下來。
2. **第二輪**你回「都改」「4 跟 8 不用，其他都改」「只改第 3 條」，它才動筆，也才會寫進你的檔案。

這是刻意的。改稿工具最危險的不是漏改，**關鍵在於你還沒看清楚它想幹嘛之前就把你的原稿蓋掉了**。你沒勾的它不會「順便」一起改。

不想要這關的話，在指令裡明講「不用列清單，直接幫我改」就會跳過。**非互動情境**（`codex exec`、CI、排程）它會自動偵測沒有人能回答問句，直接套用並在跑完後給你一份「原句／為什麼要改／改成了什麼」的事後摘要，方便你用 `git diff` 回溯。

## 它怎麼改

一句話原則：**先保事實，再去 AI 味，最後才加人味。**

固定六步：

1. **判情境**：社群貼文／電子報／銷售頁／客服回信／辦公文書，五種情境力度不同。社群改輕保留口語感，銷售頁改重但 CTA 力道不能弱
2. **鎖保護清單**：價格、優惠碼、專有名詞、連結、真名與引號原話、退費承諾先圈起來，改寫全程不動
3. **判範圍**：長文（約 1000 字以上）不擅自縮水，建議盡量逐句對應；整句空話也是清單裡的一條，說明「為什麼刪了不丟資訊」，由你拍板
4. **逐類改寫**：35+ 種痕跡逐類處理，模式優先、詞表兜底；台灣用語檢查同步跑
5. **保真回讀**：保護清單逐項核對，每個資訊點可追溯，不新增原文沒有的事實
6. **交稿前自評**：長文用 5 維 50 分制打分，低於 35 分不交稿

### 檢測的 35+ 種 AI 痕跡

| 分類    | 數量  | 例子                                                                                                                 |
| :---- | :-- | :----------------------------------------------------------------------------------------------------------------- |
| 內容類   | 9   | 誇大意義（標誌著、奠定基礎）、模糊歸屬（業界專家認為）、幻覺引用、公式化前景段、立場真空（各有優缺點、因人而異）                                                           |
| 語言句式類 | 12  | 「不是 A 而是 B」堆疊、排比三段式、解說導引句、假推論（這意味著）、勸誡反問收尾、說教深度腔（說到底、本質上）、金句公式（X 是 Y 的 Z）、假坦白鉤子（說真的、老實說）、戲劇性短句轟炸、公式化開場（在當今瞬息萬變的時代） |
| 風格版面類 | 8   | 破折號過密、粗體轟炸、emoji 堆疊、編號切碎段落（首先／其次／最後）、表格誤用                                                                          |
| 溝通殘留類 | 7   | 「希望這對你有幫助」、諂媚開場、罐頭結尾（總的來說、綜上所述）、知識截止免責、模板佔位文字、預告式導言                                                                |
| 工具痕跡類 | 2   | `utm_source=chatgpt.com`、`turn0search` 佔位碼、Markdown 標記錯置                                                           |

完整清單與範例句見 [references/patterns.md](references/patterns.md)。台灣在地化層（60+ 組中國用語對照、全形標點、引號規則）見 [references/taiwan-localization.md](references/taiwan-localization.md)。

---

## 📌 在你的寫作流程中，適合在哪個位置？

用 AI 寫作可以拆成兩件事：

| 讓 AI 做的             | 不該讓 AI 做的           |
| :------------------ | :------------------ |
| 架構設計、初稿撰寫、資料整理、大綱生成 | 決定立場、選擇語氣、產生比喻、寫出金句 |

問題出在中間那道縫：AI 起草的時候，會順手把兩欄一起交給你。

要完成一整篇文章、電子報、貼文，得靠你自己的 `Content Writing Skill` —— 每個人說話的偏好不一樣，這件事沒辦法通用，只能自己訓練：你的經驗、觀點、故事、平常講話的用詞和口吻，你不教它，它永遠不會知道。

不先講清楚這件事，很容易被誤用成「萬能寫作 skill」：改出來的東西表面上乾淨，實際上還是八股文、還是滿滿的違和感，因為裡面沒有你的觀點跟故事，只是把明顯的套路刮掉而已。

**這個 skill 做的就是把右欄從稿子裡刮掉，讓左欄留下來。**

但刮乾淨只是及格線。無菌、沒有觀點、每句都正確的文字，跟 AI 生成的一樣容易被認出來。所以 [references/humanize.md](references/humanize.md) 定義了改完之後往哪裡拉：允許不收尾、允許立場隨時間改變、允許岔題。這些是 AI 寫不出來的東西，因為它沒有過去，也不敢承認自己不確定。

硬界線只有一條：**人味是作者的，不是工具的。** 作者沒說過的故事、立場、轉折，它不准替你發明，只能留下「（需作者補充）」的標註。編出來的「我以前錯了」比原本那句空話糟糕得多：空話只是無聊，假故事是說謊。

至於為什麼要在乎：Google 看的從來就是讀者行為，有沒有讀完、有沒有立刻關掉。讀者關掉一篇文章，通常跟資訊對不對無關，是讀了三行覺得「這人好像不在」。

### 技能來源＆使用場景建議

中文圈已經有做得很好的方案，我們補的是不同的一塊：

- **知識源**：主要整理自[中文維基百科「AI生成文的特徵」](https://zh.wikipedia.org/zh-tw/Wikipedia:AI生成文的特徵)（WikiProject AI Cleanup 社群為了清理 AI 條目持續更新的第一手觀察）與[朱宥勳的「AI腔」句型分析](https://www.youtube.com/watch?v=9uuX6cb81C8)
- **場景**：專注在電子報、社群貼文、銷售頁、客服回信、辦公文書。
- **語言**：從頭以繁體中文與台灣用語校準，內建中國用語檢查。不是單純簡轉繁
- **實戰驗證**：核心規則來自 3 年多的真實改稿紀錄：哪些 AI 習慣被人類編輯反覆抓出來，全部進了規則和評測集

## 評測

[evals/benchmark.md](evals/benchmark.md) 目前 42 條用例：27 條 SF（該改必中）＋ 15 條 SNF（不可誤殺）。SNF 專門保護容易被誤殺的情況：有事實撐著的排比、有來源的數據、金流制式條款、長文節奏句、被討論的 AI 味詞、有選擇條件的「用 A 或用 B」。

判分含「不換湯」規則：刪掉「標誌著」卻補上「象徵著」，記失敗。跑法見 [evals/run-eval.md](evals/run-eval.md)。

**評測保證什麼、不保證什麼**：這 42 條驗的是「該改的有改到、不該動的沒被動、沒有換湯不換藥、事實一字沒漂」。**沒有任何一條在測「改完更有人味」**——人味沒辦法自動判分，硬要打分數就會變成另一種公式。那部分靠 [humanize.md](references/humanize.md) 的正向目標和你自己的判斷，這個專案不宣稱它可量化。

## 安裝

| 平台 | 文件 |
| :-- | :-- |
| Claude Code | [install/claude-code.md](install/claude-code.md) |
| Codex | [install/codex.md](install/codex.md) |
| Cursor | [install/cursor.md](install/cursor.md) |
| OpenCode | [install/opencode.md](install/opencode.md) |

核心只需要 `SKILL.md` 一個檔案（lite）；要完整的 35+ 種痕跡、台灣用語表和誤殺防護，帶上 `references/` 完整包（full）。

## 常見問題

### 為什麼它不直接改，要先問我？

這是刻意的，因為你的原稿比它的建議值錢。完整流程見上面的[〈它不會直接改你的稿〉](#第一次用會遇到的事它不會直接改你的稿)。不想要這關就說「不用列清單，直接幫我改」；非互動情境（`codex exec`、CI、排程）它會自動跳過確認、改完給事後摘要。

### 這是拿來騙 AI 偵測器的嗎？

不是。目標是讓文字真正讀起來更好：更具體、更誠實、更像一個具體的人在說話。最好的「去 AI 味」是文字裡有真實的思考。

### 改完會變成某個人的風格嗎？

不會。這個 skill 把稿子洗乾淨，不會替你注入人設。「去 AI 味」和「有個人風格」是兩件事：前者是及格線，後者要你自己（或你專屬的風格 skill）來加。

### 簡體中文能用嗎？

規則大多通用，但台灣在地化層（用語對照、全形標點慣例）是為繁體中文台灣讀者設計的。簡中場景建議用 [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua)。

### 會不會把我的銷售頁改到沒有轉換力？

不會。銷售頁情境明文規定：CTA 力道與急迫感是功能不是 AI 味，價格、優惠碼、期限、退費條款在保護清單裡一字不動。評測集有專門的誤殺防護用例（SNF-01 到 03）盯著這件事。

### 為什麼改完有時還是有點 AI 味？

「清掉明顯套路」不等於「擁有你的個人聲音」。遇到改完仍不自然的案例，用 [bad case 模板](.github/ISSUE_TEMPLATE/bad-case.md)回報，這比 star 更有用。


---

## 貢獻

歡迎提 Issue 和 PR：新的 AI 味模式、更貼切的範例句、中國用語對照的補充、評測用例。提交前請先讀 [CONTRIBUTING.md](CONTRIBUTING.md)，核心判斷只有一個：

> 這是一個「新模式」，還是「現有模式的變體」？

## 參考資源

- [中文維基百科：AI生成文的特徵](https://zh.wikipedia.org/zh-tw/Wikipedia:AI生成文的特徵)：主要知識來源，收錄真實的繁中案例
- [朱宥勳〈對「AI腔」厭煩了嗎？分析AI生成文字的經典句型〉](https://www.youtube.com/watch?v=9uuX6cb81C8)：否定平行結構一節的靈感來源。他的論點比「別用這個句型」更深一層——句型本身是正規的寫作動作（定義＋區分），問題出在濫用造成的審美疲勞，以及讀者容易把「形式正確」誤判成「內容正確」
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)：英文版原始指南
- [SEO研究院〈什麼是 AI 味？〉](https://blog.dns.com.tw/2026/05/ai-writing.html)：「AI 起草、人工注魂」的分工框架，以及「公式化開場」這個痕跡的來源
- [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua)：簡體中文去 AI 味的先行者，鎖定工程師與技術文件場景。保護片段、情境分級、SF/SNF 評測的方法論給了很好的參考，本專案把這套方法論帶到繁體中文與內容行銷場景重新設計
- [blader/humanizer](https://github.com/blader/humanizer)、[hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)：英文先行專案

所有範例句、詞表、保護清單、情境策略皆針對繁體中文場景原創撰寫，不翻譯、不移植上述任何專案的內容。

## 關於作者

這個 skill 來自[雷蒙（侯智薰）](https://github.com/Raymondhou0917) 這 3 年多的真實 AI 協作紀錄、寫作模式萃取。我經營「雷蒙三十」，寫數位工作術、AI 應用、一人公司和超級個體的經營模式，這個 skill 本來只是自己用，後來想公開給其他人，花了我好幾個晚上去重新打磨、潤飾和呈現，希望對需要的人有幫助。

► 想認識更多關於我？

- **[生活黑客研究院](https://academy.lifehacker.tw/)**：雷蒙三十的課程站，AI 與數位工作術
- **[AI Agent 學習資源](https://cc.lifehacker.tw/)**：Claude Code、Codex 的教學與設定包，非工程師也能上手
- **[免費訂閱雷蒙週報](https://lifehacker.kit.com/ai-agent)**：每週一封，寫 AI Agent 怎麼真的用在工作裡
- **[雷蒙的個人使用說明書](https://raymondhouch.com/lifehacker/raymond-manual/)**：我做了什麼，快速一頁式認識我

也可以在 [Facebook](https://www.facebook.com/raymondhou0917/)、[Instagram](https://www.instagram.com/yuiraymond/)、[Threads](https://www.threads.com/@raymond0917) 上找到我，但最近備課、寫書比較忙，比較少回訊息。

這個 skill 永遠免費。如果它幫你省下改稿的時間，**點顆星**我會很開心；但真正讓它變好的是[回報一個 bad case](.github/ISSUE_TEMPLATE/bad-case.md)，告訴我哪一段改完還是像 AI。

## 授權

[MIT License](LICENSE)。歡迎 fork、修改、提 PR。
