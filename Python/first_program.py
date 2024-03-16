class FirstProgram():
    def __init__(self):
        self.name = None
    
    def ask_question(self):
        return print("Tell me. What is your name?")
    
    def response(self):
        self.name = input()
        return print(f"My name is: {self.name}")

if __name__ == "__main__":
    fp = FirstProgram()

    fp.ask_question()
    fp.response()