import files_data_operation as fdo
import json


def create_report():
    list_str = '\n'.join(map(str,
    fdo.sorted_biggest_files +
    fdo.sorted_biggest_folders +
    fdo.result_newest_files))
    with open('report.txt', 'w') as file:
      file.write(list_str)
    print("report saved to file successfully!")
