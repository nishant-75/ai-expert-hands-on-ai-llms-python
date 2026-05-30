# main.py — AI Writing Assistant: Generate and Refine Essays
# Switch provider by changing the import:
#   from groq import generate_response   ← uses Groq (default)
#   from hf import generate_response     ← uses Hugging Face

from groq import generate_response
# from hf import generate_response

def get_essay_details():
    print("\n=== AI Writing Assistant ===\n")
    topic = input("What is the topic of your essay? ").strip()
    essay_type = input(
        "What type of essay? (Argumentative/Expository/Descriptive/Persuasive/Analytical): "
    ).strip()

    print("\nSelect essay word count:")
    print("1) 300 words\n2) 900 words\n3) 1200 words\n4) 2000 words")
    wc = input("Enter choice (1-4): ").strip()
    length_map = {"1": "300", "2": "900", "3": "1200", "4": "2000"}
    length = length_map.get(wc, "300")

    target_audience = input("Target audience (e.g., High school students): ").strip()
    specific_points = input("Any specific points to include? ").strip()
    stance = input("Your stance (For/Against/Neutral): ").strip()
    references = input("Any sources/quotes/references? ").strip()
    writing_style = input("Preferred writing style (Formal/Conversational/Academic/Creative): ").strip()
    outline_needed = input("Would you like an outline first? (Yes/No): ").strip().lower()

    return {
        "topic": topic, "essay_type": essay_type, "length": length,
        "target_audience": target_audience, "specific_points": specific_points,
        "stance": stance, "references": references,
        "writing_style": writing_style, "outline_needed": outline_needed,
    }

def generate_essay_content(d):
    try:
        temp = float(input("\nEnter temperature (0.2 structured, 0.7 creative): ").strip())
        if not (0.0 <= temp <= 1.0):
            raise ValueError
    except ValueError:
        print("Invalid temperature. Using 0.3.")
        temp = 0.3

    ctx = (
        f"Essay type: {d['essay_type']} | Topic: {d['topic']} | "
        f"Length: {d['length']} words | Stance: {d['stance']} | "
        f"Audience: {d['target_audience']} | Style: {d['writing_style']} | "
        f"Must include: {d['specific_points']} | References: {d['references']}"
    )

    # Optional outline
    if d["outline_needed"] in ("yes", "y"):
        outline = generate_response(f"Create a clear essay outline. {ctx}", temperature=temp, max_tokens=1024)
        print("\n=== Suggested Outline ===\n")
        print(outline)

    # Introduction
    intro = generate_response(f"Write the introduction only. {ctx}", temperature=temp, max_tokens=1024)
    print("\n=== Generated Introduction ===\n")
    print(intro)

    # Body — full draft or step-by-step
    print("\nHow would you like the body generated?")
    print("1) Full draft\n2) Step-by-step")
    choice = input("> ").strip()

    if choice == "1":
        body = generate_response(
            f"Write the full body (arguments, evidence, reasoning). {ctx}", temperature=temp, max_tokens=1024
        )
        print("\n=== Generated Full Body ===\n")
        print(body)
    else:
        body = generate_response(
            f"Write step-by-step arguments with evidence and reasoning. {ctx}", temperature=temp, max_tokens=1024
        )
        print("\n=== Generated Step-by-Step Body ===\n")
        print(body)

    # Conclusion
    concl = generate_response(
        f"Write the conclusion only. Summarize key points and reinforce the thesis. {ctx}",
        temperature=temp, max_tokens=1024
    )
    print("\n=== Generated Conclusion ===\n")
    print(concl)

def feedback_and_refinement():
    rating = input("\nHow satisfied are you with the essay? (1-5): ").strip()
    if rating != "5":
        feedback = input("Provide feedback (tone, structure, clarity, etc.): ").strip()
        print(f"\nThank you! We'll refine based on: {feedback}")
    else:
        print("\nThank you! The essay looks great.")

def run_activity():
    print("\nWelcome to the AI Writing Assistant!")
    details = get_essay_details()
    if not details["topic"] or not details["essay_type"]:
        print("Please provide at least a topic and essay type to continue.")
        return
    generate_essay_content(details)
    feedback_and_refinement()

if __name__ == "__main__":
    run_activity()
