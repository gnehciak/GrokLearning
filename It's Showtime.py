"""
Band: The One Word Wonders
Songs: Song Lyric Ballad
Please welcome to the stage, The One Word Wonders!
They will be playing...
🎵 Song
🎵 Lyric
🎵 Ballad
Give it up for The One Word Wonders!
"""
band, songs = input('Band: '), input('Songs: ')
print(f"Please welcome to the stage, {band}!\nThey will be playing...")
for i in songs.split():
    print(f"🎵 {i}")
print(f"Give it up for {band}!")