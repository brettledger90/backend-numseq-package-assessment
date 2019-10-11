def primes(n):
    prime_list = []
    for i in range(n):
        if is_prime(n):
            prime_list.append(i)
    return prime_list

             
def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):  
        if n%i==0:
            return False    

    return True