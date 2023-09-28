def scheduling(meetHrs1,wrkHrs1, minTime1, meetHrs2, wrkHrs2, minTime2)-> list:
    mutual_hrs=[]
    rangeF = []
    if meetHrs1 not in range(wrkHrs1) and meetHrs2 not in range(wrkHrs2):
        return ("error")
    else:
        if wrkHrs1 >= wrkHrs2:
            rangeF.append(wrkHrs1)
        else:
            rangeF.append(wrkHrs2)
        for i in rangeF:
            if meetHrs1[i]>= meetHrs2[i+1]:
                mutual_hrs.append(meetHrs1)


