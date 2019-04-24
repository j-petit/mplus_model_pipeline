"""
File: pipeline.py
Author: Jens Petit
Email: petit.jens@gmail.com
Github: https://github.com/j-petit
Description: Full pipeline
"""

from mplus_model import MPlusModel
from model_utilities import appendToFile
from model_utilities import combineModels
from pipeline_utils import createDiffs
from pipeline_utils import filterDiffs
import subprocess
import copy

model = MPlusModel("data/model.inp")

male_model = copy.deepcopy(model)
male_model.name = "male model"
male_model.addModelLabel("m")

female_model = copy.deepcopy(model)
female_model.name = "female model"
female_model.addModelLabel("f")

# appendToFile("data/model.out", model)
# appendToFile("data/model.out", male_model)
# appendToFile("data/model.out", female_model)

createDiffs(male_model, female_model, "data/model.out")

same = filterDiffs(0.01, "data/model.out", "diff")

combineModels(female_model, male_model, "s", same)
createDiffs(male_model, female_model, "data/model.out")

appendToFile("data/model.out", female_model)
appendToFile("data/model.out", male_model)
# print(subprocess.check_output(['ls','-l']))
