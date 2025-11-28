# Ideas for features and how the project should work

Endpoints:
- GET /flashcard/{subject}/{topic}/{card}
    - returns the specified card for the topic and subject
- GET /flashcard/{subject}/{topic}/list
    - list all the flashcards in a topic
- GET /flashcard/{subject}/{topic}/random
    - returns a random flashcard from a specified topic
- In future I hope to also add POST endpoints to allow the API to add new flashcards

Storage:
- The API should store and fetch flashcards from a MongoDB database

User Interface:
- Long term, there should be an app that will use the API to allow users to create/modify/delete flashcards
- This will involve adding user authentication, and making a web app (most likely in a seperate repo)

