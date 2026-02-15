app.py 
import streamlit as st
import random

# The "Data" - All current expansions
EXPANSIONS = {
    "The Worst Takes It All (Base)": ["Maleficent", "Jafar", "Ursula", "Captain Hook", "Queen of Hearts", "Prince John"],
    "Wicked to the Core": ["Hades", "Dr. Facilier", "Evil Queen"],
    "Evil Comes Prepared": ["Scar", "Ratigan", "Yzma"],
    "Perfectly Wretched": ["Cruella de Vil", "Mother Gothel", "Pete"],
    "Despicable Plots": ["Gaston", "Lady Tremaine", "The Horned King"],
    "Bigger and Badder": ["Syndrome", "Lotso", "Madam Mim"],
    "Filled with Fright": ["Oogie Boogie"]
}

st.title("😈 Villainous Game Selector")

# 1. Choose your expansions
st.sidebar.header("Your Collection")
selected_expansions = []
for box in EXPANSIONS.keys():
    if st.sidebar.checkbox(box, value=True):
        selected_expansions.append(box)

# 2. Choose number of players
num_players = st.number_input("How many players?", min_value=1, max_value=6, value=2)

# 3. The Big Button
if st.button("Generate Matchup"):
    # Pool all available villains
    available_villains = []
    for box in selected_expansions:
        available_villains.extend(EXPANSIONS[box])
   
    if len(available_villains) < num_players:
        st.error("Not enough villains selected for that many players!")
    else:
        # Randomize!
        results = random.sample(available_villains, k=num_players)
       
        st.subheader("Your Lineup:")
        for i, villain in enumerate(results, 1):
            st.write(f"**Player {i}:** {villain}")
