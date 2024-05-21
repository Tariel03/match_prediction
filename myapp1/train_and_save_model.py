import joblib
from sklearn.model_selection import train_test_split

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('results.csv')


X = df[['home_team', 'away_team']]
y_home = df['home_score']
y_away = df['away_score']


X = pd.get_dummies(X, columns=['home_team', 'away_team'])


X_train, X_test, y_train_home, y_test_home, y_train_away, y_test_away = train_test_split(X, y_home, y_away, test_size=0.2, random_state=42)


model_home = RandomForestRegressor(n_estimators=100, random_state=42)
model_home.fit(X_train, y_train_home)

model_away = RandomForestRegressor(n_estimators=100, random_state=42)
model_away.fit(X_train, y_train_away)




# Save models and columns
joblib.dump(model_home, 'model_home.pkl')
joblib.dump(model_away, 'model_away.pkl')
joblib.dump(X.columns, 'model_columns.pkl')

