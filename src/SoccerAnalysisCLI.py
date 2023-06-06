from src.commands.CliCommandFactory import CliCommandFactory


class SoccerAnalysisCLI:

    def __init__(self, data_loader):
        self.data_loader = data_loader
        self.command_factory = CliCommandFactory(self.data_loader)
        self.active_commands = ['top_player_scorers', 'top_player_rating']

    def start(self):
        print("Welcome to the European Soccer Dataset analyzer.")
        self.show_help()

        while True:
            user_input = input("Enter command: ").strip().lower().split()
            command_name = user_input[0]
            command_args = user_input[1:]

            if command_name == 'quit':
                break
            elif command_name == 'help':
                self.print_help()
            else:
                command = self.command_factory.create_command(command_name, self.data_loader)
                if command is None:
                    print(f"Unknown command: {command_name}. Type 'help' to see the list of available commands.")
                else:
                    try:
                        command.execute(*command_args)
                    except Exception as e:
                        print(f"An error occurred while executing the command: {e}")

    def show_help(self):
        print("Available commands:")
        for command in self.active_commands:
            print("-", command)
