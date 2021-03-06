"""
File: pipeline_utils.py
Author: Jens Petit
Email: petit.jens@gmail.com
Github: https://github.com/j-petit
Description: Utility functions for filtering models
"""

import re


def createDiffs(model1, model2, filename):
    """Takes two models and creates constraint variables out of their paths.

    Parameters
    ----------
    model1 : mplus model object

    model2 : mplus model object

    filename : string where to write diffs
    """

    if len(model1.model) != len(model2.model):
        raise Exception("Models not the same")

    no_lines = len(model1.model)
    not_diffs = 0

    for i in range(no_lines):
        if model1.labels[i] == model2.labels[i]:
            not_diffs = not_diffs + 1

    lines = []

    start_line = "new(diff0-diff{});".format(no_lines - not_diffs - 1)

    counter = 0
    for i in range(no_lines):

        if model1.labels[i] == model2.labels[i]:
            line = "diffX = {1} - {2};".format(i, model1.labels[i],
                                             model2.labels[i])
            line = "! " + line
        else:
            line = "diff{0} = {1} - {2};".format(counter, model1.labels[i],
                                             model2.labels[i])
            counter = counter + 1

        lines.append(line)

    with open(filename, 'a') as f:

        f.write("MODEL CONSTRAINT:\n")
        f.write(start_line + "\n")

        for line in lines:
            f.write(line + "\n")


def filterDiffs(threshold, filename, var_name):
    """Searches for lines starting with var_name in file and indexes them.

    Parameters
    ----------
    threshold : float indicating which lines to consider

    filename : string specifying file

    var_name : string to search for in file
    """

    to_match = '^' + var_name.upper()
    match_counter = 0

    same_paths = []

    with open(filename) as fp:

        for line in fp:
            line = line.strip(None)

            if (line == "New/Additional Parameters"):
                found = True

            if (line == ""):
                found = False

            if (re.match(to_match, line) and found):
                value = float(line.split()[4])

                if value < threshold:

                    same_paths.append(match_counter)

                match_counter = match_counter + 1
    return same_paths
