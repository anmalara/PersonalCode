from Utils import *

def reverseList(list_):
  final = []
  for eta in default_eta:
    final.append([eta,[]])
  for i in range(len(list_)):
    for eta in list_[i][1]:
      final[eta-1][1].append(list_[i][0])
  for i in reversed(range(len(final))):
    if len(final[i][1])==0:
      final.pop(i)
    else:
      final[i][1] = sorted(set(final[i][1]))
  return final


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
            for x in range(1,14):
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




pt_bins  = [40, 72, 95, 160, 226, 283, 344, 443, 577, 606, 1500]
eta_bins = [0, 0.522, 0.783, 1.131, 1.305, 1.740, 1.930, 2.043, 2.322, 2.5, 2.853, 2.964, 3.139, 5.191]

default_eta = list(range(1, len(eta_bins)))
default_pt  = list(range(1, len(pt_bins)))

standard_green  = " & \\textcolor{ForestGreen}{\\textbf{V}}"
standard_black  = " & \\textcolor{black}{not used}"
standard_orange = " & \\textcolor{orange}{check}"
standard_red    = " & \\textcolor{Red}{\\textbf{X}}"
standard_violet = " & \\textcolor{violet}{stat}"
standard_blue   = " & \\textcolor{blue}{shift}"
standard_corn   = " & \\textcolor{CornflowerBlue}{extrapolation}"

colors = []
colors.append(standard_black)
colors.append(standard_orange)
colors.append(standard_red)
colors.append(standard_violet)
colors.append(standard_blue)
colors.append(standard_corn)



def mainprogram(new_table, SM_change, FE_change):
  cmd = "cp "+ original_table + " " + new_table
  a = os.system(cmd)
  for i in reversed(range(len(SM_change))):
    change_table(to_change=SM_change[i], new_string=colors[i])
    change_table(to_change=FE_change[i], new_string=colors[i], forwardOnly=True)

path = "/nfs/dust/cms/user/amalara/WorkingArea/UHH2_94/CMSSW_9_4_1/src/UHH2/PersonalCode/"
original_table = "TABLE_FIX_EXTENDED.tex"


new_table = "table_new.tex"

checks = [[1,[7,8,9,10]]]
reds = [[7,[10]], [8,[9,10]], [9,[7,8,9,10]], [10,[1,2,3,4,5,6,7,8,9,10]]]

################################################################################
################################################################################
################################################################################

#############################
#                           #
#       MAIN Program        #
#                           #
#############################

new_table = "table_standard.tex"

notused_SM        = [[1,[1]], [2,[1]], [3,[1]], [4,[1]], [5,[1]], [6,[1]], [7,[1]], [8,[1]], [9,[1]], [10,[1]], [11, default_pt], [12, default_pt], [13, default_pt]]
checks_SM         = []
reds_SM           = []
stats_SM          = [[7,[1,9]], [8,[9]], [9,[1,7,8,9,10]], [10,[6,7,8,9,10]]]
shifts_SM         = []
extrapolations_SM = [[2,[2]], [3,[2]], [4,[6]], [5,[2,6]], [6,[2,3,4,6,9]], [7,[2,3,4,5,6,7,10]], [8,[2,6,7,8,10]], [9,[2,3,6]], [10,[2,3,4,5]] ]


notused_FE        = [[1,[1]], [2,[1]], [3,[1]], [4,[1]], [5,[1]], [6,[1]], [7,[1]], [8,[1]], [9,[1]], [10,[1]], [11,[1]], [12,[1]], [13,[1]]]
checks_FE         = [[12,[7,8]], [13,[7]]]
reds_FE           = [[11, default_pt]]
stats_FE          = [[12,[9,10]], [13,[9,10]]]
shifts_FE         = [[12,[1,2,3,4,5,6]], [13, [1,2,3,4,5,6,7,8]]]
extrapolations_FE = [[1,[3]], [2,[2]], [4,[2]], [6,[6]], [7,[6]], [9,[2]], [10,[6]], [10,[9]], [11,[3,6]], [12,[6,8]], [13,[6]] ]

notused_SM        = reverseList(notused_SM)
checks_SM         = reverseList(checks_SM)
reds_SM           = reverseList(reds_SM)
stats_SM          = reverseList(stats_SM)
shifts_SM         = reverseList(shifts_SM)
extrapolations_SM = reverseList(extrapolations_SM)

notused_FE        = reverseList(notused_FE)
checks_FE         = reverseList(checks_FE)
reds_FE           = reverseList(reds_FE)
stats_FE          = reverseList(stats_FE)
shifts_FE         = reverseList(shifts_FE)
extrapolations_FE = reverseList(extrapolations_FE)

mainprogram(new_table, [notused_SM,checks_SM, reds_SM, stats_SM, shifts_SM, extrapolations_SM], [notused_FE, checks_FE, reds_FE, stats_FE, shifts_FE, extrapolations_FE])
################################################################################
################################################################################


################################################################################
################################################################################
new_table = "table_standard_simplified.tex"

notused_SM        = [[1,[1]], [2,[1]], [3,[1]], [4,[1]], [5,[1]], [6,[1]], [7,[1]], [8,[1]], [9,[1]], [10,[1]], [11, default_pt], [12, default_pt], [13, default_pt]]
checks_SM         = []
reds_SM           = []
stats_SM          = [[7,[1,9]], [8,[9]], [9,[1,7,8,9,10]], [10,[6,7,8,9,10]]]
shifts_SM         = []
extrapolations_SM = [[2,[2]], [3,[2]], [5,[2]], [6,[2]], [7,[2]], [8,[10]], [9,[3]], [10,[2]] ]


notused_FE        = [[1,[1]], [2,[1]], [3,[1]], [4,[1]], [5,[1]], [6,[1]], [7,[1]], [8,[1]], [9,[1]], [10,[1]], [11,[1]], [12,[1]], [13,[1]]]
checks_FE         = [[12,[7,8]], [13,[7]]]
reds_FE           = [[11, default_pt]]
stats_FE          = [[12,[9,10]], [13,[9,10]]]
shifts_FE         = [[12,[1,2,3,4,5,6]], [13, [1,2,3,4,5,6,7,8]]]
extrapolations_FE = [[4,[2]], [9,[2]], [11,[3]]]

notused_SM        = reverseList(notused_SM)
checks_SM         = reverseList(checks_SM)
reds_SM           = reverseList(reds_SM)
stats_SM          = reverseList(stats_SM)
shifts_SM         = reverseList(shifts_SM)
extrapolations_SM = reverseList(extrapolations_SM)

notused_FE        = reverseList(notused_FE)
checks_FE         = reverseList(checks_FE)
reds_FE           = reverseList(reds_FE)
stats_FE          = reverseList(stats_FE)
shifts_FE         = reverseList(shifts_FE)
extrapolations_FE = reverseList(extrapolations_FE)

mainprogram(new_table, [notused_SM,checks_SM, reds_SM, stats_SM, shifts_SM, extrapolations_SM], [notused_FE, checks_FE, reds_FE, stats_FE, shifts_FE, extrapolations_FE])
################################################################################
################################################################################


################################################################################
################################################################################
new_table = "table_V24.tex"

notused_SM        = [[1,[1]], [2,[1]], [3,[1]], [4,[1]], [5,[1]], [6,[1]], [7,[1]], [8,[1]], [9,[1]], [10,[1]], [11, default_pt], [12, default_pt], [13, default_pt]]
checks_SM         = []
reds_SM           = []
stats_SM          = [[6,[9]], [7,[9]], [8,[9,10]], [9,[7,8,9,10]], [10,[6,7,8,9,10]]]
shifts_SM         = []
extrapolations_SM = [[2,[2]], [4,[2]], [5,[3]], [7,[2,5,6]], [8,[2,3]], [9,[2]], [10,[2]] ]


notused_FE        = [[1,[1]], [2,[1]], [3,[1]], [4,[1]], [5,[1]], [6,[1]], [7,[1]], [8,[1]], [9,[1]], [10,[1]], [11,[1]], [12,[1]], [13,[1]]]
checks_FE         = [[12,[8]], [13,[7]]]
reds_FE           = [[11, default_pt]]
stats_FE          = [[11,[9,10]], [12,[9,10]], [13,[8,9,10]]]
shifts_FE         = [[12,[1,2,3,4,5,6,7]], [13, [1,2,3,4,5,6]]]
extrapolations_FE = [[2,[2]], [4,[2]], [9,[2]], [12,[2,3]] ]

notused_SM        = reverseList(notused_SM)
checks_SM         = reverseList(checks_SM)
reds_SM           = reverseList(reds_SM)
stats_SM          = reverseList(stats_SM)
shifts_SM         = reverseList(shifts_SM)
extrapolations_SM = reverseList(extrapolations_SM)

notused_FE        = reverseList(notused_FE)
checks_FE         = reverseList(checks_FE)
reds_FE           = reverseList(reds_FE)
stats_FE          = reverseList(stats_FE)
shifts_FE         = reverseList(shifts_FE)
extrapolations_FE = reverseList(extrapolations_FE)

mainprogram(new_table, [notused_SM,checks_SM, reds_SM, stats_SM, shifts_SM, extrapolations_SM], [notused_FE, checks_FE, reds_FE, stats_FE, shifts_FE, extrapolations_FE])
################################################################################
################################################################################



################################################################################
################################################################################
new_table = "table_V27.tex"

notused_SM        = [[1,[1]], [2,[1]], [3,[1]], [4,[1]], [5,[1]], [6,[1]], [7,[1]], [8,[1]], [9,[1]], [10,[1]], [11, default_pt], [12, default_pt], [13, default_pt]]
checks_SM         = []
reds_SM           = []
stats_SM          = [[6,[9]], [7,[9]], [8,[9,10]], [9,[7,8,9,10]], [10,[6,7,8,9,10]]]
shifts_SM         = []
extrapolations_SM = []


notused_FE        = [[1,[1]], [2,[1]], [3,[1]], [4,[1]], [5,[1]], [6,[1]], [7,[1]], [8,[1]], [9,[1]], [10,[1]], [11,[1]], [12,[1]], [13,[1]]]
checks_FE         = [[12,[8]], [13,[7]]]
reds_FE           = [[11, default_pt]]
stats_FE          = [[11,[9,10]], [12,[9,10]], [13,[8,9,10]]]
shifts_FE         = [[12,[1,2,3,4,5,6,7]], [13, [1,2,3,4,5,6]]]
extrapolations_FE = []

notused_SM        = reverseList(notused_SM)
checks_SM         = reverseList(checks_SM)
reds_SM           = reverseList(reds_SM)
stats_SM          = reverseList(stats_SM)
shifts_SM         = reverseList(shifts_SM)
extrapolations_SM = reverseList(extrapolations_SM)

notused_FE        = reverseList(notused_FE)
checks_FE         = reverseList(checks_FE)
reds_FE           = reverseList(reds_FE)
stats_FE          = reverseList(stats_FE)
shifts_FE         = reverseList(shifts_FE)
extrapolations_FE = reverseList(extrapolations_FE)

mainprogram(new_table, [notused_SM,checks_SM, reds_SM, stats_SM, shifts_SM, extrapolations_SM], [notused_FE, checks_FE, reds_FE, stats_FE, shifts_FE, extrapolations_FE])
################################################################################
################################################################################
