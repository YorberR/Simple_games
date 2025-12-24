import streamlit as st
import random

def deck_of_cards():
    DoC = []
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["♣", "♠", "♥", "♦"]
    for suit in suits:
        for number in numbers:
            card = f"{number}{suit}"
            DoC.append(card)
    return DoC

def card_value(card):
    if card[:-1] in ['K', 'Q', 'J', '10']:
        return 10
    elif card[0] == 'A':
        return 11
    else:
        return int(card[:-1])

def hand_value(hand):
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def init_game():
    st.session_state.deck = deck_of_cards()
    st.session_state.player_hand = []
    st.session_state.dealer_hand = []
    
    # Initial deal
    for _ in range(2):
        card = random.choice(st.session_state.deck)
        st.session_state.deck.remove(card)
        st.session_state.player_hand.append(card)
        
        card = random.choice(st.session_state.deck)
        st.session_state.deck.remove(card)
        st.session_state.dealer_hand.append(card)
    
    st.session_state.game_over = False
    st.session_state.result_message = ""

def app():
    st.header("🃏 Blackjack")

    if 'deck' not in st.session_state or 'player_hand' not in st.session_state:
        init_game()

    # New Game Button
    if st.button("Juego Nuevo"):
        init_game()

    # Display hands
    player_score = hand_value(st.session_state.player_hand)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Tu Mano")
        st.write(f"Cartas: {', '.join(st.session_state.player_hand)}")
        st.write(f"Puntaje: {player_score}")

    with col2:
        st.subheader("Mano del Crupier")
        if st.session_state.game_over:
            dealer_score = hand_value(st.session_state.dealer_hand)
            st.write(f"Cartas: {', '.join(st.session_state.dealer_hand)}")
            st.write(f"Puntaje: {dealer_score}")
        else:
            st.write(f"Cartas: {st.session_state.dealer_hand[0]}, 🂠")
            st.write("Puntaje: ?")

    # Game Logic
    if not st.session_state.game_over:
        col_actions = st.columns(2)
        with col_actions[0]:
            if st.button("Pedir Carta (Hit)"):
                card = random.choice(st.session_state.deck)
                st.session_state.deck.remove(card)
                st.session_state.player_hand.append(card)
                if hand_value(st.session_state.player_hand) > 21:
                    st.session_state.game_over = True
                    st.session_state.result_message = "👎 Te pasaste de 21. ¡Perdiste!"
                st.rerun()
        
        with col_actions[1]:
            if st.button("Plantarse (Stand)"):
                # Dealer plays
                while hand_value(st.session_state.dealer_hand) < 17:
                    card = random.choice(st.session_state.deck)
                    st.session_state.deck.remove(card)
                    st.session_state.dealer_hand.append(card)
                
                player_final = hand_value(st.session_state.player_hand)
                dealer_final = hand_value(st.session_state.dealer_hand)
                
                st.session_state.game_over = True
                
                if dealer_final > 21:
                    st.session_state.result_message = "👍 El crupier se pasó. ¡Ganaste!"
                elif player_final > dealer_final:
                    st.session_state.result_message = "🏆 ¡Ganaste!"
                elif player_final < dealer_final:
                    st.session_state.result_message = "💀 Perdiste."
                else:
                    st.session_state.result_message = "🤝 Empate."
                st.rerun()

    if st.session_state.game_over:
        if "Ganaste" in st.session_state.result_message:
            st.success(st.session_state.result_message)
        elif "Perdiste" in st.session_state.result_message:
            st.error(st.session_state.result_message)
        else:
            st.info(st.session_state.result_message)
