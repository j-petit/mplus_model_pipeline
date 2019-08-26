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
import os
import copy

# the model is converted into only one to one correspondencies. the path is
# relative to the python script
mplus_input = "data/model.inp"
mplus_input_trunk = mplus_input.split(".")
mplus_out = mplus_input_trunk[0] + ".out"

print("I will generate the new input in:")
print(mplus_input)
print("I will read the output of:")
print(mplus_out)

model = MPlusModel(mplus_input)

# a model for one group is created
male_model = copy.deepcopy(model)
male_model.name = "MODEL MALE"
male_model.addModelLabel("m")

# a model for another group is created
female_model = copy.deepcopy(model)
female_model.name = "MODEL FEMALE"
female_model.addModelLabel("f")

print("I will now append the group models and diffs to the input file.")
# the newly created models are appended to the mplus script
appendToFile(mplus_input, model)
appendToFile(mplus_input, male_model)
appendToFile(mplus_input, female_model)

# the diffs between the two models are created and appended to the file
createDiffs(male_model, female_model, mplus_input)

input("Now run MPlus with the generated input and press Enter to continue...")

# This line probably doesn't work on a windows machine. It runs mplus
# os.system('mpdemo ' + mplus_input);
# after running mplus, the output is filtered for diffs which have a
# significance greater than the threshold value 0.01

same = filterDiffs(0.05, mplus_out, "diff")

# where the diff is not significant drop the different paths
combineModels(female_model, male_model, "s", same)

# write the newly created models to files
appendToFile(mplus_input, male_model)
appendToFile(mplus_input, female_model)

# this will only create diffs where the labels are different.
createDiffs(male_model, female_model, mplus_input)

input("Modified the input based on the p-value of the diffs. You can run mplus again. Press Enter to exit...")
