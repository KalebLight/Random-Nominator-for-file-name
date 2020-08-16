import os, random
dirs = os.listdir(".")

for file in dirs:    
    src = file
    newName = str(random.randint(1, 1000000))
    newName += '.mp3'
    os.rename(src, newName)
    