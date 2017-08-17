filename = "football-league-results.txt"

def leagueResult():
    with open(filename) as result:
        result.next()
        for team in result:
            team = team.split()
            print team

        pass



leagueResult()
