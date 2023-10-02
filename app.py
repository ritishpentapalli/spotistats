from flask import Flask, render_template, redirect, request
import webbrowser
from dotenv import load_dotenv
import os

load_dotenv('.env')
CLIENT_ID: str = os.getenv('CLIENT_ID')
PORT_NUMBER = 3000

def get_access_token(): # Link for user to login to Spotify -> gives Access Token upon successful login
    client_id = CLIENT_ID
    redirect_uri = 'https://www.google.com/'
    scope = 'user-top-read'
    url = 'https://accounts.spotify.com/authorize'
    url += '?response_type=token'
    url += '&client_id=' + client_id
    url += '&scope=' + scope
    url += '&redirect_uri=' + redirect_uri
    return url 

app = Flask(__name__) 

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/spotify-login', methods = ['POST'])
def redirect_to_spotify_login():
    webbrowser.open_new_tab(get_access_token()) # Opens new tab with return URI along with Access Token in browser address bar
    return render_template('enter-access-token.html')

@app.route('/access-token', methods = ['POST'])
def access_token():
    user_access_token = request.form.get("access-token") 
    with open("user_access_token.txt", "w") as file: # Writes Access Token into file # Find a better way to do this?
        file.write(user_access_token)
    
    return ('',204) # Need to return new tab with results of statistical_analysis 

if __name__ == "__main__":
    app.run(debug = True, port = PORT_NUMBER)

########## Issues ##########

# Need to add favicon

###########################