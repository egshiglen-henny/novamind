# NovaMind - AI Brainstorm Assistant
# Author: Egshiglen Enkhbayar

from openai import OpenAI
import time
import re

def validate_input(user_input):
    # accepts - letters, numbers, spaces, common tech symbols (+, /, # etc.,)
    # rejects - empty, whitespace strings, numbers only, emojis, random symbols, gibberish
    
    if not user_input or user_input.isspace():
        return False
    
    # allow letters, digits, spaces and tech symbols
    if not re.match(r'^[A-Za-z0-9\s+/#+.&\-_]+$', user_input):
        return False
    
    # reject gibberish pattern
    letters_only = user_input.replace(" ", "").isalpha()
    if letters_only:
        # too long and no spaces (might be gibberish like adsfjkhaf)
        if len(user_input) > 8 and " " not in user_input:
            return False
        # repeated single letters like aaaaaaa or bbbbbbb
        if len(set(user_input.lower())) == 1 and user_input.strip().upper() not in ["C", "R"]:
            return False
        
    # reject numbers only like 1234
    if user_input.replace(" ", "").isdigit():
        return False
    
    # reject short pattern
    if len(user_input.strip()) < 2: # pragma: no cover
        if user_input.strip().upper() not in ["C", "R"]:
            return False
    
    return True

def brainstorm(interests, goal):
    # generate 3 project ideas using OpenAI and return ideas as a string
    # set up OpenAI client
    client = OpenAI()
    # build prompt
    prompt = f"""
    You are NovaMind, a creative brainstorming assistant designed to help developers and innovators generate impactful, realistic project ideas.

    Context:
    - The user's main interests are: {interests}.
    - Their current goal or motivation is: {goal}.

    Instructions:
    1. Generate exactly **3 distinct project ideas** that align with the user's interests and goal.
    2. Keep the entire response under **250 tokens total**.
    3. Each idea must include:
    - A project name (creative and concise)
    - A one-sentence summary (clear and inspirational)
    - A brief description (1-2 sentences max) describing its purpose or core concept.
    4. Make all ideas roughly equal in length.
    5. Present your response in this format:
    
    Idea 1: [Project Name]  
    Summary: ...  
    Description: ...

    Idea 2: [Project Name]  
    Summary: ...  
    Description: ...

    Idea 3: [Project Name]  
    Summary: ...  
    Description: ...
    """

    start_time = time.time()  # start measuring

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300, # maximum length of the response
            temperature=0.7 # creativity 
        )

        end_time = time.time()  # stop measuring
        elapsed = end_time - start_time

        # print(f"\nResponse time: {elapsed:.2f} seconds\n")
        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {str(e)}"

def run_pipeline(interests: str, goal: str):
    # NovaMind workflow: validate inputs, generate brainstorm ideas, return final output
    if not validate_input(interests):
        return "Invalid interests"
    
    if not validate_input(goal):
        return "Invalid goal"
    
    return brainstorm(interests, goal)

if __name__ == "__main__": # pragma: no cover
    # greeting message
    print("Welcome to NovaMind — Your AI Brainstorm Assistant!")

    # loop until the user types exit
    while True:
        interests = input("What are your interests? (type 'exit' to quit): ").strip()
        if interests.lower() == "exit":
            print("Goodbye! Hope NovaMind inspired you today.")
            break

        # validate user input
        if not validate_input(interests):
            print("Please enter valid text (letters, numbers, and basic symbols like +, /, or #).")
            continue

        goal = input("What is your goal (e.g., build a project, learn a new skill)? ").strip()
        if not validate_input(goal):
            print("Please enter valid text (letters, numbers, and basic symbols like +, /, or #).")
            continue

        # run brainstorm function
        try:
            result = run_pipeline(interests, goal)
            print("\nNovaMind's Ideas:\n")
            print(result)
        except Exception as e:
            print(f"Oops! Something went wrong: {e}")
