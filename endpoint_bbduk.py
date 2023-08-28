import sys
import os
import time
import subprocess

st = time.time()

job_id = sys.argv[1]

# Set the path to your input file
input_file = sys.argv[2]
x = os.listdir(input_file)

# Set the path to your output directory
output_dir = sys.argv[3]

# Set the name of output filename 
output_filename = []
for i in x:
    output_filename.append(output_dir + "/" + i.split(".")[0])

optionlist = sys.argv[4]
opt_list = [we for we in optionlist.strip('[]').split(',')]

# Run MultiQC using the conda installation
cmd = ""
if len(x) == 2:
    if opt_list:
        fin_opt = [rmopt.replace(":", "=") for rmopt in opt_list]
        cmd = f"bbduk.sh in1={input_file+'/'+x[0]} in2={input_file+'/'+x[1]} out1={output_filename[0]}.fq out2={output_filename[1]}.fq out2={output_filename[1]}.fq ref='/home/madmin/Desktop/Mediomix/adapters/adapters.fa'" + " " + " ".join(fin_opt) + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
    else:
        cmd = f"bbduk.sh in1={input_file+'/'+x[0]} in2={input_file+'/'+x[1]} out1={output_filename[0]}.fq out2={output_filename[1]}.fq out2={output_filename[1]}.fq ref='/home/madmin/Desktop/Mediomix/adapters/adapters.fa'" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
elif len(x) == 1:
    if opt_list:
        fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
        cmd = f"bbduk.sh in={input_file+'/'+x[0]} out={output_filename[0]}.fq ref='/home/madmin/Desktop/Mediomix/adapters/adapters.fa'" +" "+ " ".join(fin_opt)+ " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
    else:
        cmd = f"bbduk.sh in={input_file+'/'+x[0]} out={output_filename[0]}.fq ref='/home/madmin/Desktop/Mediomix/adapters/adapters.fa'" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
else:
    print("More than two files")

print(cmd)
os.system(cmd.strip())

et = time.time()
tt = et - st

print("Total Time Taken by Process : ", tt, " sec")
