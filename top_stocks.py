import requests

def get_data():
    r = requests.get('https://wsb-pop-index.s3.amazonaws.com/wsbPopIndex.json')
    
    return r.json()["data"]
  
