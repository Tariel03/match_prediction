import csv


def get_team_names_from_csv(csv_file_path):
    team_names = set()
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            team_names.add(row[1])  # Assuming the home team is in the second column
            team_names.add(row[2])  # Assuming the away team is in the third column
    return team_names
