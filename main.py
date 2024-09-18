import requests 
#library to fetch

# FUNCTION TO FETCH DATA 
def getRickandMortyData(character_name):
    
    url = f"https://rickandmortyapi.com/api/character/?name={character_name.lower()}"
    response = requests.get(url)
    
    
    if response.status_code == 200: 
        data = response.json()
        if data['results']:  # Check if any results are returned
            return data['results'][0]  # Return the first matching result
        else:
            return None
    
    else: 
        return None 
    
    
def getCharacterData(character_name):
    data = getRickandMortyData(character_name)
    
    if data:
        
        print(f"Name: {data['name']}")
        print(f"Status: {data['status']}")
        print(f"Species: {data['species']}")
        print(f"Gender: {data['gender']}")
        
    else: 
        
        print(f"Character '{character_name}' not found.")

def main():
    
    search = input("\nEnter Character Name: ")
    
    getCharacterData(search)   

if __name__ == "__main__":
    
    while True:
        main()
    
    

    