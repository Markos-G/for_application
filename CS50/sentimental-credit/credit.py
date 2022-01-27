from cs50 import get_string

card = get_string("NUmber: ").strip()
length = len(card)

sum = 0
for i in range(length-2, -1, -2):
    # print(i)
    x = int(card[i]) * 2
    if x > 9:
        x = str(x)
        sum += int(x[0]) + int(x[1])
    else:
        sum += x

for i in range(length-1, 0, -2):
    # print(i)
    sum += int(card[i])

if length == 15 and int(card[0:2]) in [34, 37]:
    print("AMEX")
elif length >= 13 and length <= 16 and int(card[0]) == 4:
    print("VISA")
elif int(card[0:2]) in range(51, 56) and length == 16:
    print("MASTERCARD")
else:
    print("INVALID")