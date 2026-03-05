from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class pokemon(BaseModel):
    id:int
    name:str
    type:str
    life:int
    atack:int

p1 = pokemon(id=1, name="Gengar", type="Ghost/Poison", life=60, atack=65)
p2 = pokemon(id=2, name="Charmander", type="Fire", life=39, atack=52)
p3 = pokemon(id=3, name="Bulbasaur", type="Grass/Poison", life=45, atack=49)
p4 = pokemon(id=4, name="Squirtle", type="Water", life=44, atack=48)
p5 = pokemon(id=5, name="Pikachu", type="Electric", life=35, atack=55)
p6 = pokemon(id=6, name="Charizard", type="Fire/Flying", life=78, atack=84)
p7 = pokemon(id=7, name="Blastoise", type="Water", life=79, atack=83)
p8 = pokemon(id=8, name="Venusaur", type="Grass/Poison", life=80, atack=82)
p9 = pokemon(id=9, name="Jigglypuff", type="Normal/Fairy", life=115, atack=45)
p10 = pokemon(id=10, name="Meowth", type="Normal", life=40, atack=45)
p11 = pokemon(id=11, name="Psyduck", type="Water", life=50, atack=52)
p12 = pokemon(id=12, name="Machop", type="Fighting", life=70, atack=80)
p13 = pokemon(id=13, name="Geodude", type="Rock/Ground", life=40, atack=80)
p14 = pokemon(id=14, name="Onix", type="Rock/Ground", life=35, atack=45)
p15 = pokemon(id=15, name="Cubone", type="Ground", life=50, atack=50)
p16 = pokemon(id=16, name="Koffing", type="Poison", life=40, atack=65)
p17 = pokemon(id=17, name="Rhyhorn", type="Ground/Rock", life=80, atack=85)
p18 = pokemon(id=18, name="Horsea", type="Water", life=30, atack=40)
p19 = pokemon(id=19, name="Staryu", type="Water", life=30, atack=45)
p20 = pokemon(id=20, name="Magikarp", type="Water", life=20, atack=10)
p21 = pokemon(id=21, name="Gyarados", type="Water/Flying", life=95, atack=125)
p22 = pokemon(id=22, name="Lapras", type="Water/Ice", life=130, atack=85)
p23 = pokemon(id=23, name="Ditto", type="Normal", life=48, atack=48)
p24 = pokemon(id=24, name="Eevee", type="Normal", life=55, atack=55)
p25 = pokemon(id=25, name="Vaporeon", type="Water", life=130, atack=65)
p26 = pokemon(id=26, name="Jolteon", type="Electric", life=65, atack=65)
p27 = pokemon(id=27, name="Flareon", type="Fire", life=65, atack=130)
p28 = pokemon(id=28, name="Snorlax", type="Normal", life=160, atack=110)
p29 = pokemon(id=29, name="Dratini", type="Dragon", life=41, atack=64)
p30 = pokemon(id=30, name="Dragonair", type="Dragon", life=61, atack=84)
p31 = pokemon(id=31, name="Dragonite", type="Dragon/Flying", life=91, atack=134)
p32 = pokemon(id=32, name="Mewtwo", type="Psychic", life=106, atack=110)
p33 = pokemon(id=33, name="Mew", type="Psychic", life=100, atack=100)
p34 = pokemon(id=34, name="Chikorita", type="Grass", life=45, atack=49)
p35 = pokemon(id=35, name="Cyndaquil", type="Fire", life=39, atack=52)
p36 = pokemon(id=36, name="Totodile", type="Water", life=50, atack=65)
p37 = pokemon(id=37, name="Mareep", type="Electric", life=55, atack=40)
p38 = pokemon(id=38, name="Sudowoodo", type="Rock", life=70, atack=100)
p39 = pokemon(id=39, name="Hoppip", type="Grass/Flying", life=35, atack=35)
p40 = pokemon(id=40, name="Aipom", type="Normal", life=55, atack=70)
p41 = pokemon(id=41, name="Wooper", type="Water/Ground", life=55, atack=45)
p42 = pokemon(id=42, name="Espeon", type="Psychic", life=65, atack=65)
p43 = pokemon(id=43, name="Umbreon", type="Dark", life=95, atack=65)
p44 = pokemon(id=44, name="Slowking", type="Water/Psychic", life=95, atack=75)
p45 = pokemon(id=45, name="Misdreavus", type="Ghost", life=60, atack=60)
p46 = pokemon(id=46, name="Wobbuffet", type="Psychic", life=190, atack=33)
p47 = pokemon(id=47, name="Girafarig", type="Normal/Psychic", life=70, atack=80)
p48 = pokemon(id=48, name="Pineco", type="Bug", life=50, atack=65)
p49 = pokemon(id=49, name="Steelix", type="Steel/Ground", life=75, atack=85)
p50 = pokemon(id=50, name="Scizor", type="Bug/Steel", life=70, atack=130)
pokemons=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,
        p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,
        p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,
        p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,
        p41,p42,p43,p44,p45,p46,p47,p48,p49,p50]

@app.get("/showallpokemons")
def show_all_pokemons():
    return pokemons

@app.get("/showonepokemon/{name}")
def show_one_pokemon(name:str):
    for pok in pokemons:
        if pok.name.lower()==name.lower():
            return pok

@app.get("/showpokemonbyId/{id}")
def show_pokemon_byID(id:int):
    for pok in pokemons:
        if pok.id==id:
            return pok

@app.get("/pokemonbattle/{pokemon1}/{pokemon2}")
def battle(pokemon1:str,pokemon2:str):
    print("Win the pokemon whit more life, in case of draw win the stronger pokemon")

    pok1=pokemon()
    pok2=pokemon()
    for pok in pokemons:
        if pok.name.lower()==pokemon1.lower():
            pok1=pok
        elif pok.name.lower()==pokemon2.lower():
            pok2=pok
    show_pokemon_byID(pok1.id)
    print("\nVS\n")
    show_pokemon_byID(pok2.id)
    if pok1.life>pok2.life:
        return f"Ganador: {pok1.name}"
    elif pok2.life>pok1.life:
        return f"Ganador: {pok2.name}"
    elif pok1.atack>pok2.atack:
        return f"Ganador: {pok1.name}"
    elif pok2.atack>pok1.atack:
        return f"Ganador: {pok2.name}"
    return "Draw"
@app.get("/pokemonorderedby")
def orderedby():
    return new_pokemon