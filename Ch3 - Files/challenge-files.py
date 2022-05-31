# Crete a dir
# Open / Create a file
# run OS commands like list dir shutils? 
# Close file

import os
import subprocess

def main():

    directory = "results"
    os.mkdir(directory)
    # os.rmdir(directory)

    with open(r'' + directory + '/list.txt', 'w') as f:
        subprocess.run(['find', '/"Ch3 - Files"', '-maxdepth', '1', '-type', 'f'], stdout=f)

if __name__ == "__main__":
    main()

