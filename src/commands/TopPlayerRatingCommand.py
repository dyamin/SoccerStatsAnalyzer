from src.commands.Command import Command


class TopPlayerRatingCommand(Command):
    def __init__(self, analysis):
        self.analysis = analysis

    def execute(self, *args):
        top_rating = self.analysis.analyze(*args)
        print(top_rating.to_string(index=False, header=False))