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

elif state == "playing":
    s = st.session_state
    remaining = s["max_attempts"] - s["attempts"]
    st.write("I have selected a number between 1 and 100.")
    st.write(f"You have **{s['max_attempts']}** attempts in total.")
    if s["hint"]:
        st.warning(s["hint"])
    st.info(f"Attempts remaining: {remaining}")
    st.number_input("Enter your guess", min_value=1, max_value=100, step=1, key="guess")
    st.button("Submit Guess", type="primary", on_click=submit_guess)

elif state == "won":
    s = st.session_state
    st.balloons()
    st.success("🎉 Congratulations! You guessed the correct number.")
    st.write(f"**Number:** {s['secret']}")
    st.write(f"**Attempts:** {s['attempts']}")
    st.write(f"**Round Score:** {s['round_score']}")
    st.write("Do you want to play another round?")
    b1, b2 = st.columns(2)
    b1.button("Yes, play again", type="primary", on_click=next_round, use_container_width=True)
    b2.button("No, finish game", on_click=finish_game, use_container_width=True)

elif state == "lost":
    s = st.session_state
    st.error("❌ GAME OVER!")
    st.write(f"The correct number was: **{s['secret']}**")
    st.write("Round Score: 0")
    st.write("Do you want to play another round?")
    b1, b2 = st.columns(2)
    b1.button("Yes, play again", type="primary", on_click=next_round, use_container_width=True)
    b2.button("No, finish game", on_click=finish_game, use_container_width=True)

elif state == "finished":
    s = st.session_state
    st.subheader("GAME FINISHED")
    st.write(f"**Total Rounds:** {s['total_rounds']}")
    st.write(f"**Final Score:** {s['total_score']}")
    st.write("Thank you for playing! 🎮")
    st.button("Start New Game", type="primary", on_click=new_game)
