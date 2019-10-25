def time():
     hour1 = 6
     hour2 = 6 
     min1 = 1 
     min2 = 2
     sec1 = 30
     sec2 = 10


     time1_in_sec = (hour1 * 3600) + (min1 * 60) + sec1
     time2_in_sec = (hour2 * 3600) + (min2 * 60) + sec2
     time3 = time2_in_sec - time1_in_sec
     print(time3)
time()