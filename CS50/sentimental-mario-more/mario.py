from cs50 import get_int

while (True):
    try:
        n = int(get_int("Height: "))
        if n > 0 and n < 9:
            break
    except ValueError:
        continue
for i in range(1, n+1):
    block = (n-i)*' ' + i*'#'
    # print(block + '  ' + block[-1:-i-1:-1])
    print(block + '  ' + block[n-i:])