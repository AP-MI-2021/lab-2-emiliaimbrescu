def factorial(n: int) -> int:
    """Calculeaza si returneaza factorialul unui numar
    Args:
        n (int): Numarul al carui factorial e calculat
    Returns:
        int: Factorialul returnat
    """
    fact = 1
    for i in range(1,n+1):
        fact*=i

    return fact

def get_n_choose_k(n: int, k: int) -> int:
    """Calculeaza combinari de n luate cate k
    Args:
        n (int): Marimea multimii din care se iau elemente
        k (int): Marimea unei combinari
    Returns:
        int: [Numarul de combinari]
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

input_get_n_choose_k()