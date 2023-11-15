#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getTotalGoals(team, year):
    # Write your code here
    home_match_url = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&team1=" + team

    home_match_response = requests.get(home_match_url)
    home_match_data = json.loads(home_match_response.content)

    current_page = 1
    total_pages = home_match_data['total_pages']

    total_goals = 0

    while current_page <= total_pages:
        home_match_url = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1={1}&page={2}".format(year,team,current_page)
        home_match_response = requests.get(home_match_url)
        home_match_data = json.loads(home_match_response.content)
        for match in home_match_data['data']:
            if match['team1'].lower() == team.lower():
                total_goals += int(match['team1goals'])
        current_page += 1


    away_match_url = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&team2=" + team

    away_match_response = requests.get(away_match_url)
    away_match_data = json.loads(away_match_response.content)

    current_page = 1
    total_pages = away_match_data['total_pages']

    while current_page <= total_pages:
        away_match_url = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team2={1}&page={2}".format(year,team,current_page)
        away_match_response = requests.get(away_match_url)
        away_match_data = json.loads(away_match_response.content)
        for match in away_match_data['data']:
            if match['team2'].lower() == team.lower():
                total_goals += int(match['team2goals'])
        current_page += 1

    return total_goals


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
