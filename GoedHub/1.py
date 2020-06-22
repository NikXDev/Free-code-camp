def multiple(number):
    if number in range(1500, 2701):
        if number % 7 == 0 and number % 5 == 0:
            print(f"{number} Is Divisible By 7 And Multiple Of 5")
        else:
            print(f"{number} Is Not Divisible By 7 And Multiple Of 5")
    else:
        print("The Number Is Not In The Given Range")

number = int(input())
multiple(number)