import re
import random
import long_responses as long

# Function to calculate the probability of a message based on recognized words
def likelihood(input, detected_words, singular_answer=False, essential_words=[]):
    confidence = 0
    includes_essential_words = True

    # Count the number of recognized words in the user message
    for term in input:
        if term in detected_words:
            confidence += 1
    
    # Calculate the percentage of recognized words in the message
    proportion = float(confidence) / float(len(detected_words))
    
    # Check if the user message contains all the essential words or if singular_answer flag is set
    for term in essential_words:
        if term not in input:
            includes_essential_words = False
            break
    
    # Return the probability as a percentage if essential words are present or singular_answer is True
    if includes_essential_words or singular_answer:
        return int(proportion * 100)
    else:
        return 0

# Function to check all possible bot answer and determine the best match
def inspect_messages(sentence):
    most_probable_list = {}  # Store the probabilities of bot answers

    def answer(bot_answer, list_of_terms, singular_answer=False, essential_words=[]):
        nonlocal most_probable_list
        # Calculate the probability of the bot answer based on the user message
        most_probable_list[bot_answer] = likelihood(sentence, list_of_terms, singular_answer, essential_words)

# Define bot answers and their corresponding recognized words and essential words
    answer('Hello', ['hello', 'hi', 'sup', 'hey', 'whatsup'], singular_answer=True)
    answer('I\'m good, and you?', ['how', 'are', 'you', 'doing'], essential_words=['how'])
    answer('Thank you!', ['i', 'love', 'talking', 'to','bots'])
    answer(long.r_ate,['what','you','eat'],essential_words=['you','eat'])

# Find the bot response with the highest probability
    closest_answer = max(most_probable_list, key=most_probable_list.get)

# Return the corresponding bot response if its probability is above a certain threshold, otherwise return unknown response
    return long.unknown() if most_probable_list[closest_answer] < 1 else closest_answer

# Function to get bot's response based on user input
def bot_answer(message):
    separate_message = re.split(r'\s+|[-?;,!.]\s*', message.lower())  # Split user input into individual words
    answer = inspect_messages(separate_message)  # Check all possible bot responses and determine the best match
    return answer

# Testing the response system in a loop
while True:
    submission = input('User: ')  # Get user input
    print('Chatbot: ' + bot_answer(submission))  # Get and print bot's response
