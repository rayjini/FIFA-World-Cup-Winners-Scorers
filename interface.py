import sqlite3

def search_tournaments(year):
    conn = sqlite3.connect('world_cup.db')
    cursor = conn.cursor()

    query = """
    SELECT T.year, T.host_country, W.team_name AS winner, R.team_name AS runner_up, T.winner_score
    FROM Tournaments T
    JOIN Teams W ON T.winner_team_id = W.team_id
    JOIN Teams R ON T.runner_up_team_id = R.team_id
    WHERE T.year = ?;
    """
    cursor.execute(query, (year,))
    data = cursor.fetchone()

    if data:
        print("\nWorld Cup Winner:")
        print("{:<8} {:<20} {:<20} {:<20} {:<10}".format("Year", "Host", "Winner", "Runner-Up", "Score"))
        print("-" * 80)
        print("{:<8} {:<20} {:<20} {:<20} {:<10}".format(*data))
    else:
        print("\nNo results found for the specified year.")

    conn.close()

def search_top_scorers(year):
    conn = sqlite3.connect('world_cup.db')
    cursor = conn.cursor()

    query = """
    SELECT P.player_name, P.nationality, TS.goals_scored, TS.team_performance
    FROM Top_Scorers TS
    JOIN Players P ON TS.player_id = P.player_id
    JOIN Tournaments T ON TS.tournament_id = T.tournament_id
    WHERE T.year = ?;
    """
    cursor.execute(query, (year,))
    data = cursor.fetchone()

    if data:
        print("\nTop Scorer:")
        print("{:<25} {:<15} {:<10} {:<15}".format("Player", "Nationality", "Goals", "Performance"))
        print("-" * 70)
        print("{:<25} {:<15} {:<10} {:<15}".format(*data))
    else:
        print("\nNo results found for the specified year.")

    conn.close()

def display_winner_and_top_scorer(year):
    conn = sqlite3.connect('world_cup.db')
    cursor = conn.cursor()

    winner_query = """
    SELECT T.year, T.host_country, W.team_name AS winner, R.team_name AS runner_up, T.winner_score
    FROM Tournaments T
    JOIN Teams W ON T.winner_team_id = W.team_id
    JOIN Teams R ON T.runner_up_team_id = R.team_id
    WHERE T.year = ?;
    """
    cursor.execute(winner_query, (year,))
    winner_data = cursor.fetchone()

    top_scorer_query = """
    SELECT P.player_name, P.nationality, TS.goals_scored, TS.team_performance
    FROM Top_Scorers TS
    JOIN Players P ON TS.player_id = P.player_id
    JOIN Tournaments T ON TS.tournament_id = T.tournament_id
    WHERE T.year = ?;
    """
    cursor.execute(top_scorer_query, (year,))
    top_scorer_data = cursor.fetchone()

    if winner_data:
        print("\nWorld Cup Winner:")
        print("{:<8} {:<20} {:<20} {:<20} {:<10}".format("Year", "Host", "Winner", "Runner-Up", "Score"))
        print("-" * 80)
        print("{:<8} {:<20} {:<20} {:<20} {:<10}".format(*winner_data))
    else:
        print("\nNo results found for the winner in the specified year.")

    if top_scorer_data:
        print("\nTop Scorer:")
        print("{:<25} {:<15} {:<10} {:<15}".format("Player", "Nationality", "Goals", "Performance"))
        print("-" * 70)
        print("{:<25} {:<15} {:<10} {:<15}".format(*top_scorer_data))
    else:
        print("\nNo top scorer data found for the specified year.")

    conn.close()

def main():
    while True:
        print("\nWorld Cup Database Interface")
        print("1. Search World Cup Winner")
        print("2. Search Top Scorer")
        print("3. Search Both Winner and Top Scorer")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice in ['1', '2', '3']:
            year = input("Enter the year of the tournament (1970-2022): ")

            if choice == '1':
                search_tournaments(year)
            elif choice == '2':
                search_top_scorers(year)
            elif choice == '3':
                display_winner_and_top_scorer(year)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
