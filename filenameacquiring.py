import glob
files = glob.glob("*/*.obj")
with open("existed.txt", "w") as f:
    for file in files:
        f.write(file + "\n")
