import sys
import subprocess

list_processes = []
script_path = "/nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/scripts/"

path = sys.argv[1]+"/*/*.root"
xml  = sys.argv[2]

proc = subprocess.Popen( [script_path+"./create-dataset-xmlfile", path, xml] )
proc.wait()
proc = subprocess.Popen( ["python", script_path+"readaMCatNloEntries.py", "20", xml] )
proc.wait()
proc = subprocess.Popen( ['tail', '-1', xml] )
proc.wait()
