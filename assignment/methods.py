import logging
import os
import random
import shutil
import sys

# Setup logger to view logs in file and console output.
root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
logging.basicConfig(filename='logfile.log',
                    format='%(asctime)s %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)
root.addHandler(handler)

# Define directories paths.
source_directory = "source_directory/"
replica_directory = "replica_directory/"
parent_directory = os.getcwd()
source_path = os.path.join(parent_directory, source_directory)
replica_path = os.path.join(parent_directory, replica_directory)


def create_directories():
    # Create directories if not already created.
    if os.path.isdir(source_path):
        logging.info(f"Source directory already exists in '{parent_directory}'!")
    else:
        os.mkdir(source_path)
        logging.info(f"Source directory created in '{parent_directory}'!")

    if os.path.isdir(replica_path):
        logging.info(f"Replica directory already exists in '{parent_directory}'!")
    else:
        os.mkdir(replica_path)
        logging.info(f"Replica directory created in '{parent_directory}'!")


def add_files():
    # Add files to source directory.
    for i in range(1, 4):
        created_file_name = (random.choice(range(100, 999)))
        with open(f'{source_path}/{created_file_name}.txt', 'w') as fp:
            fp.write('Text inside file.')
            pass
        logging.info(f"File {created_file_name} created in '{source_path}'!")


def clear_replica_directory():
    # Delete files from replica directory.
    files = [f for f in os.listdir(replica_path)]
    for f in files:
        os.remove(os.path.join(replica_path, f))
    logging.info("Content of replica directory cleared!")


def copy_files():
    # Copy files from source directory to replica directory.
    files = os.listdir(source_path)
    for file_name in files:
        shutil.copy(source_path + file_name, replica_path + file_name)
    logging.info(f"{files} copied from '{source_path}' to '{replica_path}' successfully!")
