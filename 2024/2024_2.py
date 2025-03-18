#!/bin/bash

from typing import List


def get_data(file: str) -> List:
    report_list = []
    with open(file, 'r') as f:
        while line := f.readline():
            report = [int(x) for x in line.split()]
            report_list.append(report)

    return report_list


def is_safe(report: List) -> bool:
    if all(report[i] <= report[i+1] for i in range(len(report)-1)) or all(report[i] >= report[i+1] for i in range(len(report)-1)):
        # two adjacent levels in a report differ by at least 1 and at most 3
        if all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1)):
            return True
    return False


def get_safe_reports(reports: List) -> int:
    safe_reports = 0

    for report in reports:
        if is_safe(report):
            safe_reports = 1 + safe_reports

    return safe_reports


def is_safe_with_removal(report: List) -> bool:
    if is_safe(report):
        return True
    else:
        for i in range(len(report)):
            # remove the ith level and check if safe
            new_report = report[:i] + report[i+1:]
            if is_safe(new_report):
                return True
        return False


def get_safe_reports_with_removal(reports: List) -> int:
    safe_reports = 0

    for report in reports:
        if is_safe_with_removal(report):
            safe_reports = 1 + safe_reports

    return safe_reports


reports = get_data("./inputs/2024_2")

print(get_safe_reports(reports))

print(get_safe_reports_with_removal(reports))
