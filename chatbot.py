import random

def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer get cold? Because it left its Windows open!",
        "Why was the JavaScript developer sad? Because they didn’t Node how to Express themselves.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet."
    ]
    return random.choice(jokes)

def give_help():
    return (
        "Sure! I can help with:\n"
        "- Telling jokes\n"
        "- Basic advice\n"
        "- Motivation\n"
        "- Simple tech explanations\n"
        "Just ask me something like 'Can you motivate me?' or 'What is AI?'"
    )

def give_motivation():
    messages = [
        "You are capable of amazing things. Keep going! 💪",
        "Remember why you started. You're doing great. 🌟",
        "Small steps every day lead to big results.",
        "You got this. I believe in you. 🚀"
    ]
    return random.choice(messages)

def explain_concept(topic):
    explanations = {
        "ai": "Artificial Intelligence (AI) refers to machines that can perform tasks that typically require human intelligence, like learning, reasoning, or understanding language.",
        "machine learning": "Machine Learning is a subset of AI that allows systems to learn from data and improve over time without being explicitly programmed.",
        "python": "Python is a versatile, beginner-friendly programming language known for its readability and wide range of applications."
    }
    return explanations.get(topic.lower(), "Hmm, I don't know much about that yet. Try asking about AI, Python, or Machine Learning.")

def fallback_response():
    responses = [
        "I'm not sure I understand, but I'm still learning!",
        "Could you rephrase that? I want to help.",
        "That’s interesting! Tell me more or ask for help anytime."
    ]
    return random.choice(responses)

# Intent recognition (simple keyword-based)
def recognize_intent(user_input):
    user_input = user_input.lower()

    if "joke" in user_input:
        return "joke"
    elif "help" in user_input:
        return "help"
    elif "motivate" in user_input or "motivation" in user_input:
        return "motivation"
    elif any(kw in user_input for kw in ["what is", "explain", "tell me about"]):
        for topic in ["ai", "python", "machine learning"]:
            if topic in user_input:
                return ("explain", topic)
        return ("explain", None)
    else:
        return "unknown"

def chatbot():
    print("👋 Hello! I'm SmartBot – here for fun or serious chat. Type 'exit' to leave.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("SmartBot: Goodbye! Take care and come back anytime! 👋")
            break

        intent = recognize_intent(user_input)

        if intent == "joke":
            print("SmartBot:", tell_joke())
        elif intent == "help":
            print("SmartBot:", give_help())
        elif intent == "motivation":
            print("SmartBot:", give_motivation())
        elif isinstance(intent, tuple) and intent[0] == "explain":
            topic = intent[1]
            if topic:
                print("SmartBot:", explain_concept(topic))
            else:
                print("SmartBot: Can you tell me which topic you'd like me to explain?")
        else:
            print("SmartBot:", fallback_response())

if __name__ == "__main__":
    chatbot()
