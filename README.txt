
First create a conda environment with the correct python modules:
conda create -n venn -y matplotlib matplotlib-venn

Acitvate the environment:
source activate venn

Make the python script executable:
chmod +x make_venn_from_files.py

Run the python script with the 3 filenames:
./make_venn_from_files.py list1.txt list2.txt list3.txt
