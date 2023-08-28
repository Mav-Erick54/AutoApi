import sys
import os
import time
import subprocess

st = time.time()

job_id = sys.argv[1]

# Set path for indexing of human genome
input_path = sys.argv[2] + "/" + "reference_index"

# Set the path to your input file
input_file = sys.argv[3]
x = os.listdir(input_file)

# Set the path to your output directory
output_dir = sys.argv[4]

# options list
optionlist = sys.argv[5]
opt_list = [we for we in optionlist.strip('[]').split(',')]

# Set the name of output filename 
output_filename = []
for i in x:
    output_filename.append(i.split(".")[0])

# Run hisat2 alignment
try:
    cmd = ""
    if len(x) == 2:
        if opt_list:
            fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
            cmd = f"hisat2 -x {input_path} -1 {input_file+'/'+x[0]} -2 {input_file+'/'+x[1]} -S {output_dir+'/'+output_filename[0]}.sam" +" "+ " ".join(fin_opt) + " " + "2>&1 | tee /home/ubuntu/Desktop/Mediomix/Tools_log/tool_logs.txt"
        else:
            cmd = f"hisat2 -x {input_path} -1 {input_file+'/'+x[0]} -2 {input_file+'/'+x[1]} -S {output_dir+'/'+output_filename[0]}.sam" + " " + "2>&1 | tee /home/ubuntu/Desktop/Mediomix/Tools_log/tool_logs.txt"
    elif len(x) == 1:
        if opt_list:
            fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
            cmd = f"hisat2 -x {input_path} -U {input_file+'/'+x[0]} -S {output_dir+'/'+output_filename[0]}.sam" + " " + " ".join(fin_opt) + " " + "2>&1 | tee /home/ubuntu/Desktop/Mediomix/Tools_log/tool_logs.txt"
        else:
            cmd = f"hisat2 -x {input_path} -U {input_file+'/'+x[0]} -S {output_dir+'/'+output_filename[0]}.sam" + " " + "2>&1 | tee /home/ubuntu/Desktop/Mediomix/Tools_log/tool_logs.txt"
    else:
        print("More than two files")
except Exception as e:
    print(e)
    
os.system(cmd.strip())

et = time.time()
tt = et - st

print("Total Time Taken by Process : ", tt, " sec")
