import sys
import os
import time
import subprocess

st = time.time()

job_id = sys.argv[1]

# input file
input_file = sys.argv[2]
x = os.listdir(input_file)

# ouput dir
output_dir = sys.argv[3]
output_filename = []
for i in x:
    output_filename.append(output_dir + "/" + i.split(".")[0])

# list of options
optionlist = sys.argv[4]
opt_list = [we for we in optionlist.strip('[]').split(',')]

# adapter (mandatory)
adapter = sys.argv[5:]
p_adapters = "".join(adapter).strip("[]").split(",")

# run command for cutadapt
cmd = ""
if len(x) == 2:
    if opt_list: 
        if (len(p_adapters) == 2):
            fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
            cmd = f"cutadapt -a {p_adapters[0]} -A {p_adapters[1]} -o {output_filename[0]}.trim.fastq -p {output_filename[1]}.trim.fastq {input_file+'/'+x[0]} {input_file+'/'+x[1]}" + " " + " ".join(fin_opt) + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
        else:
            print("1 adapter found")
    else:
        cmd = f"cutadapt -a {p_adapters[0]} -A {p_adapters[1]} -o {output_filename[0]}.trim.fastq -p {output_filename[1]}.trim.fastq {input_file+'/'+x[0]} {input_file+'/'+x[1]}" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
elif len(x) == 1:
    if opt_list: 
        if(len(p_adapters) == 1):
            fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
            cmd = f"cutadapt -a {p_adapters[0]} -o {output_filename[0]}.trim.fastq {input_file+'/'+x[0]}" + " " + " ".join(fin_opt)+ " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
        else:
            print("2 adapter found")
    else:
        cmd = f"cutadapt -a {p_adapters[0]} -o {output_filename[0]}.trim.fastq {input_file+'/'+x[0]}" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
else:
    print("more than 2 files found")
    
#subprocess.run(["cutadapt", "-a", "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA", "-A", "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT", "-o", f"{output_filename[0]}.trim.fastq", "-p", f"{output_filename[1]}.trim.fastq", input_file+"/"+x[0], input_file+"/"+x[1]])

#subprocess.run(["cutadapt", "-a", "AACCGGTT", "-o", f"{output_filename[0]}.trim.fastq", input_file+"/"+x[0]])

print(cmd)
os.system(cmd.strip())

et = time.time()
tt = et - st

print("Total Time Taken by Process : ", tt, " sec")
