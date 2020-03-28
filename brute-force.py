# by @hackerxbella
# import <3
# based off of https://stackoverflow.com/questions/40269605/how-to-create-a-bruteforce-password-cracker-for-alphabetical-and-alphanumerical

# import time functionality to track time and a Python tool to easily iterate
import itertools
import time


# brute force the password
def findPassword(uPasswordSet, charSet):
    # start counting how long this takes
    start = time.time()
    # move characterset into a new variable
    chars = charSet
    # move password character set into a new variable
    passwordSet = uPasswordSet
    # reset the number of attempts at cracking this
    attempts = 0
    # get the length of the password worth iterating over - lets go with 10 but even that is a lot
    length = 10
    for i in range(1, length):
        print("thinking...")
        # run through each character in the characterset for the length of the string, incrementing one each time. i.e. firs time through this will go 1....2....3...etc, then second time through it will go 11...12...21...22... etc
        for character in itertools.product(chars, repeat=i):
            # increment the counter so we know that we have made another attempt
            attempts += 1
            # turn the character into a string
            character = ''.join(character)
            # if we've guessed the password, stop the timer and return. hooray! otherwise, continue.
            if character == passwordSet:
                end = time.time()
                distance = end - start
                return (attempts, distance, passwordSet)

# lets ask for a password
uPassword = raw_input("Enter a Password: ")
# all characters that will be used as input
characters = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
# run the actual function to find the password
tries, pTime, password = findPassword(uPassword, characters)
# output the results when they finally are done!
print("The password %s was found in in %s tries and %s seconds. Try a better password." % (password, tries, pTime))