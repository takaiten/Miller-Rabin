import random


def gcd(a, b):
    """
    Euclidean Algorithm to Calculate
    Greatest Common Divisor
    Returns: Greatest Common Divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a


def square_and_multiply(x, k, p=None):
    """
    Square and Multiply Algorithm
    Returns: x**k or x**k mod p when p is given
    """
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r ** 2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r


def miller_rabin_test(n, tests=5):
    if n == 2 or n == 3:  # 2 is the only even prime
        return True
    if n % 2 == 0:  # if n is an even number it can't be prime
        return False

    n1 = n - 1
    s = 0
    t = n1  # n-1 = 2**s * t

    while t % 2 == 0:
        t >>= 1
        s += 1

    # test that n-1 = 2**s * t
    assert n - 1 == 2 ** s * t

    def witness(a):
        """
        Returns: True, if there is a witness that p is not prime.
                False, when p might be prime
        """
        z = square_and_multiply(a, t, n)
        if z == 1:
            return False

        for i in range(s):
            z = square_and_multiply(a, 2 ** i * t, n)
            if z == n1:
                return False
        return True

    for _ in range(tests):
        a = random.randrange(2, n - 2)
        if not gcd(a, n) == 1:
            return False
        if witness(a):
            return False

    return True


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
          103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
          223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337,
          347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
          463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
          607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
          743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
          883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def gen_odd_n_byte_number(n):
    """
    Generates random n-byte number (from 0 to 2**n)
    And sets first and last bits to 1
    """
    return random.getrandbits(n) | ((2 ** n >> 1) + 1)


def check_prime_division(n, primes_count=len(primes)):
    """
    Checks if n can be divided primes_count of primes
    Returns: True if n can't be divided by number primes
        False if n was divided by some prime
    """
    for prime in primes[:primes_count]:
        if n % prime == 0:
            return False
    return True


if __name__ == '__main__':
    byte_count = int(input('Enter number of bytes: '))
    num = gen_odd_n_byte_number(byte_count)

    while not check_prime_division(num) and not miller_rabin_test(num, 5):
        num = gen_odd_n_byte_number(byte_count)

    print('Random prime number:', num)

    # num = int(input('Enter number to which primes are gonna be found: '))
    # miller_rabin_primes = []
    # for i in range(2, num):
    #     if miller_rabin_test(i):
    #         miller_rabin_primes.append(i)
    # print('Prime numbers bellow', num, 'selected by Miller Rabin Test:')
    # print(miller_rabin_primes)
    # print('True prime numbers:')
    # print(primes[:primes.index(miller_rabin_primes[len(miller_rabin_primes) - 1]) + 1])
