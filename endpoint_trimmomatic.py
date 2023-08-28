import sys
import os
import time

st = time.time()

job_id = sys.argv[1]

# input file dir
input_file = sys.argv[2]
x = os.listdir(input_file)

# output dir
output_dir = sys.argv[3]

# list of options
optionlist = sys.argv[4]
opt_list = [we for we in optionlist.strip('[]').split(',')]

# mandatory values
kmers = sys.argv[5]

lead = sys.argv[6]

trail = sys.argv[7]

minlen = sys.argv[8]

# set path for output file name
output_filename = []
for i in x:
    output_filename.append(output_dir + "/" + i.split(".")[0])

# run trimmomatic command
cmd = ""
if len(x) == 2:
    if opt_list:
        fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
        cmd = f"trimmomatic PE {input_file+'/'+x[0]} {input_file+'/'+x[1]} {output_filename[0]}_paired.fastq {output_filename[0]}_unpaired.fastq {output_filename[1]}_paired.fastq {output_filename[1]}_unpaired.fastq ILLUMINACLIP:/home/madmin/Desktop/Mediomix/adapters/TruSeq3-SE.fa:{kmers} LEADING:{lead} TRAILING:{trail} MINLEN:{minlen}" +" "+ " ".join(fin_opt) + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
    else:
        cmd = f"trimmomatic PE {input_file+'/'+x[0]} {input_file+'/'+x[1]} {output_filename[0]}_paired.fastq {output_filename[0]}_unpaired.fastq {output_filename[1]}_paired.fastq {output_filename[1]}_unpaired.fastq ILLUMINACLIP:/home/madmin/Desktop/Mediomix/adapters/TruSeq3-SE.fa:{kmers} LEADING:{lead} TRAILING:{trail} MINLEN:{minlen}" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
elif len(x) == 1:
    if opt_list:
        fin_opt = [" ".join(rmopt.split(":")) for rmopt in opt_list]
        cmd = f"trimmomatic SE {input_file+'/'+x[0]} {output_filename[0]}.trimmed.fastq ILLUMINACLIP:/home/madmin/Desktop/Mediomix/adapters/TruSeq3-SE.fa:{kmers} LEADING:{lead} TRAILING:{trail} MINLEN:{minlen}" + " " + " ".join(fin_opt) + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
    else:
        cmd = f"trimmomatic SE {input_file+'/'+x[0]} {output_filename[0]}.trimmed.fastq ILLUMINACLIP:/home/madmin/Desktop/Mediomix/adapters/TruSeq3-SE.fa:{kmers} LEADING:{lead} TRAILING:{trail} MINLEN:{minlen}" + " " + "2>&1 | tee /home/madmin/Desktop/Mediomix/Tools_log/tool_logs.txt"
else:
    print("More than two files")

print(cmd)   
os.system(cmd.strip())

et = time.time()
tt = et - st

print("Total Time Taken by Process : ", tt, " sec")
