import os
import random


def get_files_info(directory,files_folders_dict = {}):
    for entry in os.scandir(directory):
        myPath = entry.path
        if entry.is_file():
            results = entry.stat()
            result_files = {
            'name': entry.name,
            'size': results.st_size,
            'time': results.st_ctime,
            'is_directory': os.path.isdir(entry)
            }
            files_folders_dict[myPath] = result_files

        elif entry.is_dir():
            get_files_info(entry.path, files_folders_dict)
            results = entry.stat()
            result_folders = {
            'name': entry.name,
            'size': results.st_size,
            'time': results.st_ctime,
            'is_directory': os.path.isdir(entry)
            }
            files_folders_dict[myPath] = result_folders
    return files_folders_dict
