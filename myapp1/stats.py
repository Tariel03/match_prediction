import pandas as pd

from myproject import settings

df = pd.read_csv(settings.RESULTS_CSV_PATH)


def get_most_successful_teams():
    home_wins = df[df['home_score'] > df['away_score']]['home_team'].value_counts()
    away_wins = df[df['away_score'] > df['home_score']]['away_team'].value_counts()

    team_results = home_wins.add(away_wins, fill_value=0).sort_values(ascending=False)
    return team_results.head(15)


def tournaments():
    tournament_counts = df['tournament'].value_counts()
    print("Самые популярные турниры:")
    tournaments = tournament_counts.head(9)
    return tournaments

