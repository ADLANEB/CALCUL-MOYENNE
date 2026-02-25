"""
Programme principal StudentStats
"""

from utils import calcul_moyenne, trouver_min, trouver_max


def main():
    """
    Point d'entrée du programme.
    """
    notes = [12, 15, 9, 18, 14]

    moyenne = calcul_moyenne(notes)
    minimum = trouver_min(notes)
    maximum = trouver_max(notes)

    print("Notes :", notes)
    print("Moyenne :", moyenne)
    print("Minimum :", minimum)
    print("Maximum :", maximum)


if __name__ == "__main__":
    main()
