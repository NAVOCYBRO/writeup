Easy RSA Write-up
Challenge Information

Category: Cryptography

Difficulty: Easy

Description:
A simple RSA implementation where we're given the public key (n, e) and ciphertext (c). The challenge is to decrypt the ciphertext to retrieve the original message.

Given Problem: 

“The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, the ‘factoring problem’” -Wikipedia"

given rsa_easy.py below there 
#################################################################################################################


    import random
    from sympy import nextprime, mod_inverse


    def gen_primes(bit_length, diff=2**525):
    p = nextprime(random.getrandbits(bit_length))
    q = nextprime(p + random.randint(diff//2, diff))
    return p, q


    def gen_keys(bit_length=1024):
    p, q = gen_primes(bit_length)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    d = mod_inverse(e, phi)

    return (n, e)


    def encrypt(message, public_key):
    n, e = public_key
    message_int = int.from_bytes(message.encode(), 'big')
    ciphertext = pow(message_int, e, n)
    return ciphertext


    if __name__ == "__main__":
    public_key = gen_keys()

    message = "FLAG"
    ciphertext = encrypt(message, public_key)

    f = open("easy_rsa.txt", "a")
    f.write(f"n: {public_key[0]} \n")
    f.write(f"e: {public_key[1]} \n")
    f.write(f"c: {ciphertext}")
    f.close()
    
    

##########################################

 Give easy_rsa.txt below :

    n: 26518484190072684543796636642573643429663718007657844401363773206659586306986264997767920520901884078894807042866105584826044096909054367742753454178100533852686155634326578229244464083405472076784252798532101323300927917033985149599262487556178538148122012479094592746981412717431260240328326665253193374956717147239124238669998383943846418315819353858592278242580832695035016713351286816376107787722262574185450560176240134182669922757134881941918668067864082251416681188295948127121973857376227427652243249227143249036846400440184395983449367274506961173876131312502878352761335998067274325965774900643209446005663 
    e: 65537 
    c: 14348338827461086677721392146480940700779126717642704712390609979555667316222300910938184262325989361356621355740821450291276190410903072539047611486439984853997473162360371156442125577815817328959277482760973390721183548251315381656163549044110292209833480901571843401260931970647928971053471126873192145825248657671112394111129236255144807222107062898136588067644203143226369746529685617078054235998762912294188770379463390263607054883907325356551707971088954430361996309098504380934167675525860405086306135899933171103093138346158349497350586212612442120636759620471953311221396375007425956203746772190351265066237



To solve this RSA challenge, we should use Fermat's Factorization Method because of how the primes were generated.

    The key generation in rsa_easy.py shows:
    def gen_primes(bit_length, diff=2**525):
    p = nextprime(random.getrandbits(bit_length))
    q = nextprime(p + random.randint(diff//2, diff))

 This makes p and q close to each other (since q is generated near p), which is precisely the condition where Fermat's factorization excels.

 1. Factor n using Fermat's Method

Fermat's factorization works when n = p*q and p and q are close (i.e., |p - q| is small relative to n). The idea is to express n as:

 n = a² - b²  
=> n = (a - b)(a + b)
where a = (p + q)/2 and b = (q - p)/2.

2. Compute the private exponent d

Once you have p and q, calculate:

    φ(n) = (p - 1) * (q - 1)

    d = e⁻¹ mod φ(n) (modular inverse of e)

To solve this problem I improve python code the file name is easy.py 

Using venv (built into Python)

#Create the virtual environment (replace 'ctf' with your preferred name)
    
    python3 -m venv ~/venvs/ctf

Activate the environment

    source ~/venvs/ctf/bin/activate

Your terminal prompt should now show the environment name
 
     (ctf)-user@host:~$

Install packages while the environment is active

    pip install pycryptodome gmpy2


┌──(ctf)─(navocybro㉿kali)-[/home]

└─$ python easy.py easy_rsa.txt

Decrypting...

FLAG: squ1rrel{who's_your_favorite_mathemetician?}
                                                                                                                                                                       
┌──(ctf)─(navocybro㉿kali)-[/home]

└─$ 

Deactivate when you're done
    
    deactivate
