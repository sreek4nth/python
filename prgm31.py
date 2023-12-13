import math
import statistics
import time
print("the value of pi is",math.pi)
seconds=time.time()
print("seconds since epoch(the point where time begins)=",seconds)
li=[1,2,3,3,2,2,2]
print("the average of list value is:",end="")
print(statistics.mean(li))
loacl_time=time.ctime(seconds)
print("local time:",loacl_time)