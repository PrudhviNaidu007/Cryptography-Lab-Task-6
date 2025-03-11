def power(a, b, p):
   return pow(a, b) % p

def main():
    P = int(input("Enter a prime number (P): "))
    G = int(input("Enter a primitive root (G): "))

    a = int(input("Enter Alice's private key (a): "))
    x = power(G, a, P)

    b = int(input("Enter Bob's private key (b): "))
    y = power(G, b, P)

    ka = power(y, a, P)
    kb = power(x, b, P)

    print("Secret key for Alice:", ka)
    print("Secret key for Bob:", kb)

if __name__ == "__main__":
    main()
