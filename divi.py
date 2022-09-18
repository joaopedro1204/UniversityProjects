a = int(input('Enter dividend: '))
b = int(input('Enter divider: '))

r, q = a, 0

while r >= b:
    q += 1
    r -= b

print(f'Result: {q}\nRest: {r}')
