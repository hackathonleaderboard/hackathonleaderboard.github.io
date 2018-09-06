# Gets page contents
import urllib.request
import csv

proj_url = "https://devpost.com/software/pill-dispenser-leuqcb"

fp = urllib.request.urlopen(proj_url)
proj_mybytes = fp.read()
proj_mystr = proj_mybytes.decode("utf8")
fp.close()

proj_content = proj_mystr.split("\n")

# Makes sure names found are not in likes section
isOnLikesYet = False
# Prevent double printing
toggle = True
# The makes the Dict for this project
winner_info = {}
winner_info["Awards"] = []
winner_info["Members"] = []

# Goes through each line of projects url
for i in range(len(proj_content)):
    # Breaks if on likes
    if(isOnLikesYet):
        break

    # Display Hackathon
    if("Submitted to" in proj_content[i]):
        winner_info["Hackathon"] = proj_content[i+11].strip().split("<a href=\"")[1].split("\">")[1].split("</a>")[0]

    # Display Awards
    if("<span class=\"winner label radius small all-caps\">Winner</span>" in proj_content[i]):
        name = proj_content[i+1]
        winner_info["Awards"].append(name.strip())

    # Display Names of people
    if("<a class=\"user-profile-link\" href=" in proj_content[i]):
        name = proj_content[i].split("<a class=\"user-profile-link\" href=\"https://devpost.com/")[1].split("\"")[0]
        if(toggle == True):
            winner_info["Members"].append(name)
            toggle = False
        else:
            toggle = True

    if("<span class=\"like-counts\">" in proj_content[i]):
        isOnLikesYet = True

# Writes to csv
#writer.writerow(winner_info)
print(winner_info)
print()
