from src.analysis.TopScorersStrategy import TopScorersStrategy
from src.commands.TopScorersCommand import TopScorersCommand


class SoccerAnalysisCLI:

    def __init__(self, data_loader):
        self.commands = {
            'top_scorers': TopScorersCommand(TopScorersStrategy(data_loader)),
            'help': self.show_help,
            # Add more commands here
        }

    def start(self):
        self.show_help()  # Show the help message at startup
        while True:
            command = input("Enter command: ")
            if command in self.commands:
                self.commands[command].execute()
            elif command == 'quit':
                break
            else:
                print("Invalid command. Please try again.")

    def show_help(self):
        print("Available commands:")
        for command in self.commands:
            print("-", command)