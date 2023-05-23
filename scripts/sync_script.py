import os
import random
import shutil
import string
import time

import schedule
from dirsync import sync

# Create directories.
source_directory = "source_directory"
replica_directory = "replica_directory"
parent_directory = "C:/Users/cretz/PycharmProjects/TestTask"
source_path = os.path.join(parent_directory, source_directory)
replica_path = os.path.join(parent_directory, replica_directory)

# Check if directories already exist.
if os.path.isdir(source_path):
    print("Source directory already exists!")
else:
    os.mkdir(source_path)

if os.path.isdir(replica_path):
    print("Replica directory already exists!")
else:
    os.mkdir(replica_path)

# Add files to directories.
file_name = random.choice(string.ascii_lowercase)
with open(f'../source_directory/{file_name}.txt', 'w') as fp:
    fp.write('Test')
    pass
print(f"File {file_name} created in the source directory!")

file_name = random.choice(string.ascii_lowercase)
with open(f"../replica_directory/{file_name}.txt", 'w') as fp:
    fp.write('Test')
    pass
print(f"File {file_name} created in the replica directory!")

# Delete files from replica directory.
files = [f for f in os.listdir(replica_path)]
for f in files:
    os.remove(os.path.join(replica_path, f))
print("Files from replica_folder deleted.")

# Add files from source directory to replica directory.
sync(source_path, replica_path, 'sync', verbose=True)

# Teardown - delete directories.
shutil.rmtree(source_path)
shutil.rmtree(replica_path)

#schedule.every(3).seconds.do(sync_folders_script)
#while True:
#    schedule.run_pending()
#    time.sleep(1)
