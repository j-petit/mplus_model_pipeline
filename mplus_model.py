"""
File: mplus_model.py
Author: Jens Petit
Email: petit.jens@gmail.com
Github: https://github.com/j-petit
Description: Class which contains mplus model
"""

from model_utilities import modelParse

class MPlusModel(object):

    """Defines an MPlus Model.

    Parameters
    ----------
    is_diffed: Boolean indicating if a diff has happened

    labels : list containing the label for each line

    name : string naming the model

    model : list of strings for each line

    """


    def __init__(self, filename, name=None):
        """Constructor creates model from file.

        Parameters
        ----------
        filename : string

        name : string written to member self.name
        """

        self.is_diffed = False
        self.labels = []

        self.model, self.line_no = modelParse(filename)

        if name:
            self.name = name
        else:
            self.name = "model"


    def addModelLabels(self, labels):
        """Adds labels when all are explicitely specified

        Parameters
        ----------
        labels : list of strings
        """

        if len(labels) != len(self.model):
            raise Exception("Lengths of labels must match model")

        self.labels = labels


    def addModelLabel(self, label):
        """Labels of lines given only single label.

        Automatically adds numbers to the label.

        Parameters
        ----------
        label : string
        """

        if len(self.labels) == 0:
            new_fill = True
        else:
            new_fill = False

        for i, line in enumerate(self.model):

            if new_fill:
                self.labels.append(label + str(i))
            else:
                self.labels[i] = label + str(i)
