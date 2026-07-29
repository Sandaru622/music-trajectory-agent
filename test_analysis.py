from utils.analysis import analyze_artist
import pprint

artists = [
    "Kasun Kalhara",
    "Bathiya & Santhush",
    "Centigradz"
]

for artist in artists:
    result = analyze_artist("data/songs.csv", artist)

    print("\n" + "=" * 40)
    print("Artist:", artist)
    print("=" * 40)

    pprint.pprint(result)