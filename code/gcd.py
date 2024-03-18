def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a


if __name__ == "__main__":
    print(gcd(int(input("a: ")), int(input("b: "))))