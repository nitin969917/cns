import random

# Helper: Clean text to uppercase alphabets
def clean(text):
    return "".join([ch.upper() for ch in text if ch.isalpha()])

# 1. CAESAR CIPHER
def caesar():
    print("=== 1. CAESAR CIPHER ===")
    pt = input("Enter Plaintext: ")
    key = int(input("Enter Key Number (e.g., 14): "))
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Encrypt
    ct = ""
    for ch in clean(pt):
        idx = alpha.index(ch)
        ct += alpha[(idx + key) % 26]
        
    # Decrypt
    dt = ""
    for ch in ct:
        idx = alpha.index(ch)
        dt += alpha[(idx - key + 26) % 26]
        
    print("Encrypted:", ct)
    print("Decrypted:", dt)

# 2. MONOALPHABETIC CIPHER
def monoalphabetic():
    print("\n=== 2. MONOALPHABETIC CIPHER ===")
    pt = input("Enter Plaintext: ")
    seed_val = int(input("Enter UID for Random Key Seed (e.g., 2025301008): "))
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Generate key alphabet using UID seed
    random.seed(seed_val)
    key_list = list(alpha)
    random.shuffle(key_list)
    key_str = "".join(key_list)
    print("Generated Key Alphabet:", key_str)
    
    # Encrypt
    ct = "".join([key_str[alpha.index(ch)] for ch in clean(pt)])
    
    # Decrypt
    dt = "".join([alpha[key_str.index(ch)] for ch in clean(ct)])
    
    print("Encrypted:", ct)
    print("Decrypted:", dt)

# 3. VIGENÈRE CIPHER
def vigenere():
    print("\n=== 3. VIGENÈRE CIPHER ===")
    pt = input("Enter Plaintext: ")
    key = clean(input("Enter Keyword (e.g., UYEAU): "))
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    clean_pt = clean(pt)
    
    # Encrypt
    ct = ""
    for i, ch in enumerate(clean_pt):
        shift = alpha.index(key[i % len(key)])
        ct += alpha[(alpha.index(ch) + shift) % 26]
        
    # Decrypt
    dt = ""
    for i, ch in enumerate(ct):
        shift = alpha.index(key[i % len(key)])
        dt += alpha[(alpha.index(ch) - shift + 26) % 26]
        
    print("Encrypted:", ct)
    print("Decrypted:", dt)

# 4. PLAYFAIR CIPHER
def playfair():
    print("\n=== 4. PLAYFAIR CIPHER ===")
    pt = clean(input("Enter Plaintext: ")).replace("J", "I")
    key = clean(input("Enter Key Keyword (e.g., UYEAU): ")).replace("J", "I")
    
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: J is omitted
    
    # 1. Build 5x5 Matrix
    used = ""
    for ch in key + alpha:
        if ch not in used:
            used += ch
    matrix = [list(used[i:i+5]) for i in range(0, 25, 5)]
    
    def find_pos(ch):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == ch:
                    return r, c
                    
    # 2. Split Plaintext into Pairs
    pairs = []
    i = 0
    while i < len(pt):
        a = pt[i]
        b = pt[i+1] if i+1 < len(pt) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
            
    # 3. Encrypt Pairs
    ct = ""
    for a, b in pairs:
        r1, c1 = find_pos(a)
        r2, c2 = find_pos(b)
        if r1 == r2:
            ct += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            ct += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            ct += matrix[r1][c2] + matrix[r2][c1]
            
    print("Encrypted:", ct)

# 5. HILL CIPHER (2x2 Matrix)
def hill():
    print("\n=== 5. HILL CIPHER (2x2) ===")
    pt = clean(input("Enter Plaintext: "))
    print("Enter 2x2 Matrix Key values (a, b, c, d):")
    a = int(input("Row 1 Col 1 (e.g., 21): "))
    b = int(input("Row 1 Col 2 (e.g., 25): "))
    c = int(input("Row 2 Col 1 (e.g., 4): "))
    d = int(input("Row 2 Col 2 (e.g., 11): "))
    
    if len(pt) % 2 != 0:
        pt += 'X'
        
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Encrypt
    ct = ""
    for i in range(0, len(pt), 2):
        p1 = alpha.index(pt[i])
        p2 = alpha.index(pt[i+1])
        c1 = (a * p1 + b * p2) % 26
        c2 = (c * p1 + d * p2) % 26
        ct += alpha[c1] + alpha[c2]
        
    # Helper: Mod Inverse for Decryption Matrix
    def mod_inverse(val, m=26):
        for x in range(1, m):
            if (val * x) % m == 1:
                return x
        return 1

    # Decrypt Matrix Calculation
    det = (a * d - b * c) % 26
    det_inv = mod_inverse(det)
    
    inv_a = (d * det_inv) % 26
    inv_b = (-b * det_inv) % 26
    inv_c = (-c * det_inv) % 26
    inv_d = (a * det_inv) % 26
    
    dt = ""
    for i in range(0, len(ct), 2):
        c1 = alpha.index(ct[i])
        c2 = alpha.index(ct[i+1])
        p1 = (inv_a * c1 + inv_b * c2) % 26
        p2 = (inv_c * c1 + inv_d * c2) % 26
        dt += alpha[p1] + alpha[p2]
        
    print("Encrypted:", ct)
    print("Decrypted:", dt)

# MAIN EXECUTION

caesar()
monoalphabetic()
vigenere()
playfair()
hill()