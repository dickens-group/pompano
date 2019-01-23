#!/usr/bin/env python3

import sys
# import matplotlib
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# import the venn functions
from matplotlib_venn import venn3


def load_file_to_list(filename):
    """ takes a single file and returns a list of the items
    assumes one ID per line in the file"""
    item_list = []
    with open(filename) as in_fh:
        for line in in_fh:
            item_list.append(line.strip())
    return item_list[:]


# load the input filenames from commandline
if len(sys.argv)>4:
    sys.exit("You gave too many filenames - your MUST give only 3")
elif len(sys.argv)<4:
    sys.exit("You gave too few filenames - your MUST give only 3")
else:
    (file1, file2, file3) = sys.argv[1:]


# load the data into lists
list1_augustus = load_file_to_list(file1)
list2_trinity = load_file_to_list(file2)
list3_turbot = load_file_to_list(file3)

print("List 1: {}".format(len(list1_augustus)))
print("List 2: {}".format(len(list2_trinity)))
print("List 3: {}".format(len(list3_turbot)))


# draw the venn
# TODO: make it take these names from the commandline too
venn3([set(list1_augustus), set(list2_trinity), set(list3_turbot)], set_labels = ("Augustus-Hints","Transcripts","Turbot"))
plt.title("Comparison of OrthoMCL Groups\n")
plt.show()
#plt.savefig("venn.png", width=10, height=10, dpi=300)
