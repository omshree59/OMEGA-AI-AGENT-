from memory.memory import Memory


memory = Memory()


memory.add_message(
    "My name is Omshree",
    "Nice to meet you"
)


print(memory.get_history())