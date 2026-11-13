"""Build index.html, a standalone page for static hosting, from sannishtha-elder-care.html.

The source file is written for claude.ai artifacts, which add the document
skeleton at publish time. Run `python3 build.py` after editing the source.
"""
src = open("sannishtha-elder-care.html", encoding="utf-8").read()
cut = src.index("</style>") + len("</style>")
head, body = src[:cut], src[cut:]
page = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="Sannishtha Elder Care, a not-for-profit programme of Sannishtha Foundation: '
    'long-term care planning for ageing parents in India.">\n'
    '<link rel="icon" href="assets/sannishtha-mark.png">\n'
    "<style>body{margin:0}img{max-width:100%}</style>\n"
    + head + "\n</head>\n<body>\n" + body.lstrip("\n") + "\n</body>\n</html>\n"
)
open("index.html", "w", encoding="utf-8").write(page)
print("wrote index.html")
