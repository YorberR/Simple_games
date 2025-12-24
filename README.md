# Simple Games (Streamlit Edition)

This repository contains three simple games adapted for the web using **Streamlit**:

1.  **Blackjack** 🃏
2.  **Hangman** 🔤
3.  **Rock, Paper, Scissors** ✂️

## Installation

First, make sure you have Python 3.x installed on your system. Then, install the necessary dependencies using pip and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## How to Run

To start the main menu and play the games, run the `streamlit_app.py` file:

```bash
streamlit run streamlit_app.py
```

This will open a tab in your web browser where you can interact with the application.

## Included Games

### Blackjack
A classic Blackjack game where you play against a computer-controlled dealer. Try to get closer to 21 than the dealer without going over!

### Hangman
A Hangman game where you must guess the word before running out of attempts. Uses a built-in word list.

### Rock, Paper, Scissors
A quick Rock, Paper, Scissors game where you play against the computer. Tracks your wins and losses in the current session.

## Deployment

This app is ready to be deployed on **Streamlit Cloud**:
1.  Push this repository to GitHub.
2.  Log in to [share.streamlit.io](https://share.streamlit.io/).
3.  Deploy the app by selecting your repository and point to `streamlit_app.py` as the main file.

## License
This project is licensed under the MIT License.