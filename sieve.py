def sieve(limit):
    # We know 2 and 3 to be prime
    res = []
    if limit < 2:
        return res  # []
    res.extend([False, True])
    if limit == 2:
        return res  # [False, True]
    res.append(True)
    if limit == 3:
        return res  # [False, True, True]

    res.extend([False] * (limit - 2))

    i = 1
    while i * i <= limit:
        j = 1
        while j * j <= limit:
            n = (4 * i * i) + (j * j)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                res[n] ^= True

            n = (3 * i * i) + (j * j)
            if n <= limit and n % 12 == 7:
                res[n] ^= True

            n = (3 * i * i) - (j * j)
            if i > j and n <= limit and n % 12 == 11:
                res[n] ^= True

            j += 1
        i += 1

    r = 5
    while r * r <= limit:
        if res[r]:
            for i in range(r * r, limit + 1, r * r):
                res[i] = False
        r += 1

    return res


def pick_prime(primes, min_size=1000):
    """returns a suitable prime to use as modulus"""
    # if no prime large enough exists, use last one on list
    if len(primes) <= min_size:
        return len(primes)

    for i in range(len(primes)):
        if i >= min_size:
            return i


def hash_string(string, modulus):
    """implements polynomial rolling of string keys"""
    hash_value = 5381
    for char in string:
        # hash = 33 XOR ord(c)
        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)

    return hash_value % modulus


def main():
    # generate primes list to use as modulus
    primes = sieve(10000)  # modify limit based on your needs
    modulus = pick_prime(primes, 1000)

    test_array = ["alpha", "beta", "gamma", "delta", "epsilon"]
    for string in test_array:
        hash_value = hash_string(string, modulus)
        print(f"Hash of {string} is {hash_value}")


if __name__ == '__main__':
    main()
