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

    for row in reader:
        total_votes += 1
        candidates_name = row[2]
        # This uses each candidates name as a key to attach values
        # If the candidates name is present on the candidate_dictionary, it will increment the corresponding value by 1
        
        candidate_dictionary[candidates_name] = candidate_dictionary.get(candidates_name, 0) + 1
