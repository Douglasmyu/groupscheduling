from datetime import timedelta,datetime
def parse_time_range(time_range):
    # Remove single quotes and split the string by ':' to get start and end times
    start_str = time_range.split()
    start_time = datetime.strptime(start_str[0], '%H:%M')
    end_time = datetime.strptime(start_str[1], '%H:%M')
    return start_time, end_time

def scheduling(meetHrs1,wrkHrs1, meetHrs2, wrkHrs2, meetLength):
    #parse
    meetHrs1_list = []
    meetHrs2_list = []
    wrkHrs1_list = []
    wrkHrs2_list = []
    range_work = []

    for period in meetHrs1:
        start1, end1 = parse_time_range(period)
        meetHrs1_list.append([start1,end1])
    for period in meetHrs2:
        start1, end1 = parse_time_range(period)
        meetHrs2_list.append([start1,end1])
    for period in wrkHrs1:
        time_obj = datetime.strptime(period, '%H:%M')
        wrkHrs1_list.append(time_obj)
    for period in wrkHrs2:
        time_obj = datetime.strptime(period, '%H:%M')
        wrkHrs2_list.append(time_obj)
    

    # Define the meeting duration as a timedelta object
    meet_duration = timedelta(minutes=meetLength)
    
    #get work hours range
    if(wrkHrs1_list[0]> wrkHrs2_list[0]):
        range_work.append(wrkHrs1_list[0])
    elif(wrkHrs1_list[0]== wrkHrs2_list[0]):
        range_work.append(wrkHrs2_list[0])
    else:
        range_work.append(wrkHrs2_list[0])

    if(wrkHrs1_list[1]> wrkHrs2_list[1]):
        range_work.append(wrkHrs2_list[1])
    elif(wrkHrs1_list[1]== wrkHrs2_list[1]):
        range_work.append(wrkHrs2_list[1])
    else:
        range_work.append(wrkHrs1_list[1])   

    available_slots = []
    combinedschedule = sorted(meetHrs1_list + meetHrs2_list, key = lambda x:x[0])
    start_time = range_work[0]
    for start,end in combinedschedule:
        if start>start_time:
            avaliable_duration = start - start_time
            if avaliable_duration >= meet_duration:
                available_slots.append((start_time,start))
        start_time = max(start_time,end)
    end_time = range_work[1]

    if end_time-start_time >= meet_duration:
        available_slots.append((start_time,end_time))
    for start, end in available_slots:
       print(f"Available slot: {start.time()} - {end.time()}")



def main():
    input_data = []
    with open("input.txt", "r") as file:
        current_input_set = []

        for line in file:
            line = line.strip()
            # Check if the line is empty (indicating the end of an input set)
            if not line:
                if current_input_set:
                    input_data.append(current_input_set)
                    current_input_set = []
            else:
                # Split the line by comma and remove the outer brackets
                range = line.strip('[]').split(',')
                time_ranges = []
                for element in range:
                    
                    element = element.strip('[]')
                    element = element.replace("':'"," ")
                    element = element.strip("'")
                    time_ranges.append(element)
                    
                # Append the time ranges to the current input set
                current_input_set.append(time_ranges)
    i = 0
    while i < len(current_input_set):
        mhours1 = current_input_set[i]
        whours1 = current_input_set[i+1]
        mhours2 = current_input_set[i+2]
        whours2 = current_input_set[i+3]
        dur = int(current_input_set[i+4][0])
        scheduling(mhours1,whours1,mhours2,whours2,dur)
        print('\n')
        i = i+5

    
main()
