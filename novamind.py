# NovaMind - AI Brainstorm Assistant
# Author: Egshiglen Enkhbayar

from openai import OpenAI
import time;

def brainstorm(interests, goal):
    client = OpenAI()
    prompt = f"""
    You are NovaMind, a creative brainstorming assistant designed to help developers and innovators generate impactful, realistic project ideas.

    Context:
    - The user's main interests are: {interests}.
    - Their current goal or motivation is: {goal}.

    Instructions:
    1. Generate exactly **3 distinct project ideas** that align with the user's interests and goal.
    2. Each idea must include:
    - A **project name** (creative and concise)
    - A **one-sentence summary** (clear and inspirational)
    - A **short description** (2–3 sentences) explaining the purpose, target users, and technology or concept behind it.
    3. Ensure the ideas balance **creativity** and **feasibility** — they should be interesting enough to excite a developer but practical enough to build.
    4. Vary the themes (e.g., one web-based idea, one AI-based, one mobile or data-focused).
    5. Present your response in the following clean format:

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

    print("\nGenerating ideas... please wait...\n")
    
    start_time = time.time()  # ⏱️ Start measuring

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.9
    )

    end_time = time.time()  # ⏱️ Stop measuring
    elapsed = end_time - start_time

    print("\n💡 NovaMind's Ideas:\n")
    print(response.choices[0].message.content)
    # print(f"\n⏱️ Response time: {elapsed:.2f} seconds\n")
    
if __name__ == "__main__":
    print("Welcome to NovaMind — Your AI Brainstorm Assistant 🌟")

    while True:
        interests = input("What are your interests? (type 'exit' to quit): ").strip()
        if interests.lower() == "exit":
            print("👋 Goodbye! Hope NovaMind inspired you today.")
            break
        elif not interests.replace(" ", "").isalpha():
            print("⚠️ Please enter valid text (letters only, not numbers or symbols).")
            continue

        goal = input("What is your goal (e.g., build a project, learn a new skill)? ").strip()
        if not goal.replace(" ", "").isalpha():
            print("⚠️ Please enter valid text (letters only, not numbers or symbols).")
            continue

        try:
            brainstorm(interests, goal)
        except Exception as e:
            print(f"❌ Oops! Something went wrong: {e}")
