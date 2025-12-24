import streamlit as st
from blackjack import streamlit_game as blackjack
from Hangman import streamlit_game as hangman
from Rock_paper_or_scissors import streamlit_game as rps

def main():
    st.set_page_config(page_title="Menú de Juegos", page_icon="🎮")

    st.title("🎮 Menú de Juegos")
    st.write("Selecciona un juego del menú lateral para comenzar a jugar.")

    # Sidebar menu
    game_choice = st.sidebar.selectbox(
        "Elige un juego",
        ("Inicio", "Blackjack", "Ahorcado", "Piedra, Papel o Tijeras")
    )

    if game_choice == "Inicio":
        st.header("Bienvenido a la colección de Juegos Simples")
        st.markdown("""
        Esta aplicación contiene tres juegos clásicos:
        
        1.  **Blackjack 🃏**: Intenta llegar a 21 sin pasarte.
        2.  **Ahorcado 🔤**: Adivina la palabra antes de que se acaben los intentos.
        3.  **Piedra, Papel o Tijeras ✂️**: Juega contra la computadora.
        
        ¡Selecciona uno en la barra lateral para empezar!
        """)
    elif game_choice == "Blackjack":
        blackjack.app()
    elif game_choice == "Ahorcado":
        hangman.app()
    elif game_choice == "Piedra, Papel o Tijeras":
        rps.app()

if __name__ == "__main__":
    main()
