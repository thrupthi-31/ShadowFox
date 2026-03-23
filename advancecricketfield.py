import pandas as pd
data = [
    # Match, Innings, Team, Player, Over, Ball, Position, Pick, Throw, Runs
    [1, 1, "RCB", "Virat Kohli", 5, 2, "Cover", "Clean Pick", "None", 2],
    [1, 1, "RCB", "Virat Kohli", 7, 4, "Cover", "Fumble", "None", -1],
    [1, 1, "RCB", "Faf du Plessis", 10, 3, "Long-off", "Catch", "None", 0],
    [1, 1, "RCB", "Glenn Maxwell", 12, 5, "Point", "Clean Pick", "Run Out", 1],
    [1, 1, "RCB", "Glenn Maxwell", 14, 1, "Point", "Drop Catch", "None", -2],
]
columns = [
    "Match", "Innings", "Team", "Player",
    "Over", "Ball", "Position", "Pick", "Throw", "Runs"
]
df = pd.DataFrame(data, columns=columns)
weights = {
    "Clean Pick": 1,
    "Good Throw": 1,
    "Catch": 5,
    "Drop Catch": -5,
    "Run Out": 6,
    "Missed Run Out": -3,
    "Direct Hit": 4
}
players = df["Player"].unique()
results = []
for player in players:
    player_df = df[df["Player"] == player]
    CP = (player_df["Pick"] == "Clean Pick").sum()
    GT = (player_df["Pick"] == "Good Throw").sum()
    C = (player_df["Pick"] == "Catch").sum()
    DC = (player_df["Pick"] == "Drop Catch").sum()
    RO = (player_df["Throw"] == "Run Out").sum()
    MRO = (player_df["Throw"] == "Missed Run Out").sum()
    DH = (player_df["Throw"] == "Direct Hit").sum()
    RS = player_df["Runs"].sum()
    PS = (
        CP * weights["Clean Pick"] +
        GT * weights["Good Throw"] +
        C * weights["Catch"] +
        DC * weights["Drop Catch"] +
        RO * weights["Run Out"] +
        MRO * weights["Missed Run Out"] +
        DH * weights["Direct Hit"] +
        RS
    )
    results.append([player, CP, GT, C, DC, RO, MRO, DH, RS, PS])
result_df = pd.DataFrame(results, columns=[
    "Player", "CP", "GT", "C", "DC",
    "RO", "MRO", "DH", "Runs Saved", "Performance Score"
])
print("\n🏏 Fielding Performance Summary:\n")
print(result_df)
result_df.to_excel("fielding_analysis.xlsx", index=False)

print("\nData saved to 'fielding_analysis.xlsx'")