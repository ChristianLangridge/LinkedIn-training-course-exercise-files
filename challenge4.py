def allPrimesUpTo(number):
    primesFound = [2]
    for candidate in range (3, number):
        for prime in primesFound:
            if prime*prime > candidate:
                continue 
            if candidate % prime == 0:
                continue 
        else: 
            primesFound.append(candidate)
    return primesFound


print(allPrimesUpTo(1000))


