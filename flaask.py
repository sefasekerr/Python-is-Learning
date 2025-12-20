# save this as app.py
from flask import Flask
import pandas as pd



from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route("/")
def hello():
    a = pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                        'Sounds':['Barks','Meow','Roars','Moo','Trumpet']})

    print(a)
    print(a.describe())

    b = pd.DataFrame({
        "Letters" : ['a', 'b', 'c', 'd', 'e', 'f'],
        "Numbers" : [12, 7, 9, 3, 5, 1]  })

    print(b.sort_values(by="Numbers"))

    b = b.assign(new_values = b['Numbers']*3)
    print(b)
    return "Hello, World!"



    

if __name__ == "__main__":
    app.run()
