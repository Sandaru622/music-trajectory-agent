import os
import librosa
import pandas as pd
import numpy as np

# Read CSV
df = pd.read_csv("data/songs.csv")

# Folder containing MP3 files
audio_folder = "data/audio"

print("Audio files found:")
print(os.listdir(audio_folder))

for index, row in df.iterrows():

    # Skip empty song names
    if pd.isna(row["Song Name"]):
        continue

    song_name = str(row["Song Name"]).strip()

    file_path = os.path.join(audio_folder, song_name + ".mp3")

    print("\n----------------------------------------")
    print("Artist :", row["Artist"])
    print("Song   :", song_name)

    if os.path.exists(file_path):

        y, sr = librosa.load(file_path, sr=None)

        print("Loaded :", song_name)

        # Duration
        duration = librosa.get_duration(y=y, sr=sr)

        # Tempo
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        tempo = float(np.squeeze(tempo))

        # Energy
        rms = librosa.feature.rms(y=y)
        energy = float(rms.mean())

        # Loudness
        loudness = float(librosa.amplitude_to_db(rms, ref=np.max).mean())

        print(f"Duration : {duration:.2f} sec")
        print(f"Tempo    : {tempo:.2f} BPM")
        print(f"Energy   : {energy:.4f}")
        print(f"Loudness : {loudness:.2f} dB")

        # Save values into dataframe
        df.at[index, "Song Duration"] = round(duration, 2)
        df.at[index, "Tempo"] = round(tempo, 2)
        df.at[index, "Energy"] = round(energy, 4)
        df.at[index, "Loudness"] = round(loudness, 2)

    else:

        print("❌ File not found:", file_path)

        df.at[index, "Song Duration"] = np.nan
        df.at[index, "Tempo"] = np.nan
        df.at[index, "Energy"] = np.nan
        df.at[index, "Loudness"] = np.nan

# Save updated CSV
df.to_csv("data/songs.csv", index=False)

print("\n✅ Features extracted successfully!")