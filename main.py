import requests 
#library to fetch

# FUNCTION TO FETCH DATA 
def getRickandMortyData(character):
    
    url = f"https://rickandmortyapi.com/api/character/{character.lower()}"
    
    response = requests.get(url)
    
    
    if response.status_code == 200: 
        data = response.json()
        return data
    
    else: 
        return None 
    
    