import xml.etree.ElementTree as ET
from collections import defaultdict

import pandas as pd

from src.analysis.AnalysisStrategy import AnalysisStrategy


class TopPlayerScorersStrategy(AnalysisStrategy):

    def __init__(self, data_loader):
        self.data_loader = data_loader

    def analyze(self, *args):
        players_num = int(args[0])
        goals_by_player_id = self.get_goals_by_player_id()[:players_num]

        # Map player api id to player name using Player table
        players = self.data_loader.data['Player']
        # Filter the top scorers
        filtered_players = players[
            players['player_api_id'].isin([player_id for player_id, goals in goals_by_player_id])]
        # Create dataframe with player name and goal count
        goals_by_player_name = {player['player_name']: goals for player_id, goals in goals_by_player_id for
                                index, player in filtered_players.iterrows() if player['player_api_id'] == player_id}
        sorted_players = sorted(goals_by_player_name.items(), key=lambda x: x[1], reverse=True)
        # Create dataframe with player name and goal count
        return pd.DataFrame(sorted_players, columns=['player_name', 'goals'])

    def get_goals_by_player_id(self):
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
                            player = int(child.text)
                            goal_counts[player] += 1

        # Sort the players by goal count and return the list
        return sorted(goal_counts.items(), key=lambda x: x[1], reverse=True)
