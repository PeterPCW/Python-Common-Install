import fileinput
import xmlrpc.client
import re
import time
import os
from datetime import datetime

start_time = datetime.now().strftime("%H:%M:%S")

# Replace all occurrences of "==" with ">=" in "requirements.txt" before describing so that requirements.txt_backup gets that reformatting too
with fileinput.FileInput("requirements.txt", inplace=True) as file:
    for line in file:
        print(line.replace("==", ">="), end="")

input_filename = "requirements.txt"
output_filename = "output.txt"

pypi = xmlrpc.client.ServerProxy("https://pypi.python.org/pypi")

# open the input file and create the output file
with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    
    # set expectations
    print("################################################\n")
    print("\n#\n###   with the default file (~250 lines) this will take ~8 minutes to complete due to rate limits")
    print("###   Started:", start_time)
    print("\n#\n###   only every 7th package will be printed to balance brevity with frequent updates")
    print("###   packages are in alphabetical order after a `freeze`\n#\n#")
    print("###   use Ctrl+C to cancel at any time - requirements.txt will be unchanged")
    print("###   if you cancel, you will need to delete output.txt manually\n#\n#")
    print("################################################\n")
    
    # write preamble to file
    output_file.write('################################################\n#                                              #\n#   This is a generalized requirements.txt     #\n#   to install common packages for python      #\n#   development. I will add packages as I      #\n#   need them. Using >= allows for forward     #\n#   compatibility to always install newest.    #\n#                                              #\n#   Use: "pip install -U -r requirements.txt"  #\n#                                              #\n#   Then: "pip freeze > requirements.txt"      #\n#   to update, but afterward you have to       #\n#   Find -> Replace All ">=" with ">="         #\n#   or run `DescribePackagesAndReformat.py`.   #\n#                                              #\n################################################\n\n')
    
    # loop through each line in the input file
    for i, line in enumerate(input_file):
        # skip any lines at the top of the file that start with '#'
        if not line.strip() :
            continue
        if "#" in line :
            continue
        if i != 0 and i % 28 == 0:
            print("\nrate limit wait\n")
            # wait a longer time for the 60-sec rate limit of xmlrpc
            time.sleep(30)
        if i % 7 == 0 :
            print(line.strip())
        
        # wait to not be rate limited by xmlrpc (one request per second)
        time.sleep(1)
        
        # find the package name and version string using a regex
        package_name, version_string = line.split(">=")
        package_name = package_name.strip()
        version_string = version_string.strip()
        # look up package metadata from PyPI
        package_metadata = pypi.release_data(package_name, version_string)
        package_summary = package_metadata.get("summary", "")
        # add summary to line
        line = f"{package_name} >= {version_string}       #### {package_summary}"
        # write updated line to output file
        output_file.write(line + "\n")

# remove an old backup file if it exists
if os.path.exists(input_filename + "_backup"):
    os.remove(input_filename + "_backup")

# rename the input file to have a "_backup" suffix
os.rename(input_filename, input_filename + "_backup")

# rename the output file to have the input file name
os.rename(output_filename, input_filename)

end_time = datetime.now().strftime("%H:%M:%S")
print("\nEnded:", end_time)