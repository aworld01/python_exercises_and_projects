"""Software Info"""
import platform as p

# print(f"Computer network name: {p.node()}") //Computer network name
# print(f"Machine type: {p.machine()}") //Machine type
# print(f"Processor type: {p.processor()}") //Processor type
# print(f"Platform type: {p.platform()}") //Platform type
# print(f"Operating System: {p.system()}") //Operating System
# print(f"Operating System release: {p.release()}") //Operating System release
# print(f"Operating System version: {p.version()}") //Operating System version



"""Hardware Info"""
import psutil as s


"""RAM"""
print(f"Total RAM installed: {s.virtual_memory().total/1000000000}")
print(f"Available RAM: {s.virtual_memory().available/1000000000}")
print(f"Used RAM: {s.virtual_memory().used/1000000000}")
print(f"Usage RAM: {s.virtual_memory().percent}%")

print(f"Number of physical cores: {s.cpu_count(logical=False)}")
print(f"Number of logical cores: {s.cpu_count(logical=True)}")
print(f"Current CPU frequency: {s.cpu_freq().current}")
print(f"Min CPU frequency: {s.cpu_freq().min}")
print(f"Max CPU frequency: {s.cpu_freq().max}")
print(f"Current CPU utilization: {s.cpu_percent(interval=1)}")
print(f"Current per-CPU utilization: {s.cpu_percent(interval=1, percpu=True)}")