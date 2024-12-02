from utils.api import get_input

input_str = get_input(2)

# WRITE YOUR SOLUTION HERE

def check_report(report):
    safe = False
    if report == sorted(report) or report == sorted(report,reverse=True):
        safe = True
        for idx,level in enumerate(report):
            
            if idx != len(report)-1:
                variance = abs(int(report[idx+1]) - int(level))
                if variance < min_threshold or variance > max_threshold:
                    safe = False
                    break
    return safe

lines = input_str.splitlines()

reports = []
for line in lines:
    reports.append(list(map(int, line.split())))
safe_count = 0
min_threshold = 1
max_threshold = 3

# Part 1

for report in reports:
    if check_report(report):
        safe_count += 1     

print(f"Day 1 Part 1: {safe_count}")

# Part 2
safe_count = 0

for report in reports:
    if check_report(report):
        safe_count += 1
    else:
        for i in range(len(report)):
            temp_report = report.copy()
            del temp_report[i]
            if check_report(temp_report):
                 safe_count += 1
                 break

print(f"Day 1 Part 2: {safe_count}")