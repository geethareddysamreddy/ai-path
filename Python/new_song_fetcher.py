import requests
def get_new_relase_songs(genre="all",limit=10):
    url = f"https://itunes.apple.com/search?term=new&media=music&limit={limit}"
    try:
        response=requests.get(url,timeout=5)
        response.raise_for_status()
        data=response.json()
        print(f"\n🎵 New Music Releases\n{'-'*40}")
        for song in data["results"]:
            print(f"🎵 {song['trackName']} — {song['artistName']}")
    except requests.exceptions.ConnectionError:
            print("No Internet Connection")
get_new_relase_songs()