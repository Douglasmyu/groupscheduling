from datetime import timedelta


def scheduling(meetHrs1,wrkHrs1, minTime1, meetHrs2, wrkHrs2, minTime2, meetLength)-> list:
    mutual_hrs=[]
    rangeF = []
    meetHrs1 = input()
    wrkHrs1 = input()
    minTime1 = input()
    meetHrs2 = input()
    wrkHrs2 = input()
    minTime2 = input()
    combined_schedule = [wrkHrs1, wrkHrs2]
    #check if meet hrs are in range of work hrs
    if meetHrs1 not in range(wrkHrs1) and meetHrs2 not in range(wrkHrs2):
        return ("error")
    else:
        #use the lowest work hrs as range of possible meeting times
        if wrkHrs1 <= wrkHrs2:
            rangeF.append(wrkHrs1)
        else:
            rangeF.append(wrkHrs2)
        

        testFiles = ["testCase1.txt", "testCase2.txt", "testCase3.txt"]
        outputFiles = ["output1.txt", "output2.txt", "output3.txt" ]
        for i in range(3):
            with open(testFiles[i], 'a') as f:
             f.write(' ')
        #find available work hrs
            for i in range(1, len(combined_schedule)):
                start_time = max(combined_schedule[i-1][1], combined_schedule[i][0])
                end_time = min(combined_schedule[i][1], combined_schedule[i][1])
            
                if end_time - start_time >= timedelta(minutes=meetLength):
                    mutual_hrs.append([start_time, end_time])



