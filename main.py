import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def pig_latinize(payload):
    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    input_data = {
        "input_text": payload
    }

    response = requests.post(url, data=input_data, allow_redirects=False)
    url_location = response.headers['Location']

    return url_location


@app.route('/', methods=['GET', 'POST'])
def home():
    random_quote = get_fact()
    url = pig_latinize(random_quote)
    return url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
