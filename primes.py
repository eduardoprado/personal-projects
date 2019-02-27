numprimes = 30
count = 0
potentialprime = 2
vectorprime = [0 for i in range(numprimes)]


def primetest(potentialprime):
    divisor = 2
    while divisor <= potentialprime:
        if potentialprime == 2:
            return True
        elif potentialprime % divisor == 0:
            return False
        while potentialprime % divisor != 0:
            if potentialprime - divisor > 1:
                divisor += 1
            else:
                return True

while count < int(numprimes):
    if primetest(potentialprime) == True:
        vectorprime[count] = potentialprime
        count += 1
        potentialprime += 1
    else:
        potentialprime += 1

for i in range (0, numprimes):
    print (vectorprime[i])