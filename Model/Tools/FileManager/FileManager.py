import os.path
import urllib
from PIL import Image
from pytube import YouTube
import pafy


def retrieve_audio(song_id: str, url, root_path: str) -> str:
    audio_path = os.path.join(root_path, song_id + ".mp3")
    if not os.path.exists(audio_path):
        __download_audio(song_id, url, root_path)
    return audio_path


def retrieve_image(song_id: str, url, root_path: str) -> Image:
    image_path = os.path.join(os.path.join(root_path, song_id), song_id + ".jpg")
    if not os.path.exists(image_path):
        __download_image(song_id, url, root_path)
    return Image.open(image_path)


def __download_audio(song_id: str, video_url, root_path: str):
    print("Not supported yet")

def __download_image(song_id: str, url, root_path: str):
    personal_path = os.path.join(root_path, song_id)

    if not os.path.exists(personal_path):
        os.mkdir(personal_path)

    youtube_stream = YouTube(str(url))
    image_file = youtube_stream.thumbnail_url
    image_path = os.path.join(personal_path, song_id + ".jpg")

    if not os.path.exists(image_path):
        urllib.request.urlretrieve(image_file, image_path)
        print(image_path.title())
