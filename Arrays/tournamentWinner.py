HOME_WINNING_TEAM = 1
def tournamentWinner(competitions, results):
    #O(N)TS.
    currentBestTeam = ''
    scores = {currentBestTeam : 0}
    for i in range(len(competitions)):
        result = results[i]
        homeTeam ,awayTeam = competitions[i]
        winningTeam = homeTeam if result == HOME_WINNING_TEAM else awayTeam
        updateScores(winningTeam , 3 , scores)
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam

def updateScores(team , points , scores):
    scores[team]=scores.get(team , 0) + points