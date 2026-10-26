import json
import pathlib

SITE = pathlib.Path(r"C:\Users\TUF\Documents\deepseek-harness\default-workspace\qqbot\github-site")
TMP = pathlib.Path(r"C:\Users\TUF\Documents\deepseek-harness\default-workspace\qqbot\tmp")

tpl = (SITE / "template.html").read_text(encoding="utf-8")
persona = (TMP / "persona_huli.txt").read_text(encoding="utf-8").strip()
stickers = json.loads((TMP / "stickers.json").read_text(encoding="utf-8"))

# 模板里 PERSONA 是反引号模板字符串：转义反斜杠、反引号、${}
safe = persona.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

arr = "[" + ",".join('"data:image/jpeg;base64,' + v + '"' for v in stickers.values()) + "]"

out = tpl.replace("__PERSONA__", safe).replace("__STICKERS__", arr)
(SITE / "index.html").write_text(out, encoding="utf-8")

print(f"index.html: {len(out)} 字节 = {len(out)/1024:.1f} KB")
print(f"  人格长度: {len(persona)}")
print(f"  表情张数: {len(stickers)}")
