from pathlib import Path

myfile = Path("/Users/sahilnagpal/Desktop/Resume/sahilNagpal.pdf")
if(myfile.exists()):
    print("Yes Exist")
else:
    print("Not exist")
