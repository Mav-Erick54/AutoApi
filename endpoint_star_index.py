import sys
import os
import time
import subprocess

st = time.time()

job_id = sys.argv[1]

# Set the path to your input file
input_file = sys.argv[2]

# Set the path to your output directory
output_dir = sys.argv[3]

# list of options
optionlist = sys.argv[4]
opt_list = [we for we in optionlist.strip('[]').split(',')]

# Run star command
cmd = ""
if opt_list:
    fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
    cmd = f"STAR --runMode genomeGenerate --genomeDir {output_dir} --genomeFastaFiles {input_file}" + " " + " ".join(fin_opt) + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
else:
    cmd = f"STAR --runMode genomeGenerate --genomeDir {output_dir} --genomeFastaFiles {input_file}" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"

print(cmd)
os.system(cmd.strip())
# subprocess.run(["STAR", "--runMode", "genomeGenerate", "--genomeDir", output_dir, "--genomeFastaFiles", input_file, "--genomeSAindexNbases", "3"])

et = time.time()
tt = et - st

print("Total Time Taken by Process : ", tt, " sec")
