Secret_number = 9
guess_count = 0
guess_limit = 3

# gus = int(input("Enter your number : "))

while guess_count < guess_limit :
    guess = int(input("Enter Your Number : "))
    guess_count += 1

if guess == Secret_number:
    print("You Won!")
    print("The Number is :",Secret_number)
else:
    print("You losse!")
