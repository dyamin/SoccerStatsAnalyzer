from src.analysis.AnalysisStrategy import AnalysisStrategy
import xml.etree.ElementTree as ET
from collections import defaultdict


class TopScorersStrategy(AnalysisStrategy):

    def __init__(self, data_loader):
        self.data_loader = data_loader

    def analyze(self):
        # Get number of top scorers to display
        num_scorers = int(input("Enter the number of top scorers to display: "))

        players = self.data_loader.data['Player']
        matches = self.data_loader.data['Match']

        # Count goals for each player
        goal_counts = defaultdict(int)
        for goals in matches['goal']:
            if goals is not None and goals.strip():
                # Parse the XML
                root = ET.fromstring(goals)
                # Loop over all 'value' elements in the XML
                for value in root.findall('value'):
                    # Loop over all child elements of 'value'
                    for child in value:
                        # If the tag of the child element starts with 'player'
                        if child.tag.startswith('player'):
                            # Get the player id and increment the goal count for this player
                            player = child.text
                            goal_counts[player] += 1

        # Sort the players by goal count and cut off the top 'num_scorers' players
        top_scorers = sorted(goal_counts.items(), key=lambda x: x[1], reverse=True)
        top_scorers = top_scorers[:num_scorers]

