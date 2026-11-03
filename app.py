import random

import streamlit as st

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")
st.title("🎯 NUMBER GUESSING GAME")

DIFFICULTY = {
    "Easy - 10 attempts": 10,
    "Medium - 7 attempts": 7,
    "Hard - 5 attempts": 5,
}

defaults = {
    "state": "setup",  # setup, playing, won, lost, finished
    "total_score": 0,
    "total_rounds": 0,
    "round_score": 0,
    "secret": None,
    "max_attempts": 0,
    "attempts": 0,
    "hint": "",
}
for key, value in defaults.items():
    st.session_state.setdefault(key, value)


def start_round():
    st.session_state["max_attempts"] = DIFFICULTY[st.session_state["difficulty"]]
    st.session_state["secret"] = random.randint(1, 100)
    st.session_state["attempts"] = 0
    st.session_state["hint"] = ""
    st.session_state["guess"] = 50
    st.session_state["state"] = "playing"


def submit_guess():
    s = st.session_state
    guess = int(s["guess"])
    s["attempts"] += 1

    if guess == s["secret"]:
        s["round_score"] = (s["max_attempts"] - s["attempts"] + 1) * 10
        s["total_score"] += s["round_score"]
        s["total_rounds"] += 1
        s["state"] = "won"
    elif s["attempts"] >= s["max_attempts"]:
        s["round_score"] = 0
        s["total_rounds"] += 1
        s["state"] = "lost"
    elif guess < s["secret"]:
        s["hint"] = "Hint: Your guess is TOO LOW."
    else:
        s["hint"] = "Hint: Your guess is TOO HIGH."


def next_round():
    st.session_state["state"] = "setup"


def finish_game():
    st.session_state["state"] = "finished"


def new_game():
    for key, value in defaults.items():
        st.session_state[key] = value


state = st.session_state["state"]

# Scoreboard
c1, c2 = st.columns(2)
c1.metric("Total Score", st.session_state["total_score"])
c2.metric("Rounds Played", st.session_state["total_rounds"])
st.divider()

if state == "setup":
    st.subheader("Choose Difficulty")
    st.radio("Difficulty", list(DIFFICULTY.keys()), key="difficulty")
    st.button("Start Round", type="primary", on_click=start_round)

elif state ==