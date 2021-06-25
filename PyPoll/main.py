#import dependencies 
import csv

#import CSV
csv_filepath = './Resources/election_data.csv'

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



# This for loop iterates over the key,value pairings in the candidate dictionary
# And finds out who has the max popular votes, and then sets the winner based on that
    for (k, v) in candidate_dictionary.items():
        if (v > max_popular_votes) :
            max_popular_votes = v
            winner = k


print('Election Results')
print('-' * 25)
print(f'Total Votes: {total_votes}')
print('-' * 25)
# https://docs.python.org/3/library/string.html#format-string-syntax
# This is what I'm using to format these values down below 
print("Khan: {:.3f}% ({})".format(round(candidate_dictionary["Khan"]/total_votes * 100, 3), candidate_dictionary["Khan"]))
print("Correy: {:.3f}% ({})".format(round(candidate_dictionary["Correy"]/total_votes * 100, 3), candidate_dictionary["Correy"]))
print("Li: {:.3f}% ({})".format(round(candidate_dictionary["Li"]/total_votes * 100, 3), candidate_dictionary["Li"]))
print("O'Tooley: {:.3f}% ({})".format(round(candidate_dictionary["O'Tooley"]/total_votes * 100, 3), candidate_dictionary["O'Tooley"]))
print('-' * 25)
print(f'Winner: {winner}')
print('-' * 25)