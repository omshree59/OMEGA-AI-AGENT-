from models.ollama_model import ask
from memory.memory import Memory
from memory.database import Database


memory = Memory()
database = Database()


print("=" * 50)
print("🤖 OMEGA AGENTIC AI ")
print("=" * 50)


while True:

    user = input("You: ")


    if user.lower().strip() in ["exit", "quit", "/bye"]:
        print("OMEGA AI shutting down...")
        break



    # Show memory
    if user.lower().strip() == "memory":

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
You are OMEGA AI, a personal AI assistant.

You have access to stored user information.
Use it naturally when relevant.

The stored information is NOT a previous conversation.
It is only facts/preferences the user shared earlier.

Do not invent:
- previous meetings
- previous chats
- events that did not happen
- emotions or actions

Respond naturally like a helpful assistant.
"""



    response = ask(prompt)



    # Save short term memory
    memory.add_message(user, response)



    # Save important information
    important_words = [
        "my name is",
        "my name is",
        "i am",
        "i like",
        "i love",
        "i have",
        "i want",
        "i created",
        "i built",
        "creator of",
        "creator",
        "maker"
        "made"
    ]


    for word in important_words:

        if word in user.lower():

            category = "personal"
            if "creator" in user.lower() or "created" in user.lower():
                category = "project"
            elif "like" in user.lower() or "love" in user.lower():
                category = "interest"
            database.add_memory(
                user,
                category
            )

            break



    print("\nAgent:", response)
    print()