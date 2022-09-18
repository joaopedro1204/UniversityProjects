a = int(input('Enter dividend: '))
b = int(input('Enter divider: '))

q, r = 0, a

while r >= b:
    q += 1
    r -= b

print(f'Result: {q}\nRest: {r}')
