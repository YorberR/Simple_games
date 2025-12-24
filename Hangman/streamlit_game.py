import streamlit as st
import random
import os

def read_words_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            words = [line.strip().upper() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        return ["PYTHON", "STREAMLIT", "DEVELOPER", "AHORCADO"] # Fallback

def get_hangman_art(attempts_left):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    # stages usually go from max attempts to 0. Let's map attempts_left (0-6) to index.
    # 6 attempts -> empty gallow (index 6, if we reverse or just write custom)
    # Let's map directly:
    mapping = {
        6: """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
        5: """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        4: """
           --------
           |      |
           |      O
           |      |
           |      
           |     
           -
        """,
        3: """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
           -
        """,
        2: """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
           -
        """,
        1: """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     
           -
        """,
        0: """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / \\
           -
        """
    }
    return mapping.get(attempts_left, "")

def init_game():
    filepath = os.path.join("Hangman", "DATA", "DATA.txt")
    words = read_words_from_file(filepath)
    st.session_state.hangman_word = random.choice(words)
    st.session_state.hangman_guessed = set()
    st.session_state.hangman_attempts = 6
    st.session_state.hangman_game_over = False
    st.session_state.hangman_result = ""

def app():
    st.header("🔤 Ahorcado")

    if 'hangman_word' not in st.session_state:
        init_game()

    if st.button("Juego Nuevo"):
        init_game()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.text(get_hangman_art(st.session_state.hangman_attempts))
        st.write(f"Intentos restantes: {st.session_state.hangman_attempts}")

    with col2:
        # Display word with underscores
        display_word = []
        won = True
        for char in st.session_state.hangman_word:
            if char in st.session_state.hangman_guessed:
                display_word.append(char)
            else:
                display_word.append("_")
                won = False
        
        st.markdown(f"## {' '.join(display_word)}")

        if won and not st.session_state.hangman_game_over:
            st.session_state.hangman_result = "¡Felicidades! Ganaste."
            st.session_state.hangman_game_over = True
        
        if st.session_state.hangman_attempts <= 0 and not st.session_state.hangman_game_over:
            st.session_state.hangman_result = f"Perdiste. La palabra era: {st.session_state.hangman_word}"
            st.session_state.hangman_game_over = True

        if st.session_state.hangman_game_over:
            if "Ganaste" in st.session_state.hangman_result:
                st.success(st.session_state.hangman_result)
            else:
                st.error(st.session_state.hangman_result)
        
        # Keyboard input
        if not st.session_state.hangman_game_over:
            st.write("Elige una letra:")
            alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            # Create a grid of buttons
            cols = st.columns(7)
            for i, letter in enumerate(alphabet):
                if letter not in st.session_state.hangman_guessed:
                    if cols[i % 7].button(letter, key=f"btn_{letter}"):
                        st.session_state.hangman_guessed.add(letter)
                        if letter not in st.session_state.hangman_word:
                            st.session_state.hangman_attempts -= 1
                        st.rerun()
                else:
                    cols[i % 7].button(" ", disabled=True, key=f"btn_{letter}_dis")

