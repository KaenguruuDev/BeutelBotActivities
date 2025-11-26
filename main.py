from flask import Flask, Response
import random
import threading
import time

app = Flask("DiscordStatusServer")

possible_states = []
current_state = ""

def repopulate_states() -> None:
    # Load static texts from VALUE file
    global possible_states
    with open("VALUE", "r", encoding="utf-8") as f:
        possible_states = f.read().split('\n')

    # Load any dynamic texts from dynamic/
    for name in os.listdir("dynamic"):
        path = os.path.join("dynamic", name)

        if not os.path.isfile(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

            if len(lines) != 1:
                continue

            possible_states.append(lines[0])
            print("ADDING DYNAMIC STATE: " + lines[0])



def choose_next_state() -> str:
    return random.choice(possible_states)

def update_state_loop():
    global current_state
    while True:
        time.sleep(300)
        repopulate_states()

        if possible_states:
            current_state = choose_next_state()
            print("SELECTED NEW STATE: " + current_state)
        else:
            print("INVALID STATE LIST")

@app.route("/status", methods=["GET"])
def status():
    global possible_states, current_state
    with open("VALUE", "r", encoding="utf-8") as f:
        possible_states = f.read().split('\n')
    if current_state == "":
        current_state = choose_next_state()
    return Response(current_state, mimetype="text/plain")

if __name__ == "__main__":
    threading.Thread(target=update_state_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=3551)
