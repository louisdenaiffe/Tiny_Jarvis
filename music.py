import requests


MOPIDY_URL = "http://localhost:6680/mopidy/rpc"


def handle_music(prompt, d):
    query = prompt[4:].strip()
    if not query:
        return "What would you like me to play?"
    print(f"Searching for {query}")
    '''
    try:
        tracks = search_music
    '''


def search_music(query):
    results = mopidy_request(
        "core.library.search"
        {
            "query":{
                "any":[query]
            }
        }
    )
    tracks = []
    for result in results:
        for track in result.get("tracks", []):
            tracks.append(track)
    return tracks