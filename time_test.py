import datetime

hourtm = datetime.datetime.now()


while hourtm.hour > 22 and hourtm.hour < 10:
    print("Sleep Time Son")
    time.sleep(30)
    
    
    
