import sys
import functools

with open(sys.argv[1]) as file:
    lines = file.read().strip().split("\n")

devices = {}
for line in lines:
    device_name, *outputs = line.split()
    device_name = device_name[:-1]
    devices[device_name] = outputs

@functools.cache
def count_paths(current_device, goal):
    if current_device == goal:
        return 1
    return sum(count_paths(output, goal) for output in devices.get(current_device, []))

print(count_paths("you", "out"))
print(count_paths("svr", "fft")*count_paths("fft", "dac")*count_paths("dac", "out") + count_paths("svr", "dac")*count_paths("dac", "fft")*count_paths("fft", "out"))
