with open('input.txt') as file:
    lines = file.read().strip().split('\n')


def isReportSafe(report):
    diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    if set(diff) <= {1, 2, 3} or set(diff) <= {-1, -2, -3}:
        return True
    return False

reports = [[int(data) for data in line.split(" ")] for line in lines]


safeReportCount = sum([isReportSafe(report) for report in reports])
print("Part 1:", safeReportCount)

safeReportCount = sum([any([isReportSafe(report[:i] + report[i + 1:]) for i in range(len(report))]) for report in reports])
print("Part 2:", safeReportCount)





    
    
