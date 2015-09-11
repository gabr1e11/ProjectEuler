
import math
import sets

def find_prime(number):
    i = 2
    while i<=number/2:
        if number%i==0:
            return i
        i += 1
    return number

def factorize_primes(number):
    primes = []
    while number > 1:
        prime = find_prime(number)
        primes.append(prime)
        number = number/prime

    return primes

def first_nth_primes(n):
    primes = sets.Set(xrange(2,n))
    for i in xrange(2,n):
        product = i*2
        while product < n:
            primes.discard(product)
            product += i

    return primes

def get_divisors(number):
    return [ n for n in range(1, number) if number%n==0 ]

def fibonacci():
    prev = 0
    current = 1
    while True:
        yield current
        tmp = current
        current += prev
        prev = tmp

def divide_1(number, length=10):
    reminder = 10
    while reminder != 0 and length>0:
        yield reminder/number
        reminder = 10*(reminder%number)
        length -= 1

def find_cycle(number):
    rem_set = sets.Set()
    reminder = 10
    while reminder != 0:
        rem_set.add(reminder)
        reminder = 10*(reminder%number)
        if reminder in rem_set:
            return len(rem_set)

    return 0
