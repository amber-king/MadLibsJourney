# Purpose: Mad Libs: 
# Create a program that prompts users for words and builds a mystery story using them. 
# This reinforces string manipulation techniques.

import random

# Define prompts for additional details
prompts = [
    "Describe the strange creature you encounter next:",
    "What do you see in the distance?",
    "How do you react to the voice booming from above?",
    "What challenges do you face in your quest to save the {number} {noun}s?",
    "What unexpected discovery do you make?",
    "Who (or what) comes to your aid in your time of need?",
    "Describe a turning point in the story where everything changes.",
    "What hidden truth do you uncover?",
    "What internal conflict do you wrestle with?",
    "How do you use your wit (or strength) to overcome an obstacle?",
    "What emotional impact does this adventure have on you?",
]

def create_story():
    genre = input("Choose a genre (Mystery, Horror, Thriller, Drama, Psychological, Action, Humor): ").lower()

    # Story Prompts based on Genre
    if genre == "mystery":
        noun = input("Enter a noun (e.g., figure, diary): ")
        verb_ing = input("Enter a verb (ing form): ")  # Clarify verb form
        adjective = input("Enter an adjective: ")
        adverb = input("Enter an adverb: ")
        exclamation = input("Enter an exclamation (e.g., Aha!, Uh oh!): ")
        story = f"""As you were {verb_ing} through the {adjective} marketplace, you noticed a peculiar glint coming from a {noun} shop window. Curiosity piqued, you ventured inside. The air hung heavy with the scent of old books and forgotten trinkets. Suddenly, a muffled thump echoed from the back room. {exclamation}, you thought. Something's not right here..."""
    elif genre == "horror":
        verb_ing = input("Enter a verb (ing form): ")  # Clarify verb form
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun (e.g., cabin, graveyard): ")
        adverb = input("Enter an adverb: ")
        exclamation = input("Enter an exclamation (e.g., Help me!, Run away!): ")
        story = f"""The wind howled eerily as you ventured deeper into the {adjective} forest. You were on a camping trip with friends, but they had mysteriously disappeared earlier. Reaching a clearing, you stumbled upon a chilling sight: an {noun} shrouded in mist. A primal fear gripped you as you {adverb} approached, a faint whisper slithering into your ears... {exclamation}"""
    elif genre == "thriller":
        verb_ing = input("Enter a verb (ing form): ")  # Clarify verb form
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun (e.g., pursuers, storm): ")
        adverb = input("Enter an adverb: ")
        exclamation = input("Enter an exclamation (e.g., Almost there!, This can't be happening!): ")
        story = f"""Sweat beaded on your forehead as you {verb_ing} through the rain-slicked streets. The pounding of footsteps echoed behind you – your {adjective} pursuers were closing in. A flash of lightning illuminated a narrow alleyway. You ducked inside, hoping to lose them in the labyrinthine maze... {exclamation}"""
    elif genre == "drama":
        verb_ing = input("Enter a verb (ing form): ")  # Clarify verb form
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun (e.g., suitcase, letter): ")
        adverb = input("Enter an adverb: ")
        exclamation = input("Enter an exclamation (e.g., I have to try!, What have I done?): ")
        story = f"""With a heavy heart, you were {verb_ing} your belongings into a {adjective} suitcase. Leaving everything you knew behind was a difficult decision, but the {noun} you received forced your hand. You glanced back at the empty room, a thousand memories flooding your mind. {adverb}, you picked up the suitcase and stepped out the door... {exclamation}"""
    elif genre == "psychological":
        verb_ing = input("Enter a verb driving you crazy (e.g., questioning, noticing): ")
        adjective = input("Enter an adjective describing the anomaly (e.g., unsettling, distorted): ")
        noun = input("Enter a noun related to the anomaly (e.g., reflections, memories): ")
        adverb = input("Enter an adverb describing your actions (e.g., increasingly, desperately): ")
        exclamation = input("Enter an exclamation of disbelief (e.g., Is this real?, I can't): ")
        story = f"""As you were {verb_ing} the {adjective} {noun}, you noticed something strange. The {noun} seemed to be shifting, changing, as if reality itself was unraveling. You tried to stay calm, but {adverb}, the sense of dread grew stronger. {exclamation}, you thought, as the world around you twisted into a nightmare."""
    elif genre == "humor":
        verb_ing = input("Enter a verb (ing form): ")  # Clarify verb form
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun (e.g., dog, cat): ")
        adverb = input("Enter an adverb: ")
        exclamation = input("Enter an exclamation (e.g., Oh no!, This is too much!): ")
        story = f"""As you were {verb_ing} through the {adjective} entrance of the {noun}, you realized you might be slightly underdressed. Everyone else was sporting the latest in {adjective} fashion, while you stood out in your mismatched outfit. {adverb}, you tripped over your own shoelace, landing face-first into a plate of hors d'oeuvres. {exclamation}, you thought. This is not how I envisioned making a grand entrance..."""
    else:
        story = "Invalid genre selected. Please restart the program and choose a valid genre."

    print(story)

    # Randomly choose and display a prompt
    random_prompt = random.choice(prompts)
    user_detail = input(random_prompt)

    # Include user detail in the final story segment
    story += f"\n{user_detail}"

    # Print the final story
    print(story)

    # User Choice to Continue/Exit
    user_choice = input("Would you like to continue this adventure (y/n) or exit (exit/quit)? ").lower()
    if user_choice in ("exit", "quit"):
        return  # Exit the function if user chooses to quit

# Main loop for the game
while True:
    create_story()
    user_choice = input("Would you like to continue this adventure (y/n) or exit (exit/quit)? ").lower()
    if user_choice in ("exit", "quit"):
        break

print("Thank you for playing!")
