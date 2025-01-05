import datetime
import random
import re

# Enhanced Chatbot
def enhanced_chatbot():
    print("Chatbot: Hi there! I'm your enhanced chatbot created by Utsho Kumar Dey. What's your name?")
    user_name = input("You: ").strip()
    print(f"Chatbot: Nice to meet you, {user_name}! Ask me anything or type 'help' to see what I can do.")
    print("Type 'exit' to end the conversation.\n")

    responses = {
        "hello": ["Hello! How can I assist you?", "Hi there! What's on your mind?", f"Hey {user_name}! Need any help?"],
        "how are you": ["I'm just a bot, but I'm doing great! How about you?", "Feeling fantastic! How can I help?"],
        "what is your name": [f"My name is ChatBotUKD, created by Utsho Kumar Dey!"],
        "time": ["The current time is "],
        "date": ["Today's date is "],
        "joke": ["Why don't scientists trust atoms? Because they make up everything!",
                 "Why did the math book look sad? It had too many problems.",
                 "Why did the scarecrow win an award? Because he was outstanding in his field!"],
        "weather": ["I'm not a meteorologist, but you can check a weather app for accurate updates!"],
        "bye": [f"Goodbye, {user_name}! Have a nice day!", f"Bye, {user_name}! Take care!", "See you later!"],
        "positive": ["I'm glad to hear that!", "That's wonderful to know!", "Keep up the great energy!"],
        "negative": ["I'm sorry to hear that. Is there anything I can do to help?", "Cheer up! Things will get better."],
        "default": ["I'm sorry, I didn't understand that.", "Could you rephrase your question?", "Hmm, I'm not sure about that."]
    }

    def calculate(expression):
        try:
            result = eval(expression)
            return f"The answer is {result}."
        except:
            return "I couldn't understand the calculation. Please try again."

    def detect_sentiment(user_input):
        positive_words = ["great", "good", "awesome", "happy", "fantastic"]
        negative_words = ["bad", "sad", "upset", "angry", "terrible"]
        if any(word in user_input for word in positive_words):
            return "positive"
        elif any(word in user_input for word in negative_words):
            return "negative"
        return None

    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Chat session ended. Goodbye!")
            break

        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: {responses['time'][0]}{current_time}.")
        
        elif "date" in user_input:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            print(f"Chatbot: {responses['date'][0]}{current_date}.")
        
        elif "weather" in user_input:
            print(f"Chatbot: {random.choice(responses['weather'])}")
        
        elif "joke" in user_input:
            joke = random.choice(responses["joke"])
            print(f"Chatbot: {joke}")

        elif re.search(r'\d+[\+\-\*/]\d+', user_input):
            print(f"Chatbot: {calculate(user_input)}")
        
        else:
            sentiment = detect_sentiment(user_input)
            if sentiment:
                response = random.choice(responses[sentiment])
            else:
                matched_responses = [responses[key] for key in responses if key in user_input]
                if matched_responses:
                    response = random.choice(matched_responses[0])
                else:
                    response = random.choice(responses["default"])
            print(f"Chatbot: {response}")

enhanced_chatbot()
