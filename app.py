from flask import Flask, render_template

app = Flask(__name__)

reasons = [
    "Your smile is my daily sunshine.",
    "You make even ordinary days feel magical.",
    "The way you laugh at my silly jokes.",
    "Your hugs feel like home.",
    "You believe in me when I doubt myself.",
    "The sparkle in your eyes when you’re excited.",
    "You dance with me even when there’s no music.",
    "You’re my partner in crime for midnight snacks.",
    "You make every trip an adventure.",
    "You know how to calm me instantly.",
    "Your kindness inspires me to be better.",
    "You’re playful, yet deeply caring.",
    "You never let me give up.",
    "You make me feel like the luckiest person alive.",
    "You’re my favorite storyteller.",
    "You love me even when I’m grumpy.",
    "You’re the best listener.",
    "You surprise me with little things that mean so much.",
    "You’re my safe place.",
    "You make me laugh until my stomach hurts.",
    "You’re beautiful inside and out.",
    "You’re my biggest cheerleader.",
    "You’re fearless when it comes to protecting us.",
    "You’re my favorite travel buddy.",
    "You make celebrations unforgettable.",
    "You’re my best friend and soulmate.",
    "You bring out the child in me.",
    "You’re the reason I believe in love stories.",
    "You make silence feel comfortable.",
    "You’re my forever partner in dreams.",
    "You love me in ways I never imagined possible.",
    "You’re simply you — and that’s more than enough."
]

@app.route("/")
def splash():
    return render_template("splash.html")

@app.route("/card")
def card():
    return render_template("index.html", reasons=reasons)

if __name__ == "__main__":
    app.run()
