import eyed3
import os

input_folder = "input"

def modify_mp3(input_folder): #수정하는 함수
    mp3_files = [f for f in os.listdir(input_folder) if f.endswith('.mp3')]#로드
    for mp3_file in mp3_files:
        input_path = os.path.join(input_folder, mp3_file)

        # MP3 로드
        audiofile = eyed3.load(input_path)

        # 수정 작업 수행
        audiofile.tag.artist = u"Shania Yan"
        audiofile.tag.album = u"Shania Yan"
        audiofile.tag.album_artist = u"Shania Yan"

        # 수정된 MP3 파일 저장
        audiofile.tag.save()

modify_mp3(input_folder)