import pandas as pd

def analyze_artist(csv_file, artist_name):
    """
    Analyze an artist's music statistics from the dataset.

    Parameters:
        csv_file (str): Path to CSV dataset.
        artist_name (str): Artist name.

    Returns:
        dict: Artist statistics.
    """
    df = pd.read_csv(csv_file)

    artist_df = df[df["Artist"] == artist_name]

    summary = {
        "artist": artist_df["Artist"].iloc[0],
        "songs": len(artist_df),
        "first_year": int(artist_df["Release Year"].min()),
        "latest_year": int(artist_df["Release Year"].max()),
        "highest_views": int(artist_df["Youtube Views"].max()),
        "lowest_views": int(artist_df["Youtube Views"].min()),
        "average_views": int(artist_df["Youtube Views"].mean()),
        "career_span": int(
            artist_df["Release Year"].max() - artist_df["Release Year"].min()
        )
    }

    summary["chart_data"] = artist_df
    return summary