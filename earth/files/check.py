# Earth 0123 2021
from datetime import datetime
CurrentTime = datetime.today()
CurrentTime = str(str(CurrentTime)[5:7]) + str(str(CurrentTime)[8:10]) +  " " + str(str(CurrentTime)[0:4]) + " " + str(str(CurrentTime)[11:13]) + str(str(CurrentTime)[14:16]) + str(str(CurrentTime)[17:19])

add = input("""Check  //  Ver_WinPy_9th-2020
"Month+Day + Year + Hour+Minute+Second" to 'UserData.txt'
"""+ '=' * 50 + "\n>>> ")

f = open('UserData.txt', 'a') # txt file open
print(CurrentTime + "  :  " +  str(add), file=f) # txt file save
f.close()
