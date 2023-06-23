import random

def is_number(temp):
    # this function will check if the input is a number
    # if it is a number, it will return True
    # if it is not a number, it will return False
    try:
        return int(temp)
    except:
        raise Exception(f"this {temp} is not a number")

def range_ok(temp_1, temp_2):
    # this function will check if temp_1 is lower than temp_2
    if temp_1 < temp_2:
        print("range is ok")
    else:
        raise Exception(f"the first number {temp_1} is not lower than the second number {temp_2}")

def main():
    first_number, second_number = is_number(input("please enter the first number: ")), is_number(input("please enter the second number: "))
    range_ok(first_number,
             second_number)
    guess = random.randint(first_number,
                           second_number)
    print("program has generated a random number between",
          first_number,
          "and",
          second_number)
    print("you have 5 chances to guess the number")
    for i in range(5):
        user_guess = is_number(input("please enter your guess: "))
        if user_guess == guess:
            print("you guessed the number correctly")
            break
        elif user_guess > guess:
            print("your guess is higher than the number")
        else:
            print("your guess is lower than the number")
    else:
        print("you have used all your chances")
        print("the number was",
              guess)

if __name__ == "__main__":
    main()
