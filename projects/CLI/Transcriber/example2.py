from glob import glob
import whisper #pip install openai-whisper

path = glob("*.mp4")[0] #to find *.mp4 file
name,_ = path.split(".mp4") #to remove extension
fileName = f"{name}.txt" #to add *.txt extension
# print(name)

model = whisper.load_model("base.en") #to load the model (download if not exists)
result = model.transcribe(path)

print(result["text"])

result = result["text"]

with open(fileName, "w") as file:
      file.write(result)