# NovaMind - AI Brainstorm Assistant
# Author: Egshiglen Enkhbayar

from openai import OpenAI
import time

def brainstorm(interests, goal):
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
    - A **project name** (creative and concise)
    - A **one-sentence summary** (clear and inspirational)
    - A **brief description** (1-2 sentences max) describing its purpose or core concept.
    4. Make all ideas roughly equal in length.
    5. Present your response in this format:
    
    Idea 1: *[Project Name]*  
    **Summary:** ...  
    **Description:** ...

    Idea 2: *[Project Name]*  
    **Summary:** ...  
    **Description:** ...

    Idea 3: *[Project Name]*  
    **Summary:** ...  
    **Description:** ...
    """

    # give user feedback while they are waiting
    print("\nGenerating ideas... please wait...\n")
    
    start_time = time.time()  # start measuring

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300, # maximum length of the response
        temperature=0.7 # creativity 
    )

    end_time = time.time()  # stop measuring
    elapsed = end_time - start_time

    # print results
    print("\nNovaMind's Ideas:\n")
    print(response.choices[0].message.content)
    # print(f"\nResponse time: {elapsed:.2f} seconds\n")
    
if __name__ == "__main__":
    # greeting message
    print("Welcome to NovaMind — Your AI Brainstorm Assistant 🌟")

    # loop until the user types exit
    while True:
        interests = input("What are your interests? (type 'exit' to quit): ").strip()
        if interests.lower() == "exit":
            print("Goodbye! Hope NovaMind inspired you today.")
            break

        # validate user input
        elif not interests.replace(" ", "").isalnum():
            print("Please enter valid text (letters only, not numbers or symbols).")
            continue

        goal = input("What is your goal (e.g., build a project, learn a new skill)? ").strip()
        if not goal.replace(" ", "").isalnum():
            print("Please enter valid text (letters only, not numbers or symbols).")
            continue

        # run brainstorm function
        try:
            brainstorm(interests, goal)
        except Exception as e:
            print(f"Oops! Something went wrong: {e}")
