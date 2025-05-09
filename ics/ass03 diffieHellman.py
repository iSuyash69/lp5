def diffieHellman():
    
    print("\n-----------Diffie-Hellman Key Exchange----------\n")

    p=int(input("Enter a large prime number (p): "))
    g=int(input("Enter a primitive root modulo p (g): "))

    a=int(input("\nUser A, enter your private key (a): "))
    b=int(input("User B, enter your private key (b): "))

    # public-key = g^private-key mod p 
    A=pow(g,a,p)  # A = g^a mod p 
    B=pow(g,b,p)  # B = g^b mod p

    print(f"\nUser A generated a public key: {A}")
    print(f"User B generated a public key: {B}")
    print(f"Public keys are shared with each other")

    # secret key = other's public-key^own private-key mod p
    shared_secret_key_A=pow(B,a,p)
    shared_secret_key_B=pow(A,b,p)

    print(f"\nUser A computes a shared secret key: {shared_secret_key_A}")
    print(f"User B computes a shared secret key: {shared_secret_key_B}")

    if(shared_secret_key_A==shared_secret_key_B):
        print(f"\nShared secret established successfully! Shared secret Key: {shared_secret_key_B}")
    else:
        print("\n Error: Shared secret keys do not match")

diffieHellman()
