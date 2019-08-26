"""
File: test.py
Author: Jens Petit
Email: petit.jens@gmail.com
Github: https://github.com/j-petit
Description: Class for
"""


def modelParse(filename):
    """Parses the standard mplus model into single lines. Model refers to the
    concept defined after the model: keyword in mplus.

    Each line of the model is translated into a lines with only one dependency.
    It looks for the line containing "model:" and start parsing there until the
    next empty line.

    Parameters
    ----------
    filename : The mplus model file to parse


    Returns
    -------
    new_lines : list of strings representing a single line of the model
    j : the line number where the model stopped

    """

    key_words = ['on', 'with']
    found_model = False

    with open(filename) as fp:

        new_lines = []

        model_line = 0

        for j, line in enumerate(fp):

            line = line.strip(None)

            if line.lower() == "model:":
                found_model = True
                continue

            if found_model:

                if line == "":
                    model_line = j
                    break

                line = line.rstrip(";")

                split_line = line.split(" ")

                if (("on" in line or "with" in line) and len(split_line) > 3):
                    if ("on" in line):
                        key_word = "on"
                    else:
                        key_word = "with"

                    index = split_line.index(key_word)

                    if index == 1:
                        r_list = split_line[2:]
                        for i in range(len(r_list)):
                            line = "{} {} {}".format(split_line[0], key_word, r_list[i])
                            new_lines.append(line)
                    else:
                        l_list = split_line[:index]
                        for i in range(len(l_list)):
                            line = "{} {} {}".format(l_list[i], key_word, split_line[-1])
                            new_lines.append(line)
                else:
                    new_lines.append(line)

        if not found_model:
            raise Exception("No model found in this file")

    return new_lines, j


def appendToFile(filename, model):
    """Appends a model to a file.

    Parameters
    ----------
    filename : string which specifies the path.

    model : mplus model object
    """

    with open(filename, 'a') as f:

        f.write(model.name + ":\n")
        for i, line in enumerate(model.model):
            if model.labels:
                f.write(line + " (" + model.labels[i] + ");\n")
            else:
                f.write(line + ";\n")

        f.write("\n")


def combineModels(model1, model2, label, same_indices):
    """Combines the labels of two model inplace.

    Parameters
    ----------
    model1 : mplus model object

    model2 : mplus model object

    label : string for the combined model parts

    same_indices : list of ints
    """

    for i, index in enumerate(same_indices):

        model1.labels[index] = label + str(i)
        model2.labels[index] = label + str(i)
