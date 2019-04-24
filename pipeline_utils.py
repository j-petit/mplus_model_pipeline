"""
File: pipeline_utils.py
Author: Jens Petit
Email: petit.jens@gmail.com
Github: https://github.com/j-petit
Description: Utility functions for filtering models
"""


def createDiffs(groups, no_diffs):
    lines = []
    start_line = "new(diff1-diff{});".format(no_diffs)

    for i in range(1, no_diffs + 1):
        
        line = "diff{0} = b{1}{2} - b{3}{4};".format(i, "m", i, "f", i)
        lines.append(line)
        print(line)

    return lines

def filterDiffs(threshold, filename, var_name):

    to_match = '^' + var_name.upper()
    match_counter = 0

    same_paths = []
    
    with open(filename) as fp:
        

        for line in fp:
            line = line.strip(None)


            if re.match(to_match, line):
                match_counter = match_counter + 1
                value = float(line.split()[4])

                if value < threshold:

                    same_paths.append(match_counter)
                    print(line)
                    print(match_counter)

    return same_paths
