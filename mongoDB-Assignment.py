import pymongo
import json


#calculations

    #opening json file
with open("example_tim_data.json") as amy:
    data = json.load(amy)
all_matches = data


class Team:
    def __init__(self, team_number):
        self.team_number = int(team_number)
    def find_matches(self):
        matches = []
        for match in all_matches:
            if match["team_num"] == self.team_number:
                matches.append(match)
        return matches
    def find_average_score(self):
        matches = self.find_matches()
        total_score = 0
        num_of_matches = 0
        for i in matches:
            score = i["num_balls"]
            total_score += score
            num_of_matches += 1
        average = total_score/num_of_matches
        return average
    def least_balls_scored(self):
        matches = self.find_matches()
        ball_nums = []
        for i in matches:
            ball_nums.append(i["num_balls"])
        least = min(ball_nums)
        return least      
    def most_balls_scored(self):
        matches = self.find_matches()
        ball_nums = []
        for i in matches:
            ball_nums.append(i["num_balls"])
        most = max(ball_nums)
        return most      
    def amount_of_matches(self):
        matches=self.find_matches()
        return len(matches)
    def percentage_climbed(self):
        matches=self.find_matches()
        fs=[]
        filtered=[]
        for total in matches:
            fs.append(total["climbed"])
        for thing in fs:
            if thing == True:
                filtered.append(thing)
        sum_matches=len(fs)
        success=len(filtered)
        real=100*(success/sum_matches)
        return real




            

alison = input("Pick a team >>")
team = Team(int(alison))
team.find_matches()
print("Average score is: " + str(team.find_average_score()))
print("Least balls scored: " + str(team.least_balls_scored()))
print("Most balls scored: " + str(team.most_balls_scored()))
print("Amount of matches played: " + str(team.amount_of_matches()))
print("Percentage climbed: " + str(team.percentage_climbed()))