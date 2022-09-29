import time
start_time = time.time()

for i in range(1,100,2):
        print(i)


print((time.time() - start_time)*100,"ms")