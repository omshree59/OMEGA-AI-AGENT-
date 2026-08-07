from models.ollama_model import ask
from memory.memory import Memory
from memory.database import Database


memory = Memory()
database = Database()


print("=" * 50)
print("🤖 OMEGA AI AGENT")
print("=" * 50)


while True:

    user = input("You: ")


    if user.lower() in ["exit", "quit", "/bye"]:
        print("OMEGA AI shutting down...")
        break



    # Show memory
    if user.lower() == "memory":

        print("\n===== SHORT TERM MEMORY =====")
        memory.show_memory()


        print("\n===== LONG TERM MEMORY =====")

        memories = database.get_memories()

        for item in memories:
            print(f"- {item[0]} [{item[1]}]")


        print("=" * 30)

        continue



    # Load all saved memories
    old_memories = database.get_memories()


    formatted_long_memory = ""

    for item in old_memories:

        formatted_long_memory += f"""
Memory:
{item[0]}

Category:
{item[1]}
"""



    # Load conversation history
    history = memory.get_history()


    formatted_history = ""

    for chat in history:

        formatted_history += f"""
User:
{chat['user']}

Assistant:
{chat['assistant']}
"""



    prompt = f"""
You are OMEGA AI, a personal AI assistant.

Use previous memories to answer the user.

Long Term Memories:

{formatted_long_memory}


Current Conversation:

{formatted_history}


Current User Message:

{user}


Answer naturally.

IMPORTANT:
Only use information from memories.
If you don't know something, say you don't know.
Never invent names, facts, or previous conversations.
"""



    response = ask(prompt)



    # Save short term memory
    memory.add_message(user, response)



    # Save important information
    important_words = [
        "my name is",
        "i like",
        "i love",
        "i have",
        "i want",
        "i created",
        "i built"
    ]


    for word in important_words:

        if word in user.lower():

            database.add_memory(
                user,
                "personal"
            )

            break



    print("\nAgent:", response)
    print()