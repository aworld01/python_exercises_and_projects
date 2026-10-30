from glob import glob
import datetime
import whisper

path = glob("*.mp4")[0] #to find "*.mp4" first file
name,_ = path.split(".mp4") #to remove extension
fileName1 = f"{name}.vtt" #to add *.txt extension
fileName2 = f"{name}.txt"

model = whisper.load_model("base.en") #to load the model (download if not exists)
option = whisper.DecodingOptions(language="en", fp16=False)
result = model.transcribe(path)

"""CREATE "*.vtt" FILE"""
with open(fileName1, "w") as file:
    for index, segment in enumerate(result["segments"]):
        file.write(str(index+1)+"\n")
        file.write(str(datetime.timedelta(seconds=segment["start"]))+" => "+str(datetime.timedelta(seconds=segment["end"]))+"\n")
        file.write(segment["text"].strip()+"\n")
        file.write("\n")

"""CREATE "*.txt" FILE"""
with open(fileName2,"w") as wf:
    wf.write(result["text"])


import count