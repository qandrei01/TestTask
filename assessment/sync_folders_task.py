import threading

from methods import *


def sync_folders():
    threading.Timer(3, sync_folders).start()
    create_directories()
    add_files()
    clear_replica_directory()
    copy_files()


sync_folders()
