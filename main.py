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

def json_data(data):
    '''Writing/Updating the json file'''

    with open('Results/data.json','w') as f:
        f.write(json.dumps(data,indent=2))

    # Displaying Some Results In Terminal 

    with open('Results/data.json','r') as f:
        py_data = json.load(f)
        # pprint(py_data)

        print('Meme Results 😄')
        print(f'Title --> {py_data["title"]}')
        print(f"Meme-link --> {py_data['url']}")

if __name__ == "__main__":

    req = Basic_setup(url=END_POINT)
    json_data(data=req.json())

    print('Code Completed 🔥')