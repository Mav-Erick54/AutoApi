import sys
import time
import subprocess, os

st = time.time()

job_id = sys.argv[1]

# Set the path to your input file
input_file = sys.argv[2]
x = os.listdir(input_file)

# Set the path to your output directory
output_dir = sys.argv[3]

# command is mandatory to use with samtools
cmnd = sys.argv[4]

# options list
optionlist = sys.argv[5]
opt_list = [we for we in optionlist.strip('[]').split(',')]

# Set the name of output filename 
output_filename = []
for i in x:
    output_filename.append(i.split(".")[0])

# Run Samtools
try: 
    if opt_list or cmnd:
        fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
        cmd = f"samtools {cmnd} -b {input_file+'/'+x[0]} -o {output_dir+'/'+output_filename[0]}.bam" + " " + " ".join(fin_opt) + " " + "2>&1 | tee /home/ubuntu/Desktop/Mediomix/Tools_log/tool_logs.txt"
    else:
        cmd = f"samtools {cmnd} -b {input_file+'/'+x[0]} -o {output_dir+'/'+output_filename[0]}.bam" + " " + "2>&1 | tee /home/ubuntu/Desktop/Mediomix/Tools_log/tool_logs.txt"
except Exception as e:
    print(e)
    
print(cmd.strip())
os.system(cmd.strip())

et = time.time()
tt = et - st

print("Total Time Taken by Process : ", tt, " sec")

