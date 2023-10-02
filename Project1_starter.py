from datetime import timedelta
def scheduling(meetHrs1,wrkHrs1, meetHrs2, wrkHrs2, meetLength)-> list:
    mutual_hrs =[]
    combined_schedule = [wrkHrs1, wrkHrs2]
    #check if meet hrs are in range of work hrs
    if meetHrs1 not in range(wrkHrs1) and meetHrs2 not in range(wrkHrs2):
        return ("error")
    else:
        
        #find available work hrs
            for i in range(1, len(combined_schedule)):
                start_time = max(combined_schedule[i-1][1], combined_schedule[i][0])
                end_time = min(combined_schedule[i][1], combined_schedule[i][1])
            
                if end_time - start_time >= timedelta(minutes=meetLength):
                    mutual_hrs.append([start_time, end_time])
            return mutual_hrs

def main():
    testFiles = ["input.txt"]
    for i in range(1):
            with open(testFiles[i], 'a') as f:
             f.write(' ')
             #for loop 10 times for 10 test cases
                #for loop 5 times for each input case

