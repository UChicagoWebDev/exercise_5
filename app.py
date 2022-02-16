import string
import random
from datetime import datetime
from flask import Flask, render_template, request
from functools import wraps

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# You can store data on your server in whatever structure is most convenient,
# either holding it in memory on your server or in a sqlite database.
# You may use the sample structures below or create your own.

# users is a collection of authorized users with their usernames API requests
# include an auth_key, so we want that to be the key on our dictionary so we can
# efficiently get the username from an auth_key, and so that multiple users with
# their own auth_keys can have the same display name.
# { auth_key: username }
# example: {1435275768: "Alice", 5769853333: "Bob"}
users = {}

# chats is a collection that contains the chats, keyed by their chat_id, where
# each chat object contains a collection of the users that are authorized to use
# it (identified by their auth_key), and a list of current chat messasges.
# example: chats = {
#     0: {
#         "magic_passphrase": "0123456789",
#         "authorized_users": {8959659785, 1435275768, 5769853333, ... auth_keyN},
#         "messages": [
#               {"user": 1435275768, "text": "hi"}
#               {"user": 5769853333, "text": "hello"}
#               {"user": 1435275768, "text": "knock knock"}
#               {"user": 5769853333, "text": "whos there"}
#          ]
#     },
#     1: ...
# }
chats = {}

def newChat(host_auth_key):
    magic_passphrase = ''.join(random.choices(string.ascii_lowercase + string.digits, k=40))

    return dict([
        ("authorized_users", set(host_auth_key)),
        ("magic_key", magic_key),
        ("messages", [])
    ])


@app.route('/')
def index(chat_id=None):
    return app.send_static_file('index.html')

@app.route('/username')
def auth():
    return app.send_static_file('username.html')

@app.route('/chat/<int:chat_id>')
def chat(chat_id):
    return render_template('chat.html',
            chat_id=chat_id)

# -------------------------------- API ROUTES ----------------------------------

# TODO: Create the API
