TextFile = "names.txt"
IGN = "IanTheWrong"
found = False

with open(TextFile, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if IGN.lower() in line.lower():
            print(f"Match found: {line}")
            found = True
    if(found==False):
        print("Not whitelisted Yet");
