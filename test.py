def factorial(n):
    """Calcule la factorielle d'un nombre de manière récursive"""
    if n == 0:
        return 1
    return n * factorial(n-1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    print("Tous les tests passent avec succès!")

if __name__ == "__main__":
    test_factorial()
