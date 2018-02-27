from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

TotalNumber = 0
log = 'local_copy.log'


Monthdict = {"Jan":0, "Feb":0, "Mar":0, "Apr":0, "May":0, "Jun":0, "Jul":0, "Aug":0, "Sep":0, "Oct":0, "Nov":0, "Dec":0}

for month in Monthdict.keys():
    for line in open(log):
        TotalNumber += 1
        if month in line:
            Monthdict[month] += 1

print("The total number of request made in the time period represented by the log is %d" %(TotalNumber))


for key, value in Monthdict.items():
    print(key, value)