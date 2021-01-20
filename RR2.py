
import random
import statistics

a = 1 #name of txt file
# read dataset from .txt file
file = "dataset{}.txt".format(a)
with open(file) as f:
    lines = [int(line.strip()) for line in f]
f.close
# read shuffled dataset from .txt file
file = "dataset_sh{}.txt".format(a)
with open(file) as f:
    lines_sh = [int(line_sh.strip()) for line_sh in f]
f.close

# show random burst time of process 
print ("Random Burst time : " +  str(lines))
# show shuffled queue of process
b_time = lines_sh
n = len(b_time)
print ("Randomly queue up : " +  str(b_time))

#---------------------------------------------#

q_time = 10
remain_time = [0] * n
w_time = [0] * n
for i in range (n): 
    remain_time[i] = b_time[i]
#print("REMAINING_TIME : " + str(remain_time))

current_time = 0

while(1):
    done = True

    for i in range(n):
        if(remain_time[i] > 0):
            done = False
            
            if(remain_time[i] >= q_time): 
               current_time += q_time
               remain_time[i] -= q_time
               w_time[i] += current_time

            else : #remaining time < remaining time
                current_time = current_time + remain_time[i]
                w_time[i] = current_time - b_time[i]
                remain_time[i] = 0
    
    if(done == True):
        break #exit while loop

#Show waiting time
print("Waiting time : " + str(w_time))

#Find Turn around time
tat = [0]*n
for i in range(n):
    # print(tat)
    tat[i] = w_time[i] + b_time[i]

#Show Turn around time
print("Turnaround time : " + str(tat))
 # AVERAGE waiting time
print("Average waiting time = %.3f" %(statistics.mean(w_time)))
#AVERAGE turnaround time
print("Average turnaround time = %.3f" %(statistics.mean(tat)))
#print("\n")   


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



