class Memory:

    def __init__(self):
        self.history = []


    def add_message(self, user, assistant):
        self.history.append({
            "user": user,
            "assistant": assistant
        })


    def get_history(self):
        return self.history


    def show_memory(self):
        for item in self.history:
            print("USER:", item["user"])
            print("AI:", item["assistant"])
            print("-" * 30)


    def clear(self):
        self.history = []