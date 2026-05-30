# main.py — Zero-Shot, One-Shot, and Few-Shot Learning Activity
# Switch provider by changing the import:
#   from groq import generate_response   ← uses Groq (default)
#   from hf import generate_response     ← uses Hugging Face

from groq import generate_response
# from hf import generate_response

def run_activity():
    print("ZERO-SHOT, ONE-SHOT & FEW-SHOT LEARNING ACTIVITY")
    print("=" * 50)

    category = input("Enter a category (e.g., fruit, city, animal): ").strip()
    item = input(f"Enter a specific {category}: ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return

    # Zero-shot: no examples, just the question
    print("\n--- ZERO-SHOT LEARNING ---")
    zero_prompt = f"Is {item} a {category}? Answer yes or no."
    print(f"Prompt: {zero_prompt}")
    print("Response:", generate_response(zero_prompt, temperature=0.3, max_tokens=1024))

    # One-shot: single example before the task
    print("\n--- ONE-SHOT LEARNING ---")
    one_prompt = f"""Determine if the item belongs to the category.

Example:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("Response:", generate_response(one_prompt, temperature=0.3, max_tokens=1024))

    # Few-shot: multiple examples before the task
    print("\n--- FEW-SHOT LEARNING ---")
    few_prompt = f"""Determine if the item belongs to the category.

Example 1:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Example 2:
Category: fruit
Item: carrot
Answer: No, carrot is not a fruit. It's a vegetable.

Example 3:
Category: vehicle
Item: bicycle
Answer: Yes, bicycle is a vehicle.

Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("Response:", generate_response(few_prompt, temperature=0.3, max_tokens=1024))

    # Creative few-shot: generate one-sentence stories
    print("\n--- CREATIVE FEW-SHOT EXAMPLE ---")
    creative_prompt = f"""Write a one-sentence story about the given word.

Example 1:
Word: moon
Story: The moon winked at the lovers as they shared their first kiss.

Example 2:
Word: computer
Story: The computer sighed as another cup of coffee was spilled on its keyboard.

Word: {item}
Story:"""
    print("Response:", generate_response(creative_prompt, temperature=0.7, max_tokens=1024))

    # Reflection
    print("\n--- REFLECTION QUESTIONS ---")
    print("1. How did the responses differ between zero-shot, one-shot, and few-shot?")
    print("2. Which approach gave the most helpful or creative response?")
    print("3. How did examples in few-shot prompts guide the output?")
    print("4. How could you apply these techniques to your own tasks?")

if __name__ == "__main__":
    run_activity()
