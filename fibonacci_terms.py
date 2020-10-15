n = int(input("No.of numbers of fibonacci:"))
def fibonacci(n):
    y = 0
    z = 1
    count = 0
    while count <= n:
         print(y)
         temp = y
         y = z
         z = temp + z
         count += 1
                 
fibonacci(n)