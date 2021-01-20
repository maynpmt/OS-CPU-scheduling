import random
import statistics

a = 3 #name of txt file
# read dataset from .txt file
file_rand = "dataset{}.txt".format(a)
with open(file_rand) as f:
    lines = [int(line.strip()) for line in f]
f.close
# read shuffled dataset from .txt file
file_shuff = "dataset_sh{}.txt".format(a)
with open(file_shuff) as f:
    lines_sh = [int(line_sh.strip()) for line_sh in f]
f.close

# show random burst time of process 
print ("Random Burst time : " +  str(lines))
# show shuffled queue of process
b_time = lines_sh
n = len(b_time)
print ("Randomly queue up : " +  str(b_time))
#--------------------------------------------#
b_time.sort()
print ("Sorted queue up : " +  str(b_time))

# Find the waiting time
w_time = [0] * n

w_time[0] = 0 #first process waiting time = 0
for i in range(1, n) :
    w_time[i] = w_time[i-1] + b_time[i-1]
print("Waiting time : " + str(w_time))

# Find the turnaround time
tat = [n]
tat[0] = b_time[0]
for i in range(1, n):
    temp = w_time[i] + b_time[i]
    tat.append(temp)

print("Turnaround time : " + str(tat))
print("______________________________")    
# AVERAGE waiting time
print("Average waiting time = %.3f" %(statistics.mean(w_time)))
#AVERAGE turnaround time
print("Average turnaround time = %.3f" %(statistics.mean(tat)))

 # Display processes along with all details  
print("-----------------------------------------------------------") 
print("Processes    Burst Time     Waiting Time    Turn-Around Time")
print("-----------------------------------------------------------")  
for i in range(n):  
    print(" ", i + 1, "\t\t", b_time[i],  "\t\t", w_time[i], "\t\t", tat[i]) 

# AVERAGE waiting time
print("Average waiting time = %.3f" %(statistics.mean(w_time)))
#AVERAGE turnaround time
print("Average turnaround time = %.3f" %(statistics.mean(tat)))


