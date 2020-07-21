#1 isPrime
def isPrime(a):
    # num we will use later
    ramnum = 0
    compnum = a - 2
    # check if a is positive
    if (a > 0):
        # check if a is smaller or equal to 2
        if (a <= 2):
            print('{} is a prime'.format(a))
        else:
            # prime is divisible only by 1 and itself
            for i in range(2, a):
                if (a % i != 0):
                    ramnum = ramnum + 1
            if (ramnum == compnum):
                print('{} is a prime'.format(a))
            else:
                print('{} is not a prime'.format(a))
#testcase
isPrime(97)

#2 guess the number
import random
# the random number generator
number_to_guess = random.randint(1, 1001)
# user input
input_num = int(input('lets take a wild guess: '))
print('you number is: ' + str(input_num))
# if the two num are not matched
while(input_num != number_to_guess):
    # smaller
    if (input_num > number_to_guess):
        input_num = int(input('the random num is smaller: '))
    # larger
    else:
        input_num = int(input('the random num is larger: '))

#3 strSTR
def strStr(source, target):
    # pointers
    a = 0
    score = 0
    # outer loop but only would go into inner loop once
    while (a <= (len(source) - len(target))):
        # condition
        if (source[a] == target[0]):
            # compare
            for i in range(len(target) - 1):
                if (source[a + 1] == target[i + 1]):
                    a = a + 1
                    score = score + 1
        else:
            a = a + 1
    if (score == len(target) - 1):
        return 1
    return -1
# testcase
print(strStr('strong', 'ste'))

