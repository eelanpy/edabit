#03_run_timing:

def run_time():
    times = []
    while True:
        try:
            user_time = int(input("Enter 10 km run time: "))
            times.append(user_time)
        except:
            break

    print(f"\nAverage of the user's run time is {sum(times) / len(times)} over {len(times)} runs")
        

run_time()
