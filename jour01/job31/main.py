def aroundList(listNote):
    numberNote = len(listNote)
    x = 0
    while x < numberNote:
        if listNote[x] < 40:
            # possiblement mettre un message d'erreur, d'échouage
            listNote[x] = listNote[x]
        else:
            if listNote[x] % 5 < 3:
                # possiblement mettre un message d'erreur, d'échouage
                listNote[x] = listNote[x]
            else:
                reste = 100 - listNote[x]
                ajout = reste % 5
                listNote[x] = listNote[x] + ajout
        
        x += 1

    return listNote   


print(aroundList([44, 26, 23, 83, 30, 2, 78]))