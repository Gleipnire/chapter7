#backintime.py (so much goddamn RNG)
import sys
import time
import os
import threading
import datetime
import subprocess
import random

curr_time = datetime.datetime.now()
    
new_time = (curr_time.year, #yr
                curr_time.month, #mth
                curr_time.day, #day
                curr_time.hour, #hr
                curr_time.minute, #min
                0, #sec
                curr_time.microsecond)# msec  

def linux_time_screw():
    #linux: NEED ROOT?
        #date_str = "3 Jul 2015 18:00:00"
        #os.system('date --set %s' %date_str)    
    print"thread"
    ostime= subprocess.check_output("date", stderr=subprocess.STDOUT, shell=True).split()
    ntime = ostime[3].split(':')
    #screw with seconds
    ntime_sec_tmp=int(ntime[2])
    ntime_sec_tmp -= random.randint(0, ntime_sec_tmp)
    ntime_sec_tmp += random.randint(0, 59-ntime_sec_tmp)
    ntime[2] = str(ntime_sec_tmp)
    #screw with minutes
    ntime_min_tmp = int(ntime[1])
    ntime_min_tmp -=random.randint(0, ntime_min_tmp)
    ntime_min_tmp += random.randint(0, 59- ntime_min_tmp)
    ntime[1] = str(ntime_min_tmp)
    
    #screw with minutes
    ntime_hr_tmp = int(ntime[0])
    ntime_hr_tmp -=random.randint(0, ntime_hr_tmp)
    ntime_hr_tmp += random.randint(0, 23- ntime_hr_tmp)
    ntime[0] = str(ntime_hr_tmp)  
    
    #put it all together
    ntimestr = "%s:%s:%s"%(ntime[0], ntime[1], ntime[2])
    curr_date_str = "%s %s %s %s" %(ostime[2], ostime[1], ostime[5], ostime[3])
    
    new_date_str = "%s %s %s %s" %(ostime[2], ostime[1], ostime[5], ntimestr)
    os.system('date -s "%s"'% new_date_str) 
    time.sleep(random.randint(10, 15))
    
    os.system('date -s "%s"' %curr_date_str)
    return
    
    
    
def win_time_screw():
    #windows: NEED ADMIN
        #time_str = "HR:MN"
        #os.system('time %s' %time_str)    
    print"thread"
    ostime = subprocess.check_output('time /t', stderr = subprocess.STDOUT, shell=True)
    
    
    ostime = ostime.split()
    ntime = ostime[0].split(':')
  
    #screw with minutes
    ntime_min_tmp = int(ntime[1])
    ntime_min_tmp -=random.randint(0, ntime_min_tmp)
    ntime_min_tmp += random.randint(0, 59- ntime_min_tmp)
    ntime[1] = str(ntime_min_tmp)
    
    #screw with minutes
    ntime_hr_tmp = int(ntime[0])
    ntime_hr_tmp -=random.randint(0, ntime_hr_tmp)
    ntime_hr_tmp += random.randint(0, 11- ntime_hr_tmp)
    ntime[0] = str(ntime_hr_tmp)  
    
    #screw with am/pm
    if random.randint(0,1):
        ntime.append('AM')
    else:
        ntime.append('PM')
    
    #put it all together
    ntimestr = "%s:%s"%(ntime[0], ntime[1])
    curr_time_str = "%s %s" %(ostime[0], ostime[1])
    
    new_time_str = "%s %s" %(ntimestr, ntime[2])
    os.system('time %s'% new_time_str) 
    time.sleep(random.randint(10, 15))
    
    os.system('time %s' %curr_time_str)
    return


def run(**args):
    thread_count = 1 
    
    
    if sys.platform =="linux2":
        c=0
        while c!=thread_count:
            threading.Thread(target=linux_time_screw).start()
            
            c+=1
            time.sleep(random.randint(3, 9))
        return None
    
    
    if sys.platform =="win32":
        c=0
        while c!=thread_count:
            time_thread= threading.Thread(target=win_time_screw).start()
            c+=1
            time.sleep(2)
        return None  
    
    return None
            
if __name__=="__main__":
    run()