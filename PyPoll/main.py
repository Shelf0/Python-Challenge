#import dependencies 
import csv

#import CSV
csv_filepath = './election_data.csv'

#setting Variables
candidate_dictionary = {}
total_votes = 0
max_popular_votes = 0
winner = ""

# Open & Use CSV

with open(csv_filepath) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
