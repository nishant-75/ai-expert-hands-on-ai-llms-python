# main.py — Bias Mitigation & Token Limit Handling Activity
# Switch provider by changing the import:
#   from groq import generate_response   ← uses Groq (default)
#   from hf import generate_response     ← uses Hugging Face

from groq import generate_response
# from hf import generate_response

def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return

    # Generate initial response (may contain bias)
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response:\n{initial_response}")

    # Rewrite to reduce bias
    modified_prompt = input(
        "\nModify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): "
    ).strip()
    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nModified AI Response (Neutral):\n{modified_response}")
    else:
        print("No modified prompt entered. Skipping neutral response.")

    print("\n--- Reflection ---")
    print("1. How did modifying the prompt affect the AI's response in terms of bias?")
    print("2. What words or phrases introduced bias in the original prompt?")
    print("3. What strategies can you use to write fairer prompts in the future?")

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    long_prompt = input(
        "Enter a long prompt (e.g., a detailed story or description with 300+ words): "
    ).strip()

    if long_prompt:
        long_response = generate_response(long_prompt, temperature=0.3, max_tokens=1024)
        # Show only a preview if response is very long
        preview = (long_response[:500] + "...") if len(long_response) > 500 else long_response
        print(f"\nResponse to Long Prompt (preview):\n{preview}")
    else:
        print("No long prompt entered. Skipping long prompt response.")

    short_prompt = input("\nNow, condense the prompt to be more concise: ").strip()
    if short_prompt:
        short_response = generate_response(short_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nResponse to Condensed Prompt:\n{short_response}")
    else:
        print("No condensed prompt entered. Skipping condensed response.")

    print("\n--- Reflection ---")
    print("1. How did the AI's response change when you condensed the prompt?")
    print("2. Did the shorter prompt retain all the key information?")
    print("3. What strategies help condense prompts without losing meaning?")

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Bias Mitigation")
    print("2) Token Limits")
    choice = input("> ").strip()

    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    run_activity()
