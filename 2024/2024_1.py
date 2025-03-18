#!/bin/bash
from typing import List

def populate_data_to_list(file: str) -> List:
    left_list = []
    right_list = []
    with open(file, 'r') as f:
        while line := f.readline():
            ids = line.split()
            left_list.append(int(ids[0]))
            right_list.append(int(ids[1]))
    return [left_list, right_list]

def sort(arr: List) -> List:
    return sorted(arr)

def calculate_distance():
    left_list, right_list = populate_data_to_list('./inputs/2024_1')
    sorted_left_list = sort(left_list)
    sorted_right_list = sort(right_list)

    sum = 0
    for i in range(len(sorted_left_list)):
        sum = sum + abs(sorted_left_list[i] - sorted_right_list[i])

    print(sum)

# calculate_distance()

def create_hash(input_list: List) -> dict:
    hash_of_list = {}
    for item in input_list:
        hash_of_list[item] = hash_of_list.get(item, 0) + 1
    
    return hash_of_list

def calculate_similarity_score():
    left_list, right_list = populate_data_to_list("./inputs/2024_1")
    hash_right_side = create_hash(right_list) 
    
    score = 0
    for item in left_list:
        if item in hash_right_side:
            score = score + item * hash_right_side[item]

    print(score)

calculate_similarity_score()
