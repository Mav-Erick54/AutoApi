import os
import sys
import time
import subprocess

st = time.time()

job_id = sys.argv[1]

input_path = sys.argv[2]

input_file = sys.argv[3]
x = os.listdir(input_file)

output_dir = sys.argv[4]

optionlist = sys.argv[5]
opt_list = [we for we in optionlist.strip('[]').split(',')]

output_filename = []
for i in x:
    output_filename.append(output_dir + "/" + i.split(".")[0])

# run command for bwa mem
cmd = ""
if len(x) == 2:
    if opt_list:
        fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
        cmd = f"bwa mem {input_path} {input_file+'/'+x[0]} {input_file+'/'+x[1]} -o {output_filename[0]}.sam" +" "+ " ".join(fin_opt) + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
    else:
        cmd = f"bwa mem {input_path} {input_file+'/'+x[0]} {input_file+'/'+x[1]} -o {output_filename[0]}.sam" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
elif len(x) == 1:
    if opt_list:
        fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
        cmd = f"bwa mem {input_path} {input_file+'/'+x[0]} -o  {output_filename[0]}.sam" + " " + " ".join(fin_opt) + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
    else:
        cmd = f"bwa mem {input_path} {input_file+'/'+x[0]} -o  {output_filename[0]}.sam" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
else:
    print("More than two files")

print(cmd)   
os.system(cmd.strip())

et = time.time()
tt = et - st

print("Total Time Taken by Process : ", tt, " sec")
