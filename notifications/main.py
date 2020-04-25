import disco_events
import time

time.sleep(60)
try:
    disco_events.setJobInfo('jobId', 'dispatchId')

    for i in range(1000):
    
        disco_events.ProgressMesasge("Running", i).send()
        print(i)
        time.sleep(1)
        if i % 10 is 0:
            disco_events.EventMesasge("Getting there").send()
            print('event')

    disco_events.ProgressMesasge("Finished", 100).send()
except:
    print("Unexpected error:", sys.exc_info()[0])
    time.sleep(60)
