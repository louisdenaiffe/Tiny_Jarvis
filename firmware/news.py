import feedparser
from trafilatura import fetch_url, extract


d = feedparser.parse("http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml")


entries = d["entries"]
titles = []
summaries = []
links = []
for item in entries:
    titles.append(item["title"])
    summaries.append(item["summary"])
    links.append(item["link"])


html = fetch_url(links[1])
text = extract(html, target_language="en")


print(text)


# Here's the structure for future debugging: the feedparser object is a dictionary with many top-level keys
# Amongst these keys is the "entries" key, which is itself a list of dictionaries.