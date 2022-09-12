from functools import lru_cache
import csv


@lru_cache
def read(path):
    new_list = []
    with open(path) as file:
        file_list = csv.DictReader(file)
        for jobs in file_list:
            new_list.append(jobs)
    return new_list
