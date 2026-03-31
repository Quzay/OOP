from flask import Flask, render_template
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

ANIME_ID = 11757

@app.route('/')
def home():
    anime_info = jikan.anime(ANIME_ID)
    episodes_info = jikan.anime(ANIME_ID, extension='episodes')
    
    return render_template('index.html', 
                           anime=anime_info['data'], 
                           episodes=episodes_info['data'])

if __name__ == '__main__':
    app.run(debug=True)