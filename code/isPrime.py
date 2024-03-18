import factors

def isPrime(n):
    return factors.factors(n) == [1, n]


if __name__ == "__main__":
    print(isPrime(int(input("n: "))))