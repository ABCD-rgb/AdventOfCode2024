def day2Part1(reports):
    # mark reports as either safe or unsafe
    # a report only counts as safe if both of the following are true:
        # The levels are either all increasing or all decreasing.
        # Any two adjacent levels differ by at least one and at most three.
    unsafe = 0
    for i in range(len(reports)):
        for j in range(len(reports[i])-1):   # use len - 1 to avoid index out of range (since we're comparing i with i+1)
            # print(j)
            # asc
            if reports[i][0] < reports[i][1]:
                # print(f"\t {reports[i][j]} {reports[i][j+1]}: {abs(reports[i][j+1] - reports[i][j])}")
                if (reports[i][j] > reports[i][j+1]) or abs(reports[i][j+1] - reports[i][j]) < 1 or abs(reports[i][j+1] - reports[i][j]) > 3:
                        unsafe += 1
                        break
            # desc
            else:
                # print(f"\t {reports[i][j]} {reports[i][j+1]}: {abs(reports[i][j+1] - reports[i][j])}")
                if (reports[i][j] < reports[i][j+1]) or abs(reports[i][j+1] - reports[i][j]) < 1 or abs(reports[i][j+1] - reports[i][j]) > 3:
                        unsafe += 1
                        break

    # total safe reports
    return len(reports) - unsafe


def day2Part2(reports):
    def is_safe(report):
        """Helper function to check if a report is safe."""
        ascending = report[0] < report[1]
        for i in range(len(report) - 1):
            if ascending:
                if report[i] > report[i + 1] or abs(report[i + 1] - report[i]) < 1 or abs(report[i + 1] - report[i]) > 3:
                    return False
            else:
                if report[i] < report[i + 1] or abs(report[i + 1] - report[i]) < 1 or abs(report[i + 1] - report[i]) > 3:
                    return False
        return True

    safe_count = 0

    for report in reports:
        if is_safe(report):
            safe_count += 1
        else:
            # Try removing each level (one at a time) to see if the report becomes safe
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]  # Remove the i-th level
                if is_safe(modified_report):
                    safe_count += 1
                    break  # No need to check further; it's safe with one removal

    return safe_count


reports = []
for line in open("2.txt"):
     reports.append(list(map(int, line.split())))
         

print(day2Part1(reports))   # 242
print(day2Part2(reports))   # 311
