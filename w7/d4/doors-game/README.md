# React: Doors Game

### **Note that this project was created with `create-react-app` so the file extensions are going to be `.js` instead of `.jsx`. We have changed the scripts in `package.json` so you can still use the command `npm run dev` to start the dev server

We've coded up a simple 'Choose a door' game using React. To play the game, a player must select a random door, and they win the game if they correctly choose the door that has a prize behind it (otherwise they lose).


## Step 1
Your first challenge is to install this React project (running `npm install`) and to fully understand the code that has been provided. You do not need to change anything right now within the project... just take time to go through the code, play the game, and understand how things are connected and working in this React app. Do you understand how all of the functionality in implemented here?

## Main Challenge
There is one piece of functionality that we've not implemented that would be nice to have. 
Notice that you are able to still open the other doors, even after you make your first door guess. 
The result of the game remains the same (based on the first door that you opened), but it would be better if we prevented any of the other doors from being opened after the first guess is made. Can you figure out how to implement this desired functionality?

## Stretch Challenge
 The code is written using functional components. Your task is to convert the following components into a class-based component design:
- src/App.js
- src/components/Game.js
- src/components/Door.js

Once you convert these components, verify that all of the previous functionality of the game remains in tact! Nothing should have changed from the user's perspective.

