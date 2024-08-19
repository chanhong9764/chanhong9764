import feedparser, time

URL="https://pslog.co.kr/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=4

markdown_text = """
<div align="center">

![header](https://capsule-render.vercel.app/api?type=venom&color=auto&text=Welcome%20to%20Chanhong's%20GitHub%20&animation=twinkling&fontSize=35&height=250)

<h3>🌈 Follow Me </h3>

<a href="https://pslog.co.kr/">![Static Badge](https://img.shields.io/badge/BLOG-%23EA4335?style=flat&logo=tistory)</a>
<a href="mailto:chanhong9784@naver.com.com">![Static Badge](https://img.shields.io/badge/chanhong9784%40naver.com-%23EA4335?style=flat&logo=gmail&logoColor=white)</a>
<a href="https://www.instagram.com/cks._.hong/">![Static Badge](https://img.shields.io/badge/INSTAGRAM-%23E4405F?style=flat&logo=instagram&logoColor=white)</a>

<h3>🎤 Introduce </h3>

안녕하세요😄 정보보호학과를 졸업했지만 <strong>웹 개발자</strong>가 되기 위해 나아가고 있습니다!

새로운 것을 배우기 좋아하며 <strong>백엔드 개발자 포지션</strong>을 선호합니다.

<strong>꼼꼼함</strong>과 <strong>분석력</strong>이 저의 강점이며 폭넓은 기술 스펙트럼을 보유하여 팀 프로젝트에서 주로 <strong>중재자</strong> 역할을 맡고 있습니다.

<br />

|🎈 Favorite Languages|📰 Latest Blog Posts|
|---|---|
|[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=chanhong9764&langs_count=10&layout=compact&theme=dark)](https://github.com/chanhong9764/chanhong9764)
""" # list of blog posts will be appended here
markdown_text = markdown_text[:-1]
markdown_text += "|"
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>"
markdown_text += "|"
markdown_text += "</div>"
f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
