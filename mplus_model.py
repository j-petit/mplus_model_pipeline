"""
File: mplus_model.py
Author: Jens Petit
Email: petit.jens@gmail.com
Github: https://github.com/j-petit
Description: Class which contains mplus model
"""

from model_utilities import modelParse

class MPlusModel(object):

    """Defines an MPlus Model"""

    model = []
    is_diffed = False
    model_name = ""

    def __init__(self, filename, name=None):
        """Constructor creates model from file."""

        self.model = modelParse(filename)

        if name:
            model_name = name
        else:
            model_name = "model"
