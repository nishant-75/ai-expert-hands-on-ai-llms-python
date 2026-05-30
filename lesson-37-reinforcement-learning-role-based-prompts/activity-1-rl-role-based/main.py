# main.py — Reinforcement Learning & Role-Based Prompts Activity
# Switch provider by changing the import:
#   from groq import generate_response   ← uses Groq (default)
#   from hf import generate_response     ← uses Hugging Face

from groq import generate_response
# from hf import generate_response

def reinforcement_learning_activity():
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")
    prompt = input("Enter a prompt for the AI model (e.g., 'Describe the lion'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return

    # Generate initial response
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response:\n{initial_response}")

    # Simulate rating (reward signal)
    try:
        rating = int(input("\nRate the response from 1 (bad) to 5 (good): ").strip())
        if rating < 1 or rating > 5:
            print("Invalid rating. Using 3.")
            rating = 3
    except ValueError:
        print("Invalid rating. Using 3.")
        rating = 3

    # Collect feedback and simulate improvement
    feedback = input("Provide feedback for improvement: ").strip()
    improved_response = f"{initial_response}\n\n[Improved with feedback: {feedback}]"
    print(f"\nImproved AI Response:\n{improved_response}")

    print("\n--- Reflection ---")
    print("1. How did the model's response improve with feedback?")
    print("2. How does reinforcement learning help AI improve its performance over time?")

def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    category = input("Enter a category (e.g., science, history, math): ").strip()
    item = input(f"Enter a specific {category} topic (e.g., 'photosynthesis' for science): ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return

    prompts = {
        "Teacher": f"You are a teacher. Explain {item} in simple terms.",
        "Expert": f"You are an expert in {category}. Explain {item} in a detailed, technical manner.",
        "Business Leader": f"As a business leader, explain how {item} can impact your industry.",
        "Peer Student": f"Explain {item} in terms a college student would understand.",
    }

    for role, prompt in prompts.items():
        response = generate_response(prompt, temperature=0.3, max_tokens=1024)
        print(f"\n--- {role}'s Perspective ---\n{response}")

    print("\n--- Reflection ---")
    print("1. How did the AI's response differ between different roles?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?")

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Reinforcement Learning")
    print("2) Role-Based Prompts")
    choice = input("> ").strip()

    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    run_activity()
