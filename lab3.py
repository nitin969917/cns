import math

# 0. HELPER: Modular Inverse (Single loop used everywhere)
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

# 1. RSA
def rsa():
    print("=== RSA ===")
    p = int(input("Enter p (e.g., 61): "))
    q = int(input("Enter q (e.g., 53): "))
    msg = int(input("Enter message number (e.g., 42): "))

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    while math.gcd(e, phi) != 1:
        e += 2
    d = mod_inverse(e, phi)

    cipher = pow(msg, e, n)
    plain = pow(cipher, d, n)
    print("Encrypted:", cipher)
    print("Decrypted:", plain)

# 2. ELGAMAL
def elgamal():
    print("\n=== ELGAMAL ===")
    p = int(input("Enter prime p (e.g., 23): "))
    g = int(input("Enter generator g (e.g., 5): "))
    x = int(input("Enter private key x (e.g., 6): "))
    k = int(input("Enter random k (e.g., 15): "))
    msg = int(input("Enter message number (e.g., 10): "))

    y = pow(g, x, p)  # Public key component
    c1 = pow(g, k, p)
    c2 = (msg * pow(y, k, p)) % p

    # Decryption
    s = pow(c1, x, p)
    s_inv = mod_inverse(s, p)
    plain = (c2 * s_inv) % p

    print(f"Ciphertext: ({c1}, {c2})")
    print("Decrypted:", plain)

# 3. DIFFIE-HELLMAN
def diffie_hellman():
    print("\n=== DIFFIE-HELLMAN ===")
    p = int(input("Enter prime p (e.g., 23): "))
    g = int(input("Enter base g (e.g., 5): "))
    a = int(input("Enter Alice private key (e.g., 6): "))
    b = int(input("Enter Bob private key (e.g., 15): "))

    A = pow(g, a, p)
    B = pow(g, b, p)

    key_A = pow(B, a, p)
    key_B = pow(A, b, p)

    print("Alice Public:", A, "| Shared Key:", key_A)
    print("Bob Public  :", B, "| Shared Key:", key_B)

# 4. ECC POINT MULTIPLICATION
def ecc():
    print("\n=== ECC POINT MULTIPLY ===")
    p = int(input("Enter prime p (e.g., 17): "))
    a = int(input("Enter curve param a (e.g., 2): "))
    gx = int(input("Enter G x (e.g., 5): "))
    gy = int(input("Enter G y (e.g., 1): "))
    k = int(input("Enter private scalar k (e.g., 3): "))

    # Simple point addition helper inside ECC
    def point_add(P, Q):
        if P is None: return Q
        if Q is None: return P
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and y1 == y2:
            m = ((3 * x1 * x1 + a) * mod_inverse(2 * y1, p)) % p
        else:
            m = ((y2 - y1) * mod_inverse((x2 - x1) % p, p)) % p
        x3 = (m * m - x1 - x2) % p
        y3 = (m * (x1 - x3) - y1) % p
        return (x3, y3)

    # Scalar multiplication: Repeated Addition (k times)
    result = None
    G = (gx, gy)
    for _ in range(k):
        result = point_add(result, G)

    print("Result Point (k * G):", result)

# Run All Algorithms

rsa()
elgamal()
diffie_hellman()
ecc()