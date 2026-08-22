import feedparser
from trafilatura import fetch_url, extract
from ai import generate


d = feedparser.parse("http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml")


entries = d["entries"]
titles = []
summaries = []
links = []


for item in entries:
    titles.append(item["title"])
    summaries.append(item["summary"])
    links.append(item["link"])


html = fetch_url(links[2])
text = extract(html, target_language="en")
prompt = (
    "Summarize the following news article in 3-4 clear, objective sentences."
    "Focus strictly on key facts, primary figures, and main outcomes."
    "Avoid fluff, opinion, or conversational filler."
    "Article: " + text
)
# prompt = "Below are 15 news headlines from today. Pick the 3 most globally impactful stories, synthesize them into a concise 60-second news anchor script, and avoid fluff."


print("".join(generate(prompt, False)))


# Here's the structure for future debugging: the feedparser object is a dictionary with many top-level keys
# Amongst these keys is the "entries" key, which is itself a list of dictionaries.