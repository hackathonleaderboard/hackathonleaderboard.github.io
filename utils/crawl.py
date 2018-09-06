import urllib.request
import csv

# For counting the total number of winners
count = 0
# Checks if the page has no winners
isEndPage = False
# Starting page
page = 1
# Max page
maxPage = 2

with open('names.csv', 'w') as csvfile:
    fieldnames = ['Awards', 'Members', 'Hackathon']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Parcing Projects For Winning Projects Urls
    while(not isEndPage and page <= maxPage):
        # Gets page contents
        url = "https://devpost.com/software/search?page=" + str(page) + "&query=is%3Awinner"
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

        content = mystr.split("\n")

        # Looks for page with no content
        if("<p>Oh no! Looks like there&#39;s no software matching your query.</p>" in mystr):
            isEndPage = True

        # Goes through each line of html file
        for i in range(len(content)):
            if("<a class=\"block-wrapper-link fade link-to-software\" href=" in content[i]):

                # Parcing Project Urls For Names and Awards
                # Gets page contents
                proj_url = content[i].split("<a class=\"block-wrapper-link fade link-to-software\" href=\"")[1].replace("\">","")
                print(proj_url)
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
                writer.writerow(winner_info)
                print(winner_info)
                print()

                count = count + 1

        page = page + 1

print("Total:")
print(count)
