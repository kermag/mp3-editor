import eyed3
import os

input_folder = "input"

def load_mp3_information(input_folder): #불러오는 함수

    mp3_files = [f for f in os.listdir(input_folder) if f.endswith('.mp3')]

    for mp3_file in mp3_files:
        input_path = os.path.join(input_folder, mp3_file)

        #load
        audiofile = eyed3.load(input_path)

        #print
        print("Title :", audiofile.tag.title)
        print("Artist :", audiofile.tag.artist)
        print("Album :", audiofile.tag.album)
        print("Album Artist :", audiofile.tag.album_artist)
        print("\033[1;31;40m_____________________________________\033[0m")

load_mp3_information(input_folder)