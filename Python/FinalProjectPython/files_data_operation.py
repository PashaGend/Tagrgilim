import scanning_folders_files3 as sff
import json

directory_path = '/Users/gnpavel/Documents/'
files_info = sff.get_files_info(directory_path)


def get_biggest_directories(files_And_folders):
    folders_dict = {}
    for f_key,f_value in files_info.items():
        if f_value['is_directory'] == True:
         folders_dict[f_key] = f_value
    biggest_dirs = sorted(folders_dict.items(),key = lambda x:x[1]['size'], reverse=True)

    return biggest_dirs[:5]

print_info_report = "5 biggest directories:"
sorted_biggest_folders = get_biggest_directories(files_info)
sorted_biggest_folders.insert(0, print_info_report)


def get_biggest_files(files_And_folders):
    files_dict = {}
    for f_key,f_value in files_info.items():
        if f_value['is_directory'] == False:
         files_dict[f_key] = f_value
    biggest_files = sorted(files_dict.items(),key = lambda x:x[1]['size'], reverse=True)

    return biggest_files[:5]


print_info_report = "5 biggest files:"
sorted_biggest_files = get_biggest_files(files_info)
sorted_biggest_files.insert(0, print_info_report)

def get_newest_files(files_And_folders):
    files_dict = {}
    for f_key,f_value in files_info.items():
        if f_value['is_directory'] == False:
         files_dict[f_key] = f_value

    result_newest = sorted(files_dict.items(),key = lambda x:x[1]['time'] ,reverse=True)
    return result_newest[:5]

print_info_report = "5 newest files:"
result_newest_files = get_newest_files(files_info)
result_newest_files.insert(0, print_info_report)

#print example in json format: print("5 newest files:",json.dumps(result_newest_files,sort_keys=True, indent=2))
