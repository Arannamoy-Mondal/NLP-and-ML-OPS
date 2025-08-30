import whisper
import pandas as pd
import json

model=whisper.load_model("large-v2")

result=model.transcribe(audio="./audios/1_music.mp3",language="bn",task="Translate")

chunks=[]


for segment in result["segments"]:
    chunks.append({"start":segment["start"],"end":segment["end"],"text":segment["text"]})


print(result["text"])

with open("./10_RAG_Based_AI_Teaching_Assistant/Data/2_mp3_to_text.json","w") as fl:
     json.dump(chunks,fl)