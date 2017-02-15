#!/usr/bin/env python
import subprocess
import re
import datetime
import os
dt = str(datetime.datetime.now())
#SEARCH LOG FILE AND GROUP LINES BY SESSION ID
def parsefile(logfile):
        f = open(logfile, "r")
        sessions = {}

        #read lines
        for line in f.readlines():
                id = line.split()[4]                            #session ID for line
                message = line.rpartition(']')[2]       #line message


                if has_value(sessions, id):
                        sessions[id]=str('\n'+line).rstrip('\n')  #store line in dict (key=id)(value=line) if this is the first observed session ID

                else:
                        sessions[id]=sessions[id]+message.rstrip('\n')  #append message to dict value (key=id)(value=message) if this is a known session ID append lines until new ID is observed

        #return dict of formatted log lines
        return sessions


#CHECK IF SESSION IF HAS BEEN SEEN BEFORE
def has_value(dic, key):
        try:
                dic[key]
                return False
        except KeyError:
                return True

if __name__ == "__main__":
        testfile="/var/log/inetsim/service.log"
        #logfile = "/var/log/inetsim/service.log"
        sessions = parsefile(testfile)

        #PRINT SESSIONS TO LOG FILE(CHANGE AS NEEDED)
        for id in sessions:
                #print(sessions[id])
                newfile = open("/var/log/inetsim/siem.txt", "a") #print inetsim service.log entries to new txt file, only appending the header data to the first line of the session
                logline = (sessions[id])
                newfile.write(logline)
        subprocess.call(['sort', '-n', '/var/log/inetsim/siem.txt', '-o', '/var/log/inetsim/siem.log']) #making sure the data in siem.log is sorted in proper order
        os.rename("/var/log/inetsim/service.log", "/var/log/inetsim/service_"+dt+".log") #create new service.log file so duplicated logs are not entered in to siem.txt
        name = '/var/log/inetsim/service.log'
        open(name, 'a')
        subprocess.call(['chmod', '0664', '/var/log/inetsim/service.log'])
        subprocess.call(['chown', ':inetsim', '/var/log/inetsim/service.log'])
