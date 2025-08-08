# 🇮🇳 Indian State Guess Quiz Game 🇮🇳

Welcome to the **Indian State Guess Quiz Game**, a fun and educational Python-based geography quiz!  
This game helps you learn the Indian states interactively by guessing their names and visualizing their locations on a blank map of India.

![Indian Map](https://i.pinimg.com/originals/0e/56/71/0e5671bb09b0eeb2c2d657e1e314b40d.jpg)

> 🖼️ **Source of Map:** [Pinterest - Indian Map Poster](https://in.pinterest.com/pin/indian-map-poster-design--17310779812543255/)

---

## 🛠 Features

✅ Blank map of India displayed using `turtle`  
✅ User inputs state names via a prompt  
✅ Correct guesses are labeled on the map at accurate coordinates  
✅ Keeps running until all states are guessed correctly  
✅ Interactive and beginner-friendly!

---

## 📂 Project Structure

```bash
indian-state-quiz/
│
├── main.py        # Main game logic
├── indian_state_list.csv # Predefined coordinates for each state
├── [Indian_map_blank_Indian_map.gif] # Map image for background
|--- state_cordinate_pair_formation.py # code to generate cordinates that reduce manual making csv file
└── README.md                   # This file

Tech Stack
Python 3
Turtle Graphics
CSV File for mapping state names to coordinates


How It Works
🎯 Map Setup
The game uses a blank outline map of India as a background image in the turtle window.

📍 Coordinates Mapping
Each Indian state is associated with a specific (x, y) coordinate on the map. These are stored in a CSV file like this:


Copy
Edit
State,X,Y
Uttar Pradesh,-20,60
Maharashtra,-70,-30
Tamil Nadu,100,-100
...
🎮 Gameplay Loop

The player is prompted to guess the name of a state.

If correct, the state name appears at its position on the map.

The game runs until all 28 states are guessed correctly.

❌ Wrong Input?

Invalid or repeated names are ignored silently.

Guess a state: Bihar
✅ Correct! Bihar appears on the map.

...

🎉 All states guessed! You win!


## Learning Sources:
  Udemy courses, turtle file Documentary on internet, geeks for geeks
