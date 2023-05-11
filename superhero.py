import requests


class SuperHero():
    
    def __init__(self):
        self.baseURL = 'https://akabab.github.io/superhero-api/api'

    def get_all_heros(self):
        request_URL = self.baseURL + "/all.json"
        response = requests.get(request_URL)
        self.heroes = response.json() if response.status_code == 200 else None
        return self.heroes
    
    def get_hero_by_name(self, name):
        for hero in self.heroes:
            if hero["name"] == name:
                return hero
    
    def get_heroes_by_name(self, names):
        result = []
        for name in names:
            hero = self.get_hero_by_name(name) 
            if hero != None:
                result.append(hero)
        return result
    
    def get_most_intelligence(self, heroes):
        data = []
        for hero in heroes:
            data.append((hero["name"] , hero["powerstats"]["intelligence"]))
        data.sort(key=lambda x: x[1], reverse=True)
        return data[0]

