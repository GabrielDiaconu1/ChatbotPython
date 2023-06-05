import random

r_ate = "I'm a bot, so I don't need to eat"

def unknown():
    response = ['would you mind repeating that?',
                "...",
                "Thats correct",
                "Can you explain?"][random.randrange(4)]
    return response

def get_bot_response(question):
    if question == "What is your name?":
        return "My name is Chatbot."
    elif question == "How old are you?":
        return "I am 1 year old."
    else:
        return unknown()
