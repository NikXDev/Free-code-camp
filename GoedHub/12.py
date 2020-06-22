def table(number):
    for i in range(1, 11):
        product = i * number
        print(f"{i} x {number} = {product}")

number = int(input())
table(number)