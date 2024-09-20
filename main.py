#### Fonction secondaire

"""
main.py : Script principal pour vérifier si une chaîne de caractère est un palindrome ou non
"""

def remove_accents(s):
    """
    Retourne 's' en supprimant les accents sur les caractères qui en possèdent

    Args:
        s: chaîne de caractère

    Returns:
        's' sans accents
    """
    accents = "ÀÁÂÃÄÅàáâãäåÈÉÊËèéêëÌÍÎÏìíîïÒÓÔÕÖØòóôõöøÙÚÛÜùúûüÝýÿÇç"
    no_accents = "AAAAAAaaaaaaEEEEeeeeIIIIiiiiOOOOOOooooooUUUUuuuuYyyCc"
    # Créer une table de traduction pour les accents
    translation_table = str.maketrans(accents, no_accents)
    # Appliquer la table de traduction pour retirer les accents
    return s.translate(translation_table)

def ispalindrome(p):
    """
    Retourne True si 'p' est un palindrome et False sinon.

    Args:
        p: chaîne de caractère

    Returns:
        True or False
    """
    # votre code ici

    # Enlever les accents
    p = remove_accents(p)
    # Enlever les espaces et mettre en minuscules
    p = ''.join(c.lower() for c in p if c.isalnum())
    if p== p[::-1]:
        return True
    return False

#### Fonction principale


def main():
    """
    Créer des appels de la fonction ispalindrome(p)
    """
    # vos appels à la fonction secondaire ici
    print(ispalindrome("hannah"))
    print(ispalindrome("annah"))
    print(ispalindrome("xpohopx"))
    print(ispalindrome("Ésope reste ici et se repose"))
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
