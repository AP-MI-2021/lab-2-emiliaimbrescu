def is_palindrome(n : int) -> bool:
    """Verifica daca numarul dat este un palindrom
    Args:
        n (int): Numarul care este verificat
    Returns:
        bool: Daca este sau nu palindrom
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

input_is_palindrome()