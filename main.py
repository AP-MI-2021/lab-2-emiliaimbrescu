
#Problema 5
def is_palindrome(n : int) -> bool:
    """
    Verifica daca numarul dat este un palindrom
    :param n: numarul verificat
    :return: true or false
    """
    inverse = 0
    length = len(str(n))

    for i in range(length // 2):
        inverse*=10
        inverse+=n%10
        n//=10

    if length % 2 == 1:
        n//=10

    return n == inverse

def test_is_palidnrome():
    """Testeaza is_palindrome
    """
    assert is_palindrome(1234321) == True
    assert is_palindrome(52525) == True
    assert is_palindrome(1234) == False
    assert is_palindrome(5) == True
    assert is_palindrome(101) == True

test_is_palidnrome()

def input_is_palindrome():
    x = int(input("Functia verifica daca un numar este palindrom. Ce numar doresti sa verifici? "))
    if is_palindrome(x):
        print(x, "este palindrom.")
    else:
        print(x, "nu este palindrom.")



#problema 10

def factorial(n: int) -> int:
    """
    Calculeaza si returneaza factorialul unui numar
    :param n: Numarul al carui factorial e calculat
    :return: Factorialul
    """
    fact = 1
    for i in range(1,n+1):
        fact*=i

    return fact

def get_n_choose_k(n: int, k: int) -> int:
    """
    Calculeaza combinari de n luate cate k
    :param n: Marimea multimii din care se iau elemente
    :param k: Marimea unei combinari
    :return: Numarul de combinari
    """
    return (factorial(n)/(factorial(k) * factorial(n-k)))

def test_get_n_choose_k():
    """Testeaza functia get_n_choose_k
    """
    assert get_n_choose_k(49,6) == 13983816.0
    assert get_n_choose_k(10,0) == 1.0
    assert get_n_choose_k(5,4) == 5.0
    assert get_n_choose_k(52,5) == 2598960.0
    assert get_n_choose_k(12,5) == get_n_choose_k(12,7) == 792

def input_get_n_choose_k():
    print("Functia calculeaza combinari de n luate cate k.")
    n = int(input("n="))
    k = int(input("k="))
    print(f"Exista {get_n_choose_k(n,k)} combinari de {n} luate cate {k}.")





#problema 1
def is_prime(n: int):
    """
    Returneaza valoarea de adevar in urma testarii unui numar daca este prim.
    :param n: numar natural
    :return: true or false
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def get_largest_prime_below(n: int) -> int:
    """
    Returneaza cel mai mare numar prim sub o limita data
    :param n: Limita superioara data
    :return: i-Numarul prim returnat
    """
    for i in range(n-1, 0, -1):
        if is_prime(i):
            return i

def test_get_largest_prime_below():
    """Testeaza functia
    """
    assert get_largest_prime_below(30) == 29
    assert get_largest_prime_below(2498) == 2477
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(100) == 97
    assert get_largest_prime_below(50) == 47


def input_get_largest_prime_below():
    x = int(input("Functia va gasi cel mai mare numar prim mai mic decat o limita superioara. Care este limita superioara? "))
    print(f"Cel mai mare numar prim mai mic decat {x} este {get_largest_prime_below(x)}.")

def main():

    option = '?'
    while True:
        print("""
        Ce functie vrei sa foloesti?
        (1)    get_largest_prime_below
        (2)    is_palindrome
        (3)    get_n_choose_k
        (X)    exit""",sep='')
        option = input("Optiune: ")
        if option == '1':
            input_get_largest_prime_below()
        elif option == '2':
            input_is_palindrome()
        elif option == '3':
            input_get_n_choose_k()
        else:
            break

if __name__ == "__main__":
    main()