# 狐娘 · 手机上跟完整人格卡的 DeepSeek 聊天

一个纯前端网页应用：不需要服务器、不需要安装，任何手机的浏览器打开就能用。

## 功能

- **完整人格卡**：3117 字的「赤狐狐娘」角色设定全部内置
- **流式输出**：字是一个一个蹦出来的
- **语音回复**：用系统 TTS 朗读（iOS / Android 都支持中文语音）
- **表情包**：9 张内置，随机穿插
- **主动消息**：你 5 分钟没说话，它可能主动来一句
- **聊天记录**：存在本机 localStorage，刷新不丢
- **双开关**：语音 / 表情 / 主动消息都能单独关

## 使用

1. 打开网址
2. 第一次会让你填 **DeepSeek API Key**（在 https://platform.deepseek.com 申请）
   - Key 只存在你自己的手机里（localStorage），不会上传
3. 开始聊

### 装到桌面

- **iPhone**：Safari 打开 → 分享按钮 → 「添加到主屏幕」
- **Android**：Chrome 打开 → 右上角 ⋮ → 「添加到主屏幕」

装完后是全屏的，跟原生 App 差不多。

## 技术说明

- 直接调用 `https://api.deepseek.com/chat/completions`（该 API 允许浏览器跨域访问）
- 流式解析 SSE，无后端依赖
- 语音用 `window.speechSynthesis`，不经过任何服务器
- 所有数据都在浏览器 localStorage，无账号、无云端存储

## 隐私

- 本仓库**不包含任何 API Key**
- Key 由使用者在自己的设备上输入并保存在本地
- 本仓库不上传、不记录任何聊天内容

## 开发

```bash
# 修改 template.html 里的界面/逻辑，然后重新生成
python build.py
```

`template.html` 里用 `__PERSONA__` 和 `__STICKERS__` 作为占位符，
`build.py` 会把人设文本和 base64 表情图填进去生成 `index.html`。
