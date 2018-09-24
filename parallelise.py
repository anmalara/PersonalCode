import sys
import os
import time
import subprocess

sys.path.append("/nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/PersonalCode/")
from Utils import *

@timeit
def parallelise(list_processes, MaxProcess=10, list_logfiles=[]):
  ntotal = len(list_processes)
  processes = []
  logfiles = []
  condition = len(list_logfiles)>0 and len(list_logfiles)==len(list_processes)
  for index, process in enumerate(list_processes):
    wait = True
    while wait:
      nrunning = 0
      ncompleted = 0
      idx=0
      for proc in processes:
        if proc.poll() == None :
          nrunning += 1
        else:
          ncompleted += 1
          if not logfiles[idx].closed:
            logfiles[idx].close()
            print 'Job "%s" has finished.' % logfiles[idx].name
        idx += 1
      if nrunning >= MaxProcess:
        percentage = float(ncompleted)/float(ntotal)*100
        sys.stdout.write( 'Already completed '+str(ncompleted)+' out of '+str(ntotal)+' jobs --> '+str(percentage)+'%. Currently running: '+str(nrunning)+' \r')
        sys.stdout.flush()
        time.sleep(5)
      else:
        print 'only %i jobs are running, going to spawn new ones.' % nrunning
        wait = False
    if condition:
      f = open(list_logfiles[index],'w')
    else:
      f = open("log.txt",'w')
    logfiles.append(f)
    processes.append(subprocess.Popen(process, stdout=f))

  for proc in processes:
    proc.wait()
  for file in logfiles:
    file.close()
  if not condition:
    os.remove("log.txt")
