# je sais que c'est psyduck (alias psykokwak) se trouvant à la ligne 15715 !! A bientot

import json
import re

f = open('data.txt', 'r')
m = f.read()
f.close()

with open("pokemon.json", "r") as read_file:

    data = json.load(read_file)

    for pokemons in data["results"]:

        name = pokemons["name"]

        test = re.search(name, m)

        if test != None:
            print(name)


read_file.close()