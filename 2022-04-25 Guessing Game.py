#as long as we fail to guess the secret word, it's going to keep asking for input
secret_word= "Nishi"
guess = ""
#guess count will keep track of the number of tries as it will increase by 1 everytime the loop runs
guess_count = 0
#if you run out of 3 turns, you lose
guess_limit = 3
#Boolean, when true, you lose the game
out_of_guesses= False
#not(out_of_guesses) condition makes sure you have guesses left, if boolean is true, you lose
while guess != secret_word and not(out_of_guesses):
#first, check if the user has any more guesses
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
#at the end, either you ran out of guesses or you won
if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")