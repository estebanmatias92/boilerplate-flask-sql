import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import *

# Connect to Spotify API (and your user account) and returns ths session
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE))

# Prepares the Desktop App
class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.textbox = tk.Text(frame)
        self.textbox.pack()

        self.hello_button = tk.Button(frame, text='HELLO', command=self.say_hello)
        self.hello_button.pack(side=tk.LEFT)

        self.show_tracks_button = tk.Button(frame, text='SHOW TRACKS', command=self.show_favorite_tracks)
        self.show_tracks_button.pack(side=tk.LEFT)

    def say_hello(self):
        self.textbox.insert(tk.END, 'Hello, World!\n')

    def show_favorite_tracks(self):
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            self.textbox.insert(tk.END, track['name'] + ' - ' + track['artists'][0]['name'] + '\n')


# Entrypoint
root = tk.Tk()
app = App(root)
root.mainloop()
