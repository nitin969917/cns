import random
import time

# 0. HELPER: Greatest Common Divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 1. FERMAT PRIMALITY TEST
def fermat_test(num, k):
    if num <= 1:
        return "Composite"
    if num <= 3:
        return "Prime"
    for _ in range(k):
        a = random.randint(2, num - 2)
        # Formula: a^(num-1) % num == 1
        if gcd(a, num) != 1 or pow(a, num - 1, num) != 1:
            return "Composite"
    return "Prime"

# 2. EULER PRIMALITY TEST (Euler's Criterion)
def euler_test(num, k):
    if num <= 1:
        return "Composite"
    if num % 2 == 0 and num > 2:
        return "Composite"
    if num <= 3:
        return "Prime"
    for _ in range(k):
        a = random.randint(2, num - 2)
        if gcd(a, num) != 1:
            return "Composite"
        # Formula: a^((num-1)/2) % num must be 1 or (num - 1)
        rem = pow(a, (num - 1) // 2, num)
        if rem != 1 and rem != num - 1:
            return "Composite"
    return "Prime"

# 3. MILLER-RABIN PRIMALITY TEST
def miller_rabin_test(num, k):
    if num <= 1:
        return "Composite"
    if num % 2 == 0 and num > 2:
        return "Composite"
    if num <= 3:
        return "Prime"

    # Step 1: Write num - 1 as 2^r * d
    d = num - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Step 2: Check k random bases
    for _ in range(k):
        a = random.randint(2, num - 2)
        x = pow(a, d, num)

        if x == 1 or x == num - 1:
            continue

        composite = True
        for _ in range(r - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                composite = False
                break

        if composite:
            return "Composite"
            
    return "Prime"

# MAIN PROGRAM: Take Input Once and Test All Three
if __name__ == "__main__":
    print("=== LAB 1: PRIMALITY TESTING ===")
    num = int(input("Enter number to test (e.g., 561): "))
    k = int(input("Enter number of bases k (e.g., 5): "))

    print(f"\n--- Testing Results for {num} ---")

    # 1. Fermat Test
    t0 = time.perf_counter()
    res_f = fermat_test(num, k)
    t_f = (time.perf_counter() - t0) * 1000
    print(f"Fermat Test       : {res_f} ({t_f:.4f} ms)")

    # 2. Euler Test
    t0 = time.perf_counter()
    res_e = euler_test(num, k)
    t_e = (time.perf_counter() - t0) * 1000
    print(f"Euler Test        : {res_e} ({t_e:.4f} ms)")

    # 3. Miller-Rabin Test
    t0 = time.perf_counter()
    res_mr = miller_rabin_test(num, k)
    t_mr = (time.perf_counter() - t0) * 1000
    print(f"Miller-Rabin Test : {res_mr} ({t_mr:.4f} ms)")