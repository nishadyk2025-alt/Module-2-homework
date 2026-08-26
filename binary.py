num = int(input("Enter a decimal number: "))

binary = 0
place = 1

while num > 0:
    for i in range(1):
        remainder = num % 2
        binary = binary + remainder * place
        place = place * 10
        num = num // 2

print(binary)