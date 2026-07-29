from agents.trajectory_agent import TrajectoryAgent
from agents.interpreter_agent import InterpreterAgent

trajectory = TrajectoryAgent()
interpreter = InterpreterAgent()

artists = [
    "Kasun Kalhara",
    "Bathiya & Santhush",
    "Centigradz"
]

for artist in artists:

    print("=" * 50)
    print("Artist:", artist)
    print("=" * 50)

    summary = trajectory.run(artist)

    result = interpreter.run(summary)

    print(result)
    print()