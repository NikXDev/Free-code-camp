secret_word = "niharika"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Oopsssssssssss......You Lose...!!!")
else:
    print("Yeah....You Win......!!!!!!!!!!!")