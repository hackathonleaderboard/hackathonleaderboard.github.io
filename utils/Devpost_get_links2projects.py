fname = "devpost_winners.htm"

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
for i in range(len(content)):
    if("<a class=\"block-wrapper-link fade link-to-software\" href=" in content[i]):
        name = content[i].split("<a class=\"block-wrapper-link fade link-to-software\" href=\"")[1].replace("\">","")
        print(name)