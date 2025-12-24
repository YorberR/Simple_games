import streamlit as st
import random

def get_winner(user, computer):
    if user == computer:
        return "Empate"
    elif (user == "Piedra" and computer == "Tijera") or \
         (user == "Papel" and computer == "Piedra") or \
         (user == "Tijera" and computer == "Papel"):
        return "Usuario"
    else:
        return "Computadora"

def init_game():
    st.session_state.rps_user_score = 0
    st.session_state.rps_computer_score = 0
    st.session_state.rps_round_result = ""
    st.session_state.rps_history = []

def app():
    st.header("✂️ Piedra, Papel o Tijeras")

    if 'rps_user_score' not in st.session_state:
        init_game()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Tus Victorias", st.session_state.rps_user_score)
    col2.metric("Victorias CPU", st.session_state.rps_computer_score)
    if col3.button("Reiniciar Marcador"):
        init_game()
        st.rerun()

    st.divider()
    
    st.subheader("Elige tu jugada:")
    bp1, bp2, bp3 = st.columns(3)
    
    user_choice = None
    if bp1.button("🪨 Piedra", use_container_width=True):
        user_choice = "Piedra"
    if bp2.button("📄 Papel", use_container_width=True):
        user_choice = "Papel"
    if bp3.button("✂️ Tijera", use_container_width=True):
        user_choice = "Tijera"

    if user_choice:
        options = ["Piedra", "Papel", "Tijera"]
        computer_choice = random.choice(options)
        
        result = get_winner(user_choice, computer_choice)
        
        msg = f"Tú: {user_choice} vs CPU: {computer_choice} -> "
        if result == "Usuario":
            st.session_state.rps_user_score += 1
            msg += "¡Ganaste! 🎉"
            st.balloons()
        elif result == "Computadora":
            st.session_state.rps_computer_score += 1
            msg += "Perdiste. 🤖"
        else:
            msg += "Empate. 🤝"
            
        st.session_state.rps_round_result = msg
        st.session_state.rps_history.insert(0, msg)

    if st.session_state.rps_round_result:
        st.success(st.session_state.rps_round_result)

    if st.session_state.rps_history:
        st.subheader("Historial")
        for h in st.session_state.rps_history[:5]:
            st.text(h)
