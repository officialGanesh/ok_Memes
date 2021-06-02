# Import the required modules
import requests, csv, json
from pprint import pprint

END_POINT = 'https://meme-api.herokuapp.com/gimme'

def Basic_setup(url):
    '''Basic Requirements Setup'''

    try:
        r = requests.get(END_POINT)
        r.raise_for_status
    except Exception as e:
        print('Something Went Wrong',e)

    return r



if __name__ == "__main__":

    req = Basic_setup(url=END_POINT)
    print('Code Completed 🔥')