from urllib.request import urlretrieve
import datetime
import re
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

TotalNumber = 0
log = 'local_copy.log'
errors = 0
redirects = 0
Monthdict = {"Jan":0, "Feb":0, "Mar":0, "Apr":0, "May":0, "Jun":0, "Jul":0, "Aug":0, "Sep":0, "Oct":0, "Nov":0, "Dec":0}
Daytracker ={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}
mostrequested={"test":0}



'''the initial for loop runs through every line of the log file. The subsequent 
code is mostly reliant on this particular for loop
The second loop runs through each month of the year and appends each month's data
to its appropriate file. Furthermore, it replaces the three letter abbreviation 
for each month so that the date.time function can pull up the specific day of the week
the program was run. I tried to use a dictionary for the replacement, however, Apr
and Oct could not be replaced by April and October. After verifying that it worked for
everything else, I had write out an if statement for each month instead. ''' 
for line in open(log):
            
    TotalNumber += 1
    if '" 4' in line:
        errors+=1
    if '" 3' in line:
        redirects+=1
    

    for original in Monthdict.keys():
      
        if original in line:
            Monthdict[original] += 1
            textfile = open(original+".txt", "a")
            textfile.write("%s\n" %(line))
            textfile.close      
            x = line[line.find("[")+1:line.find(":")]
                    
            if "January" in x:
                continue
            
            elif "Jan" in x:
                x = x.replace("Jan", "January")
            if "February" in x:
                continue
            elif "Feb" in x:
                x = x.replace("Feb", "February")
            if "March" in x:
                continue                    
            
            elif "Mar" in x:
                x = x.replace("Mar", "March")
            if "April" in x:
                continue                    
            
            elif "Apr" in x:
                x = x.replace("Apr", "April")
            if "May" in x:
                continue                    
                                           
            elif "May" in x:
                x = x.replace("May", "May")
            if "June" in x:
                continue                
                            
            elif "Jun" in x:
                x = x.replace("Jun", "June")     
            if "July" in x:
                continue                    
                    
            elif "Jul" in x:
                x = x.replace("Jul", "July")
                    
            if "August" in x:
                continue                
            
            elif "Aug" in x:
                x = x.replace("Aug", "August")
            if "September" in x:
                continue                
            
            elif "Sep" in x:
                x = x.replace("Sep", "September")
            if "October" in x:
                continue                
            
            elif "Oct" in x:
                x = x.replace("Oct", "October")
            if "November" in x:
                continue                
            
            elif "Nov" in x:
                x = x.replace("Nov", "November")                    
            if "December" in x:
                continue                    
            elif "Dec" in x:
                x = x.replace("Dec", "December")
            y = (datetime.datetime.strptime(x, '%d/%B/%Y').strftime('%A'))
            for day in Daytracker.keys():
                if y == day:
                    Daytracker[day]+=1
        else:
            continue


errors = 100 * float(errors)/float(TotalNumber)                    
            
redirects = 100 * float(redirects)/float(TotalNumber) 

maximum = max(mostrequested, key=mostrequested.get)
minumum = min(mostrequested, key=mostrequested.get)
              
print("The total number of request made in the time period represented by the log is %d" %(TotalNumber))
print("\n")
print("The following are the number of requests made in each month")
for key, value in Monthdict.items():
    print(key, value)
print("\n")    
print("The following are the number of requests made on each day")
for key, value in Daytracker.items():
    print(key, value)
print("\n")    
print("The following is the percentage of errors in the log file: %d%%" %(errors))
print("\n")
print("The following is the percentage of redirects in the log file: %d%%" %(redirects))
print("\n")
print("The following is the most requested file:")
print(maximum)
print("The following is the least requested file:")
print(minumum)

print(mostrequested)