import time
import matplotlib.pyplot as plt


def fib_iterative(n):
    first = 0
    second = 1
    for i in range(n):
        first, second = second, first + second
    return first

def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n-2) + fib_recursive(n-1)

runtime1 = []
runtime2 = []
n = []
num = int(input("Enter the largest term: "))
step = int(input("Enter the step: "))
for i in range(0, num, step):
    start1 = time.time()
    fib_iterative(i)
    end = time.time()
    runtime1.append(end - start1)
    start2 = time.time()
    fib_recursive(i)
    end = time.time()
    runtime2.append(end - start2)
    n.append(i)
print()
plt.plot(n, runtime1, label='fib_iterative(n)')
plt.plot(n, runtime2, label='fib_recursive(n)')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime Comparison')
plt.legend()
plt.show()
