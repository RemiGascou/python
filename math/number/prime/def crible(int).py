def crible(stop):
    # Sieve of Eratosthene
    numbers = [2]
    for k in range(3,stop+1,2):
        numbers.append(k)
    for number_p in numbers :
        for number in numbers:
            if number % number_p == 0 and number != number_p:
                numbers.remove(number)
    return numbers