import config
from SoccerAnalysisCLI import SoccerAnalysisCLI
from src.SoccerDataLoader import SoccerDataLoader


def main():
    # Initialize the data loader
    data_loader = SoccerDataLoader(config.database_path)

    # Initialize the command-line interface with the data loader
    cli = SoccerAnalysisCLI(data_loader)

    # Start the command-line interface
    cli.start()


# The script starts here
if __name__ == "__main__":
    main()
