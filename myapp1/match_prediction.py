import os

import pandas as pd
import joblib
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt

from django.conf import settings

matplotlib.use('Agg')
# Load models and columns
model_home = joblib.load(settings.MODEL_HOME_PATH)
model_away = joblib.load(settings.MODEL_AWAY_PATH)
model_columns = joblib.load(settings.MODEL_COLUMNS_PATH)

df = pd.read_csv(settings.RESULTS_CSV_PATH)

def get_match_statistics(home_team, away_team):
    matches = df[((df['home_team'] == home_team) & (df['away_team'] == away_team)) | ((df['home_team'] == away_team) & (df['away_team'] == home_team))]

    if len(matches) == 0:
        home_team_stats = df[df['home_team'] == home_team]
        away_team_stats = df[df['home_team'] == away_team]
        return home_team_stats, away_team_stats

    match_stats = {
        'total_matches': len(matches),
        'home_team_wins': len(matches[matches['home_team'] == home_team]),
        'away_team_wins': len(matches[matches['home_team'] == away_team]),
        'draws': len(matches[(matches['home_score'] == matches['away_score'])]),
        'total_goals': matches['home_score'].sum() + matches['away_score'].sum(),
        'average_goals_per_match': (matches['home_score'].sum() + matches['away_score'].sum()) / len(matches)
    }

    return match_stats

def visualize_statistics(home_team, away_team):
    match_stats = get_match_statistics(home_team, away_team)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=['Home Team Wins', 'Away Team Wins', 'Draws'], y=[match_stats['home_team_wins'], match_stats['away_team_wins'], match_stats['draws']])
    plt.title('Match Outcomes')
    plt.xlabel('Outcome')
    plt.ylabel('Number of Matches')

    # Save plot to a file
    plot_filename = f'{home_team}_vs_{away_team}.png'
    plot_filepath = os.path.join(plot_filename)
    plt.savefig(plot_filepath)
    plt.close()

    return plot_filename

def predict_scores(home_team, away_team):
    input_data = pd.DataFrame([[0] * len(model_columns)], columns=model_columns)
    input_data['home_team_' + home_team] = 1
    input_data['away_team_' + away_team] = 1

    predicted_home_score = round(model_home.predict(input_data)[0])
    predicted_away_score = round(model_away.predict(input_data)[0])

    plot_filename = visualize_statistics(home_team, away_team)

    return predicted_home_score, predicted_away_score, plot_filename

def match(home_team, away_team):
    predicted_home_score, predicted_away_score, plot_filename = predict_scores(home_team, away_team)
    return f"Predicted score between {home_team} and {away_team}: {predicted_home_score} - {predicted_away_score}", plot_filename

