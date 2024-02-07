import GPUtil as gp #pip install gputil

gpus = gp.getGPUs() #get the list of available GPUs

if not gpus:
    print(f"\t No GPU available!!!")
else:
    for i, gpu in enumerate(gpus):
        print(f"\t GPU {i + 1}:")
        print(f"\t Name: {gpu.name}")
        print(f"\t ID {gpu.id}")
        print(f"\t Driver: {gpu.driver}")
        print(f"\t GPU Memory Total: {gpu.memoryTotal} MB")
        print(f"\t GPU Memory Free: {gpu.memoryFree} MB")
        print(f"\t GPU Memory Used: {gpu.memoryUsed} MB")
        print(f"\t GPU Load: {gpu.load * 100} %")
        print(f"\t GPU Temperature: {gpu.temperature} deg C")