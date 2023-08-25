import requests
import os

def get_term():
    while(True):
        try:
            term = input('What term you want to search? ')
            limit = input('How many results you want? ')
            results = requests.get(
                "https://itunes.apple.com/search?entity=song&limit="+limit+"&term="+term
                ).json()['results']
#            results = response.json()['results']
            return results
        except ValueError:
            print(f'{term} not found!')

def main():
    results = get_term()
    os.system('cls')
    print(' \n***************************\n')
    for c in results:
        print(f'Name: {c["trackName"]}\nArtist: {c["artistName"]}\nAlbum: {c["collectionName"]}\n')
    print('***************************')

main()
 
