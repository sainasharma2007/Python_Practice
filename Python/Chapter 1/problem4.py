# import module
import os
# make dir path
directory_path = "/"
# check 
if os.path.exists(directory_path):
    print("Contents of the directory:")
    for item in os.listdir(directory_path):
        print(item)
else:
    print("Directory does not exist.")

# used os as a built-in module
