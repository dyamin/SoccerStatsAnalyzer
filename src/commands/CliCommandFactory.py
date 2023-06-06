from src.analysis.TopPlayerRatingStrategy import TopPlayerRatingStrategy
from src.analysis.TopPlayerScorersStrategy import TopPlayerScorersStrategy
from src.commands.TopPlayerRatingCommand import TopPlayerRatingCommand
from src.commands.TopPlayerScorersCommand import TopPlayerScorersCommand


class CliCommandFactory:
    def __init__(self, data_loader):
        self.data_loader = data_loader

    def create_command(self, name, data_loader):
        if name == 'top_player_scorers':
            return TopPlayerScorersCommand(TopPlayerScorersStrategy(data_loader))
        elif name == 'top_player_rating':
            return TopPlayerRatingCommand(TopPlayerRatingStrategy(data_loader))
        else:
            return None
