import requests
import os

def get_term():
    while(True):
        try:
            term = input('What term you want to search? ')
            limit = input('How many results you want? ')
            response = requests.get(
                "https://itunes.apple.com/search?entity=song&limit="+limit+"&term="+term
                )
            results = response.json()['results']
            return results
        except ValueError:
            print(f'{term} not found!')

def main():
    os.system('cls')
    print(' \n***************************')
    results = get_term()
    for c in results:
        print(f'Name: {c["trackName"]}\nArtist: {c["artistName"]}\nAlbum: {c["collectionName"]}\n ')
    print(' \n***************************')

main()
 