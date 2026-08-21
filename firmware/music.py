import requests


MOPIDY_URL = "http://localhost:6680/mopidy/rpc"


def handle_music(prompt, d):
    query = prompt[4:].strip()
    if not query:
        return "What would you like me to play?"
    print(f"Searching for {query}")
    try:
        tracks = search_music(query)
        if not tracks:
            print("No results found")
            return f"I couldn't find {query}"
        track = tracks[0]
        print(f"Playing : {track['name']}")
        play_track(track)
        d.show_metrics()
        return f"Playing {track['name']}"
    except requests.exceptions.ConnectionError:
        print("Could not connect to Mopidy")
        d.show_metrics()
        return "I can't access the music player right now. Are you connected to wifi?"
    except Exception as e:
        print(f"Music error: {e}")
        d.show_metrics()
        return "Something went wrong while trying to play the music."


def mopidy_request(method, params=None):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or {}
    }

    response = requests.post(
        MOPIDY_URL,
        json=payload,
        timeout=5
    )
    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise RuntimeError(data["error"])
    return data["result"]


def search_music(query):
    print("Calling Mopidy...")
    results = mopidy_request(
        "core.library.search",
        {
            "query": {
                "any": [query]
            }
        }
    )
    print("Mopidy responded, ", results)
    tracks = []
    for result in results:
        for track in result.get("tracks", []):
            tracks.append(track)
    return tracks


def play_track(track):
    mopidy_request(
        "core.tracklist.clear"
    )
    mopidy_request(
        "core.tracklist.add",
        {
            "uris": [track["uri"]]
        }
    )
    mopidy_request(
        "core.playback.play"
    )



# For testing purposes (python music,py)
handle_music(input("Search for something: "), d=None)