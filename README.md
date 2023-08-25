# iTunes Search

This script allows you to search for songs on iTunes using the iTunes Search API.

## Usage

1. Run the script using `python itunes_search.py`.
2. When prompted, enter the term you want to search for and the number of results you want to see.
3. The script will display the results in the console, showing the name, artist, and album for each song.

## Dependencies

This script requires the `requests` module to be installed. You can install it using `pip install requests`.

## Code Explanation

The script uses the `requests` module to send a GET request to the iTunes Search API with the specified search term and number of results. The response is then parsed and displayed in the console.

The `get_term` function prompts the user for input and sends the request to the API. The `main` function calls `get_term` and displays the results.
