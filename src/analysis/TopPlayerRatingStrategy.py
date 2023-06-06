from src.analysis.AnalysisStrategy import AnalysisStrategy



class TopPlayerRatingStrategy(AnalysisStrategy):

    def __init__(self, data_loader):
        self.data_loader = data_loader

    def analyze(self, *args):
        players_num = int(args[0])
        players_df = self.data_loader.data['Player']
        player_attr_df = self.data_loader.data['Player_Attributes']

        # Get the player ids of the top players based on player_attr_df
        top_players = player_attr_df.groupby('player_api_id').mean().sort_values('overall_rating', ascending=False).head(players_num)['overall_rating']
        # Merge the player ids with the player table to get the names of the top players
        top_players = players_df.merge(top_players, left_on='player_api_id', right_index=True)[['player_name', 'overall_rating']]
        return top_players
