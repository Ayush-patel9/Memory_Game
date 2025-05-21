import csv
if len(l3) == 16:
    timer.stop()
    total_time = timer.get_elapsed_time()
    with open(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\record.csv", "r") as A:
        csv_reader = csv.reader(A)
        K = 0
        W = 0
        for i in csv_reader:
            K += 1
            try:
                if n >= int(i[2]):
                    W += 1
            except:
                pass

    with open(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\record.csv", "a") as A:
        A.write(f"{K},{player_name},{n},{str(datetime.timedelta(seconds=total_time))[2:7]}\n")
    
with open(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\record.csv", "r") as B:

    csv_reader = csv.reader(B)
            
    next(csv_reader)
            
    for i in csv_reader:
                
        if len(i) != 0:
            print(i)

itM = []
T = []
with open(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\record.csv", "r") as B:
    csv_reader = csv.reader(B)
    next(csv_reader)
    for i in csv_reader:
        M.append(int(i[2]))
        T.append(i[3])

    s3 = Label(i5, text=f"Least No. of Moves Achieved : {min(M)}\n Least Time Taken : {min(T)}", font="times 25", background="black", foreground="#00FF00")
    s3.pack()
