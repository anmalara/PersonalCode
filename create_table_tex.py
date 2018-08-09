from utils import *

def change_table(to_change=[], new_string="", forwardOnly=False):
    newText = []
    with open(path+new_table, "U") as file:
        lines = file.readlines()
        isForward = False
        for line in lines:
            isToChange = False
            if "Forward Extension" in line :
                isForward = True
            if forwardOnly == isForward:
                for i in range(0,len(to_change)):
                    y = to_change[i][0]
                    control = "["+str(pt_bins[y-1])+"-"+str(pt_bins[y])+"]"
                    if control in line:
                        isToChange = True
                        newline = control
                        old = line.strip('\\\\\n').split('&')
                        for x in range(1,11):
                            if x in to_change[i][1]:
                                newline += new_string
                            else:
                                newline += " & " + old[x].strip()
                        newline += " \\\\\n"
                if isToChange:
                    newText.append(newline)
                else:
                    newText.append(line)
            else:
                newText.append(line)
    with open(path+new_table, "w") as file:
        for line in newText:
            file.write(line)



path = "/nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/PersonalCode/"
original_table = "TABLE_FIX.tex"
try:
    new_table = sys.argv[1]+".tex"
except :
    new_table = "table_new.tex"

cmd = "cp "+ original_table + " " + new_table
a = os.system(cmd)

standard_green  = " & \\textcolor{ForestGreen}{\\textbf{V}}"
standard_red    = " & \\textcolor{Red}{\\textbf{X}}"
standard_orange = " & \\textcolor{orange}{check}"


pt_bins  = [40, 72, 95, 160, 226, 283, 344, 443, 577, 606, 1500]
eta_bins = [0, 0.522, 0.783, 1.131, 1.305, 1.740, 1.930, 2.043, 2.322, 2.5, 2.853, 2.964, 3.139, 5.191]

oranges = [[1,[7,8,9,10]]]
reds = [[7,[10]], [8,[9,10]], [9,[7,8,9,10]], [10,[1,2,3,4,5,6,7,8,9,10]]]


change_table(to_change=oranges, new_string=standard_orange)
change_table(to_change=reds, new_string=standard_red)

oranges = [[1,[1,2,3,4,5,6,7,8,9,10]], [2,[8,9]], [3,[8,9]], [4,[8,9]], [5,[8,9]], [6,[8,9]], [7,[8,9,10]], [8,[8,9,10]]]
reds = [[9,[8,9,10]], [10,[1,2,3,4,5,6,7,8,9,10]]]

change_table(to_change=oranges, new_string=standard_orange, forwardOnly=True)
change_table(to_change=reds, new_string=standard_red, forwardOnly=True)
