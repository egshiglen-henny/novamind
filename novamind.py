# NovaMind - AI Brainstorm Assistant
# Author: Egshiglen Enkhbayar

from openai import OpenAI

def brainstorm(interests, goal):
    client = OpenAI()
    prompt = f"""
    You are NovaMind, an AI brainstorming assistant.
    The user is interested in: {interests}.
    Their goal is: {goal}.
    Generate 3 unique, creative, and practical project ideas with short descriptions.
    Each idea should have a name and a one-sentence summary.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.9
    )

    print("\n💡 NovaMind's Ideas:\n")
    print(response.choices[0].message.content)

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
