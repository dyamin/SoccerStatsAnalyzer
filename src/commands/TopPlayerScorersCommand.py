from src.commands.Command import Command


class TopPlayerScorersCommand(Command):
    def __init__(self, analysis):
        self.analysis = analysis

    def execute(self, *args):
        top_scorers = self.analysis.analyze(*args)
        for scorer in top_scorers:
            print(scorer[0], ': ', scorer[1])