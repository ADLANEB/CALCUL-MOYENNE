"""
Module utils
Fonctions de calcul des statistiques des notes.
"""

def calcul_moyenne(liste_notes):
    """
    Calcule la moyenne d'une liste de notes.

    Args:
        liste_notes (list): liste de notes numériques.

    Returns:
        float: moyenne des notes.
    """
    if not liste_notes:
        return 0.0

    total = sum(liste_notes)
    return total / len(liste_notes)


def trouver_min(liste_notes):
    """
    Trouve la note minimale dans une liste.

    Args:
        liste_notes (list): liste de notes numériques.

    Returns:
        float: note minimale.
    """
    if not liste_notes:
        return 0.0

    return min(liste_notes)


def trouver_max(liste_notes):
    """
    Trouve la note maximale dans une liste.

    Args:
        liste_notes (list): liste de notes numériques.

    Returns:
        float: note maximale.
    """
    if not liste_notes:
        return 0.0

    return max(liste_notes)
