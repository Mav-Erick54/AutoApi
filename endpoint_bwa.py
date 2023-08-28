import os
import sys
import time
import subprocess

st = time.time()

job_id = sys.argv[1]

# input files
input_file = sys.argv[2]

# output dir 
output_dir = sys.argv[3]

# list of options
optionlist = sys.argv[4]
opt_list = [we for we in optionlist.strip('[]').split(',')]

# run the command for bwa
cmd = ""
if opt_list:
    fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
    cmd = f"bwa index {input_file}" + " " + " ".join(fin_opt) + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
else:
    cmd = f"bwa index {input_file}" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
    
os.system(cmd.strip())
et = time.time()
tt = et - st

print("Total Time Taken by Process : ", tt, " sec")
