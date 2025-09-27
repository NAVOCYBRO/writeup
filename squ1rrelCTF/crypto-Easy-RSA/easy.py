import gmpy2
from Crypto.Util.number import long_to_bytes
import sys

def fermat_factor(n):
    """
    Fermat's factorization method for close primes
    """
    a = gmpy2.isqrt(n) + 1
    b2 = a*a - n
    
    while not gmpy2.is_square(b2):
        a += 1
        b2 = a*a - n
    
    b = gmpy2.isqrt(b2)
    return (a - b, a + b)

def decrypt(n, e, c):
    # Factorize n
    p, q = fermat_factor(n)
    assert p * q == n, "Factorization failed!"
    
    # Compute private key
    phi = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phi)
    
    # Decrypt
    m = pow(c, d, n)
    return long_to_bytes(m).decode()

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as f:
        data = f.read()
    
    try:
        n = int(data.split('n:')[1].split()[0])
        e = int(data.split('e:')[1].split()[0])
        c = int(data.split('c:')[1].split()[0])
    except (IndexError, ValueError) as err:
        print(f"Error parsing input file: {err}")
        sys.exit(1)
    
    print("Decrypting...")
    flag = decrypt(n, e, c)
    print(f"\nFLAG: {flag}")

if __name__ == "__main__":
    main()
