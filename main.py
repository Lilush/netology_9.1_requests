from pprint import pprint

from superhero import SuperHero

hero_names = ["Hulk", "Captain America", "Thanos"]

if __name__ == "__main__":
    sh = SuperHero()
    sh.get_all_heros()
    heroes = sh.get_heroes_by_name(hero_names)
    most_intelligence_hero = sh.get_most_intelligence(heroes)
    print(most_intelligence_hero)

