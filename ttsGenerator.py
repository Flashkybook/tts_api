import os
from pathlib import Path
from gtts import gTTS


def Generator(word: str):  
    print("create /tmp", os.path.exists("/tmp"))

    # Create path
    if not os.path.exists("/tmp"):
        os.mkdir("/tmp")
        # print("create /tmp", os.path.exists("/tmp"))
    
    print(os.path.exists("/tmp"))

    name = word
    language = "en"
    # local tmp root
    local = os.path.join(
        (Path(__file__).resolve().parent.parent.parent), f"tmp/")
    if os.path.exists(local):
        path = os.path.join(
            (Path(__file__).resolve(
            ).parent.parent.parent), f"tmp/{word}.ogg"
        )
    # dev tmp root
    else:
        path = os.path.join(f"/tmp/{word}.ogg")

    # check file exist or file size is 0KB for create new audio
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        audio = gTTS(text=name, lang=language)
        audio.save(path)

    # respose_audio = open(path, "rb")  # open

    return path 
     
