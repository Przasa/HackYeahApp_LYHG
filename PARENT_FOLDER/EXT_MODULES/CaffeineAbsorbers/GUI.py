import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random


def play_song(heartrate):
    # Set up your Spotify API credentials
    client_id = '0d8706e91fa4441dbd8b67f5380a20ee'
    client_secret = '0395e71ba6b04c79926123c70a9a6012'
    redirect_uri = 'https://open.spotify.com/?'

    # Initialize the Spotify API client
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope="user-library-read user-read-playback-state user-modify-playback-state"))

    # Prompt the user to log in (opens a browser window)
    sp.current_user()

    # Get the current user's playback device
    devices = sp.devices()
    if devices['devices']:
        device_id = devices['devices'][0]['id']  # Use the first available device
    else:
        print("No playback devices found.")
        exit(1)

    # Select playlist to play
    if heartrate == "LOW":
        # Energy BOOST
        playlist_uri = 'spotify:playlist:1XLoaJJ3OZwq6OBMHxsrL2'
    elif heartrate == "HIGH":
        # Calm Down
        playlist_uri = 'spotify:playlist:37i9dQZF1DX5bjCEbRU4SJ'
    else:
        # Happy
        playlist_uri = 'spotify:playlist:37i9dQZF1EVJSvZp5AOML2'

    sp.start_playback(device_id=device_id, context_uri=playlist_uri)


def say_something(heartrate, init=False, measure=False):
    dict_init = ['hi!',
                 'nice to see you!',
                 'how are you today?']

    dict_measure = ['Hmm, it seems that we have some data for you...',
                    'It looks like we are getting close']

    dict_high = ['Ooo, getting nervous?',
                 'Hey, maybe it\'s time for a small brake?',
                 'Maaan, chill down... Wonna smoke?',
                 'Deep breath, sir!']

    dict_normal = ['There we go, all good ;)',
                   'Nice and steady',
                   'What a beautiful day!',
                   'It\'s good to see you so well']

    dict_low = ['Getting lazy?',
                'Time for a nap?',
                'Uuu, we are getting low',
                'Mmm, COFFEE TIME!',
                'Let me play you some boost music!']

    if init:
        return random.choice(dict_init)

    if measure:
        return random.choice(dict_measure)

    if heartrate == "HIGH":
        return random.choice(dict_high)
    elif heartrate == "LOW":
        return random.choice(dict_low)
    else:
        return random.choice(dict_normal)