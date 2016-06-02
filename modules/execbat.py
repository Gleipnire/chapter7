#execbat.py
import os
import subprocess
def run(**args):
    print"[*] In execbat module."
    path = "/Python35-32/testdir/fibo.py"
    fp = "python %s 60" %path
    a=subprocess.check_output(fp, stderr=subprocess.STDOUT, shell=True)
    
    return(str(a))
    