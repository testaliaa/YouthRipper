import pylast

API_KEY = "a0472e3ba14a8c6b2d373f25f7214f47"
API_SECRET = "e3706cbf68860e14e3da9bf6968b66c4"

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)

album = pylast.Album("Tyler, the Creator", "Flower Boy", network)
tracks = album.get_tracks()

print(tracks)