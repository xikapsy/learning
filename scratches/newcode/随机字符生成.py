import time

timesdata = time.time()

print(timesdata)
timesdata = int(timesdata)
print(timesdata)
timesdata =timesdata %26
print("%",timesdata)

print(chr(ord("A")+timesdata))
