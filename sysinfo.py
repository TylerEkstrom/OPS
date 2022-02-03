import psutil

x = psutil.cpu_times()

print(x)

print("--------System Info----------")
print(f"[~] User Time: {x.user}")
print(f"[~] User Time: {x.system}")
print(f"[~] User Time: {x.interrupt}")
print("---------End System Info-------")
