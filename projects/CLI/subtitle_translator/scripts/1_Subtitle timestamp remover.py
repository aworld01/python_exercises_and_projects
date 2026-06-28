import re

input_file = "file.srt"
output_file = "cleaned.txt"

timestamp_pattern = re.compile(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}")

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned = []

for line in lines:
    if not timestamp_pattern.match(line.strip()):
        cleaned.append(line)

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(cleaned)

print("Done! Timestamps removed.")