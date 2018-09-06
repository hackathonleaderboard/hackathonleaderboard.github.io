fname = "FlexiRoute _ Devpost.htm"

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
isOnLikesYet = False
for i in range(len(content)):
    if(isOnLikesYet):
        break

    # Display Names of people
    if("<a class=\"user-profile-link\" href=" in content[i]):
        name = content[i].split("<a class=\"user-profile-link\" href=\"https://devpost.com/")[1].split("\"")[0]
        print(name)

    # Display Awards
    if("<span class=\"winner label radius small all-caps\">Winner</span>" in content[i]):
        name = content[i+1]
        print(name)

    if("<span class=\"like-counts\">" in content[i]):
        isOnLikesYet = True