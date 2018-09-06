import csv

file_name = '2018_22_7_Crawl_1.csv'
score = {}
with open(file_name, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        numAwards = len(row['Awards'].split(", "))
        #hackathonName = row['Hackathon']
        members = row['Members'].replace("[","").replace("]","").replace("'","").split(", ")
        for member in members:
            if(member in score):
                score[member] = score[member] + numAwards
                if(member == "zenesys"):
                    print(score[member])
            else:
                score[member] = numAwards

sorted_score = sorted(score.items(), key=lambda kv: kv[1])
#print(sorted_score)

import pyrebase

config = {
  "apiKey": "AIzaSyA4n_Oc42SxtuvYctlu_P-BBsgthBedrYw",
  "authDomain": "hackathonranker.firebaseapp.com",
  "databaseURL": "https://hackathonranker.firebaseio.com",
  "storageBucket": "hackathonranker.appspot.com"
}

#firebase = pyrebase.initialize_app(config)

#db = firebase.database()

rank = 0
num = 1
last_score = -1
with open('data.csv', 'w') as csvfile:
    fieldnames = ['Rank','User', 'Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    top_100 = sorted_score
    top_100.reverse()
    top_100 = top_100[:101]
    for pair in top_100:
        if pair[0] != "":
            #db.child("Scores/" + pair[0]).set(pair[1])
            nrow = {}

            if(last_score != pair[1]):
                rank = num

            nrow['Rank'] = rank
            nrow['User'] = pair[0]
            nrow['Score'] = pair[1]

            num = num + 1
            last_score = pair[1]
            

            writer.writerow(nrow)

print(sorted_score[-100:])
print(len(sorted_score))
