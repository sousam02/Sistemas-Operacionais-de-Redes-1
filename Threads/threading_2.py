import math
import concurrent.futures

executor = concurrent.futures.ThreadPoolExecutor()
future1 = executor.submit(pow, 2, 2)
result1 = future1.result()
future2 = executor.submit(math.sqrt, result1)
print(future2.result())