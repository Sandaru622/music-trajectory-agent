from utils.analysis import analyze_artist


class TrajectoryAgent:

    def run(self, artist):

        summary = analyze_artist("data/songs.csv", artist)

        summary["trend"] = "Increasing"

        return summary