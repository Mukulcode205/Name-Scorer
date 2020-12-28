try:
    import random

    password = input("Enter your name please\n>>>")
    guess_password = ''
    char = 'abcdefghijklmnopqrstuvwxyz'
    char_list = list(char)
    n = 1
    while guess_password != password:
        guess_password = random.choices(char_list, k=len(password))
        print(n, "*******", guess_password, "*******")
        n = n + 1
        if guess_password == list(password):
            print("your name is", guess_password)
            print("and your name rareity score is: ", n - 1)
            x = input("type quit to exit")
            break
except Exception as e:
    print("Invalid Input")