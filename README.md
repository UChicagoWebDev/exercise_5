# Exercise #5: Watch Party

5 points

**DUE: Friday, February 18 by 5:30pm**

### Instructions

For this exercise, we will build a group chat web application with asynchronous
Javascript and a REST API written in Python with Flask.

Watch Party lets users start new private chats that work like group texts or
Slack rooms. A user creates a new chat, which is assigned a unique identifier.
They can invite other users by sharing a unique link that will authenticate the
bearer to the chat. Users in a chat post messages which appear in a single
conversation thread to all users. Unlike Slack or a group chat, Watch Party only
saves or shows the last 30 messages. If you optionally want to further limit the
number of participants in a room or the amount of time that messages last, you
may do so. (This was part of an earlier version of the assignment).

Take Watch Party UI here and serve it
using server-side code written in the [latest stable version of Python](https://www.python.org/downloads/release/python-3102/)
([3.10.2](https://www.python.org/downloads/release/python-3102/))
and [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/).

The user experience should be:
- From index.html, the user can click the button to create a new chat. This will
  send an API request to one of the endpoints described below.
  - If the request was sent with a valid auth_key, the room is created. Redirect
    them to the newly-created room. (hint: use
    [window.location](https://developer.mozilla.org/en-US/docs/Web/API/Window/location))
  - If the request was not sent with a valid auth_key, redirect the user to
    `username.html`
- From chat/<chat_id>:
  - If the user has a valid auth_key for this chat, show them the messages and
    the magic link.
  - If the user does not have a valid auth key but came via a magic link with
    the correct magic passphrase, redirect them to `username.html`. Be sure to
    remember the chat id and the magic passphrase.
  - If the user does not have a valid auth_key and did not come via the correct
    magic link, redirect them to `index.html` Be sure not to show them the
    messages or the magic link before they go!
- From `username.html`, the user can enter a username. The server creates, saves,
  and returns a new auth_key for that user.
  - If the user was redirected here from a magic link, return the user to that
    magic link so that they can enter the chat.
  - Otherwise, redirect them to `index.html`

Be sure to
include important features like:
- Give each chat a unique URL
- As other users type new messages in a chat, Watch Party should asynchronously
  fetch them, and those messages should appear automatically without anyone
  reloading the page.
- Allow users to be in multiple chats in multiple tabs with the same username
  (hint: have your front-end code store its auth key in
  [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)).
- Redirect users to the home screen if they try to join a chat without the right
  invite link. Chats are private!
- Make sure chat messages support Unicode characters

You may save chat messages and user names on the server however you want; with a
database like we used in Exercise 3 or just in memory on your server. Either
way, make sure you delete older messages as ones over 30 come in. For the
purposes of this Exercise, you also do not need to worry about deleting chats
that nobody is using anymore.

To support the above behavior, write a REST API for creating and hosting live
Watch Party group chats, also using Python and Flask. It should support the
following methods:
- `POST /create`: Allow any user to create a new chat with a new secret invite
  link. Return a unique identifier `chat_id` to the creator.
- `GET /<chat_id>`: Require a valid `auth_key` in an authorization header.
  Return the messages in the chat. Optionally take a parameter that allows it to
  return only new messages.
- `POST /<chat_id>`: Require a valid `auth_key` in an authorization header.
  Post a new message to the chat.

Your web application should use these API methods. Feel free to include any
other methods you think will be useful, either as web controllers or as further
API endpoints. You can use any other libraries or frameworks you find useful, as
well.

Remember to include in your submission any classmates you collaborated with and
any materials you consulted. Watch Party (though it has somewhat different
requirements) is inspired by [yap.chat](https://yap.chat/).

### Rubric
- Users can enter a username at `username.html` and receive an auth_key to
  include with future requests. [1 pt]
- JSON API:
  - REST endpoint to create a new chat that requires a valid auth_key[1 pt]
  - REST endpoint to post messages to a chat that requires a valid auth_key[1 pt]
  - REST endpoint to post messages to a chat that requires a valid auth_key [1 pt]
- Sign up with Magic Links: Generate URLs that contain a chat id and a unique
  passphrase, such that visiting that URL lets the user join the chat. [1 pt]
- Chats are private! Users that didn't create a chat or follow a magic link to
  join it can't see its messages or its magic link, even with their developer
  tools. [1 pt]
- Remember permissions: When a user with an auth key creates a chat or enter one
  with a magic link, save on the server that they have permission to use that
  chat room. [1 pt]
- Posting: Users can post messages without reloading the page. [1 pt]
- Polling for messages: The UI continuously checks for new messages and displays
  them as they are posted to the server. It sends a request for new messages as
  soon as the last request is processed, but not before. [1 pt]
- Advanced UI Handling: Allow users to be in multiple chats in multiple tabs or
  windows. Support usernames and messages that contain unicode characters. [1 pt]
