import datetime
import whisper

model = whisper.load_model("base.en") #to load the model (download if not exists)
# option = whisper.DecodingOptions(language="en", fp16=False)
result = model.transcribe("Dont_lift_a_finger.mp4")

print(result["text"])

# save_target = "helloworld.vtt"
    
# with open(save_target, "w") as file:
#         for index, segment in enumerate(result["segments"]):
#             file.write(str(index+1)+"\n")
#             file.write(str(datetime.timedelta(seconds=segment["start"]))+" => "+str(datetime.timedelta(seconds=segment["end"]))+"\n")
#             file.write(segment["text"].strip()+"\n")
#             file.write("\n")


save_target = "helloworld.txt"
result = result["text"]

with open(save_target, "w") as file:
      file.write(result)