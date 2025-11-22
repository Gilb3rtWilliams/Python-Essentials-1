y=input('Enter an integer between 0 and 1024 -- ')

x=int(y)

a=0

b=1024


test=True

while test == True:

    if y.isnumeric():

        x=int(y)

if x > 1024 or x < 0:

            x=input('The entered number is not between 0 and 1024. Please re-enter an integer between 0 and 1024 -- ')

            test=True

if x == 0:

    print('Your number is 0 , thank you for playing.')

    test=False

else:

    if x == 1024:

        print('Your number is 1024, thank you for playing.')

        test=False

    while test == True:

        n=int((a+b)/2)

        if n == x:

            print('Your number is ', n, ', thank you for playing.')

            break

        else:

            if n < x:

                a=n

            else:

                b=n
