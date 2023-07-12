import requests

def generate(difficulty):
    if difficulty == 0:
        url = "https://sugoku.onrender.com/board?difficulty=random"
    elif difficulty == 1:
        url = "https://sugoku.onrender.com/board?difficulty=easy"
    elif difficulty == 2:
        url = "https://sugoku.onrender.com/board?difficulty=medium"
    else:
        url = "https://sugoku.onrender.com/board?difficulty=hard"


    querystring = {"seed":"1337"}

    headers = {
        "X-RapidAPI-Key": "6e31d17babmsh77dbedc1ec2da20p14454bjsnfb162db0d4e3",
        "X-RapidAPI-Host": "sudoku-generator1.p.rapidapi.com"
    }

    response = requests.get(url)

    return response.json()["board"]
    