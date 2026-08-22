import feedparser
from trafilatura import fetch_url, extract
from ai import generate
import time
import threading
import re


def parse_top_titles(model_output: str) -> list[str]:
    pattern = r"^\s*[\-*•]\s*(?:[\"\']?)([^:\n\r\"]+)"
    matches = re.finditer(pattern, model_output, re.MULTILINE)
    titles = []
    for match in matches:
        clean_title = match.group(1).strip()
        titles.append(clean_title)
    return titles[:3]


def parse_rss():
    d = feedparser.parse("http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml")
    entries = d["entries"]
    titles = []
    links = []
    summaries = []
    for item in entries:
        titles.append(item["title"])
        links.append(item["link"])
    headlines = parse_top_titles(select_headlines(titles))
    for headline in headlines:
        try:
            index = titles.index(headline)
            content = extract_rss(links[index])
        except ValueError:
            continue
        prompt = (
            "Summarize the following news article in 3-4 clear, objective sentences."
            "Focus strictly on key facts, primary figures, and main outcomes."
            "Avoid fluff, opinion, or conversational filler."
            "Article: " + content
        )
        summaries.append("".join(generate(prompt, False)))
    return summaries


def extract_rss(link):
    html = fetch_url(link)
    return extract(html, target_language="en")


def select_headlines(titles):
    prompt = f"""Below are 13 news headlines.
    Pick the 3 most globally impactful stories.

    Headlines:
    {chr(10).join(f"- {t}" for t in titles)}

    Return ONLY a bulleted list of the 3 selected titles verbatim, followed by a one-sentence explanation for each.
    """
    return "".join(generate(prompt, False))


def save_to_file():
    summaries = parse_rss()
    with open("news.txt", "w") as file:
        for summary in summaries:
            file.write(summary + "\n")


def read_file():
    try:
        with open("news.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def start_news_scheduler(interval_seconds=3600):
    def worker():
        while True:
            try:
                save_to_file()
            except Exception as e:
                print(f"News scheduler error: {e}")
            time.sleep(interval_seconds)
    thread = threading.Thread(target=worker, daemon=True)
    thread.start()


# Here's the structure for future debugging: the feedparser object is a dictionary with many top-level keys
# Amongst these keys is the "entries" key, which is itself a list of dictionaries.