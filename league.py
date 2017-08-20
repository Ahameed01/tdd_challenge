docname = "football-league-results.txt"
def footballLeagueResult():
	with open(docname) as results:
		results.next()
		goalDifference = []
		clubNamesList = []
		for team in results:
			team = team.split()
			clubNames = []
			clubData = []

			for data in team:
				try:
					data = int(data)
					clubData.append(data)
				except ValueError:
					stringData = str(data)
					if stringData != "-":
						clubNames.append(stringData)
					pass
			if len(clubData) > 0:
				goalFor = int(clubData[4])
				goalAgainst = int(clubData[5])
				del clubNames[:1]
				clubNames = ' '.join(clubNames)
				clubNamesList.append(clubNames)
				goalDifference.append(goalFor - goalAgainst)

		teamGoalPerformance = dict(zip(clubNamesList,goalDifference))
		lowestDiffTeam = min(sorted(teamGoalPerformance.keys()))
		lowestDiffScore = min(sorted(teamGoalPerformance.values()))


        print (str(lowestDiffTeam) + ' with ' + str(lowestDiffScore) + " goal difference is the team with the smallest difference in 'for' and 'against' goals")


footballLeagueResult()
