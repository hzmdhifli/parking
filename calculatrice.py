def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erreur: Division par zéro"

def calcul_factorielle(n):
    """Utilise la fonction factorielle existante de test.py"""
    from test import factorial
    return factorial(n)

def afficher_menu():
    print("\nCalculatrice Simple")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorielle")
    print("6. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une opération (1-6): ")
        
        if choix == '6':
            print("Au revoir!")
            break
            
        if choix not in ('1', '2', '3', '4', '5'):
            print("Choix invalide, veuillez réessayer.")
            continue
            
        if choix == '5':
            nombre = int(input("Entrez un nombre entier: "))
            resultat = calcul_factorielle(nombre)
            print(f"Factorielle de {nombre} = {resultat}")
            continue
            
        a = float(input("Entrez le premier nombre: "))
        b = float(input("Entrez le deuxième nombre: "))
        
        operations = {
            '1': addition,
            '2': soustraction,
            '3': multiplication,
            '4': division
        }
        
        resultat = operations[choix](a, b)
        print(f"Résultat = {resultat}")

if __name__ == "__main__":
    main()
