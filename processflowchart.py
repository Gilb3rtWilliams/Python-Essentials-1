a = 0
b = 128
t = 0
M = (a + b) / 2
print("Is your number " + str(M) + "?")
t = t + 1
t = input("Enter 'h' to indicate the number is higher, 'l' to indicate the number is lower, and 'c' to indicate I guessed correctly.")
while t != 'c':
    if t == 'h':
        a = M
    elif t == 'l':
        b = M
    M = (a + b) / 2
    print("Is your number " + str(M) + "?")
    t = input("Enter 'h' to indicate the number is higher, 'l' to indicate the number is lower, and 'c' to indicate I guessed correctly.")
print("Game over. Your secret number was: " + str(M))
