import pyaudio #pip install pyaudio

p = pyaudio.PyAudio()
n = p.get_device_count() #to count devices
# print(n)

"""to get devices info"""
for i in range(n):
    data = f"{p.get_device_info_by_index(i)}"
    print(data)
p.terminate() #to terminate and free resources

print()
print(n)