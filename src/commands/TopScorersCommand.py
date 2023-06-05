from src.commands.Command import Command


class TopScorersCommand(Command):
    def __init__(self, analysis):
        self.analysis = analysis

    def execute(self):
        top_scorers = self.analysis.analyze()
        for scorer in top_scorers:
            print(scorer)