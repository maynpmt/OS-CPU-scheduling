import random


a = int( input('Assumption (a number) : '))

# input the number of process
n = int( input('The number of process : ') ) 
process = []
for x in range(3):
    if x == 0:
        text = 'SHORT'
    elif x == 1:
        text = 'MEDIUM'
    else:
        text = 'LONG'

    # input lenght of burst time to random
    x, y = [int(x) for x in input('Range of {} burst time to random (millisecond, millisecond) : '.format(text)).split(',')] 
    
    #input percentage of burst time process
    percent = int( input('Percentage(%) of {} burst time processing : '.format(text)) )

    # using random to generate random number list
    res = [random.randint(x, y) for _ in range(int((n*percent)/100))] #random
    process.extend(res) #add to list without bracket
 
# printing result
print ("Random process burst time : " +  str(process))

#write random list in .txt file
with open("dataset{}.txt".format(a), "w+") as file_handler:
    for listitem in process:
        file_handler.write('%s\n' % listitem)
file_handler.close

#write shuffled list in .txt file
with open("dataset_sh{}.txt".format(a), "w+") as file_handler:
    random.shuffle(process)
    print ("Randomly queue up : " + str(process))
    for listitem in process:
        file_handler.write('%s\n' % listitem)
file_handler.close
