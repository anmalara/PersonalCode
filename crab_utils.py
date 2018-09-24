import sys
import os
import subprocess
import time
import datetime

def get_whitespace(n):
    line = ""
    for i in range(0, n):
        line += " "
    return line

def find_numbers(line,find1="(", find2=")", split_char="/"):
    numbers = line[line.find(find1)+1:line.find(find2)]
    numbers = numbers.strip()
    numbers = [s for s in numbers.split(split_char) if s.isdigit()]
    return numbers

def createLog(path):
    with open(path+"log.txt", "w+") as file:
        line="Process"+get_whitespace(23)
        for el in checks:
            line+= el+get_whitespace(wsl-len(el))
        file.write(line+"\n\n")
        for sample in sorted(os.listdir(path)):
            if os.path.isdir(path+sample):
                line=sample+get_whitespace(30-len(sample))
                for el in checks:
                    line+= "0"+get_whitespace(wsl-1)
                file.write(line+"\n")

def checkStatus(path, output=False, istoResubmit=False):
    resubText=[]
    for sample in sorted(os.listdir(path)):
        if os.path.isdir(path+sample):
            isToChange = False
            numbers = []
            for el in checks:
                numbers.append(["0", "0"])
            with open(path+"temp.txt", "w+") as f:
                command = ["crab", "status", path+"/"+sample]
                if output:
                    process = subprocess.Popen(command)
                else:
                    process = subprocess.Popen(command, stdout=f)
                process.wait()
            with open(path+"temp.txt", "r") as f:
                for line in f.readlines():
                    for index, el in enumerate(checks):
                        if "%" in line and el in line:
                            numbers[index] = find_numbers(line)
                if istoResubmit:
                    if int(numbers[1][0]) != 0 :
                        command = ["crab", "resubmit", path+sample]
                        process = subprocess.Popen(command)
                        process.wait()
                        resubText.append(sample+"\n")
            newText = []
            if not output:
                with open(path+"log.txt", "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        if sample in line:
                            newLine = sample+get_whitespace(30-len(sample))
                            for el in numbers:
                                newLine+= el[0]+"/"+el[1]+get_whitespace(wsl-len(el[0]+"/"+el[1]))
                            if numbers[0][0] == numbers[0][1]:
                                newLine = sample+get_whitespace(30-len(sample))+numbers[0][0]+"/"+numbers[0][1]+" done."
                            newText.append(newLine+"\n")
                        else:
                            newText.append(line)
            with open(path+"log.txt", "w") as outputfile:
                for line in newText:
                    outputfile.write(line)
    if resubText:
        with open(path+"log.txt", "a") as file:
            file.write("\n\n\n"+"Resubmited on " + datetime.date.today().isoformat() + "\n")
            for line in resubText:
                file.write(line)


def resubmit(path, isToCheck=False):
    if isToCheck:
        checkStatus(path, istoResubmit=True)
    else:
        with open(path+"log.txt", "r+") as file:
            lines = file.readlines()
            newText = []
            for line in lines[2:]:
                if len(line.split()) < 8:
                    continue
                if int(line.split()[2].split("/")[0]) != 0:
                    sample = line.split()[0]
                    command = ["crab", "resubmit", path+sample]
                    process = subprocess.Popen(command)
                    process.wait()
                    newText.append(sample+"\n")
            if newText:
                file.write("\n\n\n"+"Resubmited on " + datetime.date.today().isoformat() + "\n")
                for line in newText:
                    file.write(line)


wsl=15
checks= ["finished", "failed", "running", "transferring", "idle", "unsubmitted", "cooloff", "killed"]
path ="/nfs/dust/cms/user/amalara/WorkingArea/UHH2_94_Crab/CMSSW_9_4_1/src/UHH2/scripts/crab/MC_QCD_Flat/"


createLog(path)
# checkStatus(path, output=True)
checkStatus(path)
# resubmit(path)
# resubmit(path, isToCheck=True)


# from threading import Timer
#
# x=datetime.date.today()
# y=x.replace(minute=x.minute+1)
# delta_t=y-x
#
# secs=delta_t.seconds+1
#
# t = Timer(10.0, createLog, path)
# t = Timer(secs, resubmit(path, isToCheck=True))
# t.start()
