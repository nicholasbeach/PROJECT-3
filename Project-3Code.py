from datetime import datetime
from urllib.request import urlretrieve
import re
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
log = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, log)

TotalNumber = 0

errors = 0
redirects = 0

#Additional lists and dictionaries allow me to generate outputs with the names of the months attached.
monthlist= [0, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
oldmonth = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November", 12:"December"}

Monthdict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
Monthrepo = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
Daytracker ={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}
popularity ={}
weekcounter = 0
weekstart = 4

#I made my own regex that splits each line into seven parts

splitter = re.compile('([0-9]+[/]+[A-Z]+[a-z]+[/]+\d\d\d\d)(.*GET)(.+?)(HTTP)(.*") ([2-5])')

for line in open(log):
  TotalNumber +=1
  seg = splitter.split(line)
  if not set or len(seg) < 7:
    continue
  if seg[6][0] == '3':
    redirects += 1
  
  if seg[6][0] == '4':
    errors += 1
  if seg[3] not in popularity.keys():
    popularity[seg[3]] =1
  else: 
    popularity[seg[3]] +=1

  date = datetime.strptime(seg[1], "%d/%b/%Y")
  day = (date.strftime('%A'))
  daynumber =(date.strftime('%d'))
  daymonth =(date.strftime('%b'))
  weekno = (int(daynumber) - 1) // 7 + 1
  
  
  
  if weekno == weekstart:    
    weekcounter +=1
    
  else:
    print("%s, week %d, has %d requests " %(daymonth, weekno, weekcounter))
    weekcounter = 0
    weekstart = weekno

  Daytracker[day]+=1
  Monthdict[date.month]+= 1
  Monthrepo[date.month].append(line)

for month, line in Monthrepo.items():
  name = monthlist[month]
  writer = open(name, 'w')
  writer.writelines(line)
  writer.close()

  


errors = float(100 * float(errors)/float(TotalNumber))                    
            
redirects = float(100 * float(redirects)/float(TotalNumber))


print("\n")              
print("The total number of request made in the time period represented by the log is %d" %(TotalNumber))
print("\n")
print("The following are the number of requests made in each month")
for key, value in Monthdict.items():
  print(oldmonth.get(key), value)


maximum = max(popularity.items())
minimum = min(popularity.items())
print("\n")    
for key, value in Daytracker.items():
    print(key, value)
print("\n")    
print("The following is the percentage of errors in the log file: %.2f%%" %(errors))
print("\n")
print("The following is the percentage of redirects in the log file: %.2f%%" %(redirects))
print("\n")
print("The following is the most requested file:")
print (max(popularity, key=popularity.get))
print("The following are the least requested file:")
key_min = min(popularity.keys(), key=(lambda k: popularity[k]))
for a, b in popularity.items():
  if b == popularity[key_min]:
    print(a)