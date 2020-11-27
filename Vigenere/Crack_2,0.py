# Lecture du fichier crypté
#--------------------------
def lireTexte(nomFichier) :
    try:
        fichier = open(nomFichier, 'r')
    except IOError:
        print (nomFichier + " : ce fichier n'existe pas")
    return None
    texte = ''
    while True:
        ligne = fichier.readline()
        if ligne == '':
         break
    for mot in ligne.split():
        texte = texte + mot
    fichier.close()
    return texte
# On va travailler avec l'alphabet : ALPHABET
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Calcul de l'indice de coincidence
#----------------------------------
def IC(texte) :
    occ = { }
    n = len(texte)
    for car in texte:
     if car in occ:
        occ[car] = occ[car] + 1
    else:
         occ[car] = 1
         ic = 0.0
    for car in occ.keys(): ic += occ[car]*(occ[car] - 1)/n/(n-1)
    return ic
def decal(car, d) :
    return chr((ord(car) - ord('A') + d) % 26 + ord('A'))
def convertCarCode(car) :
    return ord(car) - ord('A')
# Construction d'un texte avec un alphabet décalé de d
#-----------------------------------------------------
def cesar(texte, d) :
    texteDecale = ''
    for car in texte : texteDecale = texteDecale + decal(car, d)
    return texteDecale
# Calcul de la longueur de la cle
#--------------------------------
def longueurCle(texte) :
    distances = []
    n = len(texte)
    for lgSC in range(4, 10) :
        for i in range(0, n - lgSC) :
             sc = texte[i : i + lgSC]
             j = texte[i+1 :].find(sc) + 1
             if j > 0 : distances.append(j)
    # Maintenant que l'on a le tableau des distances, on va boucler sur la longueur de la clé
    # On va s'intéresser a la longueur qui donne le meilleur score
    # mais cela n'est pas sur surtout quand la longueur de la clé a des petits diviseurs
    nbMax = 0
    for lg in range(5,20) :
        nb = 0
        for d in distances :
            if d % lg == 0 : nb = nb + 1
            if nb >= nbMax :
                nbMax = nb
                lgCle = lg
    return lgCle

# Recherche de la cle
#--------------------
def rechercheCle(texte, lgCle) :
# 1 - on va découper le texte en lgCle morceaux
# on profite d'une fonction de python sur les sequences
    texte0 = texte[0:len(texte):lgCle]
    decalages = [0]
    for k in range(1, lgCle) :
        IcMax = 0
        decalage = -1
        textek = texte[k:len(texte):lgCle]
        for d in range(0,26) :
            Ic = IC(texte0 + cesar(textek, d))
            if Ic > IcMax :
                IcMax = Ic
                decalage = d
        decalages.append(decalage)
    # 2 - maintenant on va reprendre le texte et appliquer tous les décalages
    # et chercher la lettre la plus fréquente
    occ = { }
    for i in range(0, len(texte)) :
        car = cesar(texte[i], decalages[i % lgCle])
        if car in occ:
            occ[car] = occ[car] + 1
        else:
            occ[car] = 1
    max = 0;
    for car in occ.keys():
        if occ[car] > max :
            max = occ[car];
            carE = car;
    delta = (26 + ord(carE) - ord('E') ) % 26
    # 3 - maintenant on connait la cle
    cle = ''
    for d in decalages :
        cle = cle + ALPHABET[(delta - d) % 26]
    return cle
# On decrypte Vigenere avec la cle
#---------------------------------
def decrypte(texte, cle) :
    lgCle = len(cle)
    clair = ''
    for i in range(0, len(texte)) :
        code = (convertCarCode(texte[i]) - convertCarCode(cle[i % lgCle])) % 26
        clair = clair + ALPHABET[code]
    return clair
# Debut du programme de cryptanalyse de Vigenere
#-----------------------------------------------
def casse(texte) :
    lgCle = longueurCle(texte)
    print("Longueur de la clé = ",lgCle)
    cle = rechercheCle(texte, lgCle)
    print("Cle = ", cle)
    clair = decrypte(texte, cle)
    print(clair)


with open('/home/altidor/Documents/Projects/Security_Lab-main/Vigenere/code.txt', 'r') as file:
        texte = file.read()
casse(texte)
