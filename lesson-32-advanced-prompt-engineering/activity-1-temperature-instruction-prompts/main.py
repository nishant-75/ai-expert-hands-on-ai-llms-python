# main.py — Advanced Prompt Engineering: Temperature & Instruction-Based Prompts
# Switch provider by changing the import below:
#   from groq import generate_response   ← uses Groq (default)
#   from hf import generate_response     ← uses Hugging Face

from groq import generate_response
# from hf import generate_response

import time

def pseudo_stream(text, delay=0.013):
    """Print text character-by-character for a streaming-like effect."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def temperature_prompt_activity():
    print("=" * 80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    print("=" * 80)

    # PART 1: Temperature exploration
    print("\n" + "-" * 40)
    print("PART 1: TEMPERATURE EXPLORATION")
    print("-" * 40)
    base_prompt = input("Enter a creative prompt (e.g., 'Write a short story about a robot learning to paint'): ").strip()

    print("\nGenerating responses with different temperature settings...")
    for t, label in [
        (0.1, "LOW (0.1) - Deterministic"),
        (0.5, "MEDIUM (0.5) - Balanced"),
        (0.9, "HIGH (0.9) - Creative"),
    ]:
        print(f"\n--- {label} ---")
        print(generate_response(base_prompt, temperature=t, max_tokens=512))
        time.sleep(1)

    # PART 2: Instruction-based prompts
    print("\n" + "-" * 40)
    print("PART 2: INSTRUCTION-BASED PROMPTS")
    print("-" * 40)
    topic = input("Choose a topic (e.g., 'climate change', 'space exploration'): ").strip()

    instructions = [
        f"Summarize the key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-year-old child.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional news headline from the year 2050 about {topic}.",
    ]
    for i, instruction in enumerate(instructions, 1):
        print(f"\n--- INSTRUCTION {i}: {instruction} ---")
        print(generate_response(instruction, temperature=0.7, max_tokens=512))
        time.sleep(1)

    # PART 3: Custom prompt
    print("\n" + "-" * 40)
    print("PART 3: CREATE YOUR OWN PROMPT")
    print("-" * 40)
    custom = input("Enter your instruction-based prompt: ").strip()
    try:
        temp = float(input("Set a temperature (0.1 to 1.0): ").strip())
        if not (0.1 <= temp <= 1.0):
            raise ValueError
    except ValueError:
        print("Invalid input. Using default temperature 0.7.")
        temp = 0.7

    print(f"\n--- YOUR CUSTOM PROMPT @ TEMP {temp} ---")
    print(generate_response(custom, temperature=temp, max_tokens=512))

    # Reflection
    print("\n" + "-" * 40)
    print("REFLECTION QUESTIONS")
    print("-" * 40)
    print("1. How did changing the temperature affect the creativity and variety?")
    print("2. Which instruction-based prompt produced the most useful or creative result?")
    print("3. How would you use temperature + instructions for a real-world task?")
    print("4. What surprised you about the AI's behavior with these changes?")
    print("\nCHALLENGE: Create a prompt chain:")
    print("Generate content → rewrite with constraints → create a sequel (try different temps).")

def bonus_stream():
    choice = input("\nBONUS: streaming-like output? (y/n): ").lower().strip()
    if choice == "y":
        p = input("Enter a prompt: ").strip()
        out = generate_response(p, temperature=0.7, max_tokens=512)
        print("\nStreaming-like response (not real streaming):")
        pseudo_stream(out)

if __name__ == "__main__":
    temperature_prompt_activity()
    bonus_stream()
