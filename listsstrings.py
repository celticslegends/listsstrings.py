# The below code is missing the fifth team.
five_NE_teams = "Celtics Bruins Patriots RedSox"

print "Hold on, those are not all 5 sports teams! Fix it."
# below code declares what teams is.
teams = five_NE_teams.split(' ')
# The below code will add in the fifth team.
extra_team =  ["Revolution"]
# The below five lines of code give instructions to print out the fifth team
# to the list.
while len(teams) != 5:
    new_one = extra_team.pop()
    print "Adding ", new_one
    teams.append(new_one)
    print "There are %d teams now." % len(teams)
# The below code allows you to print out all of the teams by creating a space
# after the colon.
print "Look at this trick: ", teams

print "Let's play around a lot more and have some fun with teams."
# The below code will prints out the first team.
print teams[0]
# The below code prints out the teams in reverse order (negatively).
print teams[-4]
# below code will add in the fifth team each time.
print teams.pop()
# below code prints out all of the teams.
print ' '.join(teams)
# The below code is a nice trick.
print '#'.join(teams[0:5])
