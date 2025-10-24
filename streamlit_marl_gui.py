import streamlit as st
from marl_game import Game

# Initialize game
if 'game' not in st.session_state:
    st.session_state.game = Game()
    st.session_state.game.reset(n_blue=2, n_red=2)

# Title
st.title("Littoral Naval Warfare Simulation")

# Sidebar controls
st.sidebar.header("Controls")
selected_ship = st.sidebar.selectbox("Select Blue Ship", list(range(len(st.session_state.game.blue_ships))))
move_x = st.sidebar.slider("Move X", -3, 3, 0)
move_y = st.sidebar.slider("Move Y", -3, 3, 0)
engage = st.sidebar.checkbox("Engage Target")
radar_on = st.sidebar.checkbox("Radar On")

# Action button
if st.sidebar.button("Take Action"):
    ship = st.session_state.game.blue_ships[selected_ship]
    if ship is not None:
        action = [int(radar_on), float(engage), ship.position[0] + move_x, ship.position[1] + move_y]
        ship.take_action(action)

# Always show the updated game grid
st.subheader("Game Grid")
fig = st.session_state.game.visualize_grid(show=False)
st.pyplot(fig)

# Display ship status
st.subheader("Ship Status")
for i, ship in enumerate(st.session_state.game.blue_ships):
    if ship is not None:
        st.text(
            f"Ship {i}: Position={ship.position}, "
            f"Missiles={ship.missiles}, "
            f"Radar={'On' if ship.radar_transmission else 'Off'}"
        )

