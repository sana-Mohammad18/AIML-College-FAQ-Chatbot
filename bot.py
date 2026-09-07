import aiml

bot = aiml.Kernel()

bot.learn("startup.aiml")

print("===================================")
print("       COLLEGE FAQ CHATBOT")
print("===================================")
print("Type 'bye' to exit.")
print()

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    response = bot.respond(user_input)
    print("Bot:", response)