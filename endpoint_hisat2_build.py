import sys
import os
import time
import subprocess

st = time.time()

job_id = sys.argv[1]

# # Set the path to your input file
input_file = sys.argv[2]

# Set the path to your output directory
output_dir = sys.argv[3] + "/reference_index"

# option list
optionlist = sys.argv[4]
opt_list = [we for we in optionlist.strip('[]').split(',')]

try:
    cmd = ""
    if opt_list:
        try:
            fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
            cmd = f"hisat2-build {input_file} {output_dir}" + " " + " ".join(fin_opt) + " " + "2>&1 | tee /home/ubuntu/Desktop/Mediomix/Tools_log/tool_logs.txt"
            os.system(cmd.strip())
        except Exception as e:
            print(e)
    else:
        cmd = f"hisat2-build {input_file} {output_dir}" + " " + "2>&1 | tee /home/ubuntu/Desktop/Mediomix/Tools_log/tool_logs.txt"
        os.system(cmd.strip())
except Exception as e:
    print(e)

et = time.time()
tt = et - st

print("Total Time Taken by Process : ", tt, " sec")
