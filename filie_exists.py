import os
 
# todo check for existing file.
if os.path.isfile('./PBIOutput.txt'): # check to see if file exists
    data = open('./gradebook.dat', 'rb') # if file exists open, read all data.
    data.close()
else:
    print("The file gradebook.dat was not found.\n")
    print("We will create one....\n")