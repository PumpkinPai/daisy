#!/usr/bin/python3

"""
Daisy speech queue reader:
Reads from tosay/ folder, text files in order of importance and time
Files in tosay/ are prepended by a # (lower is more important)
ex: tosay/001-2015-03-14-143001-printcomplete.txt
(important msg, print complete on 3/14/2015 at 2:30:01pm)
If time stamp is older than current time by more than a few minutes,
state the time it happened.
Then moves them to said/folder or log file
"""

'''
TODO:
    -Turn this into a daemon that dies with main process
    -Using 3 digit prefix on textfile names, decide whether to read
and archive immediately or to keep in queue until attention has been confirmed.
Also, provide a way to confirm things, or in effect ask questions of particular
household members.
    -Check to see if talking is allowed at present time.
        -Hold queue until it is and add "At blah blah, this happened..."
        -Add "at blah blah, this happened" to english.yaml
'''

import os, time, subprocess
# import daisy_config

def say(shellcall, txtfile):
    # debug
    #print(shellcall, txtfile)
    subprocess.call(shellcall, shell=True)


# Take a source text file's contents and append it to destination text file
# Then delete source text file
def archive(sourceText, destination):
    pass # temp
    
    
def repeatLastMsg():
    # Get last message in directory
    for file in os.listdir(saidDir):
        if file.endswith('.txt'):
            pass # temp
            

# Get first file in tosay/ folder
def msgReader():
    # sayDir = os.getenv('HOME') + '/.daisy/tosay/'
    # saidDir = os.getenv('HOME') + '/.daisy/tosay/said/'
    sayDir = os.getcwd() + '/tosay/'
    saidDir = os.getcwd() + '/tosay/said/' # change this to archived actions searchable by actionType field

    # get speech config from daisy_main.yaml
    conf = daisy_config.getConf('main') # broken (needs to be a config class)
    
    for file in os.listdir(sayDir):
        if file.endswith('.txt'):
            # These are set here in case we want voice options in the text file
            # This could enable dialogues given by Daisy
            cmd = conf['speech']['command']
            arg = conf['speech']['arg']
            voice = conf['speech']['voice']
            
            '''msg = open(sayDir + file).read()
            msg = msg.rstrip('\n')'''
            txtfile = sayDir + file
            # Debug
            #print(file)
            # Construct flite arguments
            argmnt = arg.format(v=voice) + '"' + txtfile + '"'
            shellcall = cmd + argmnt
            say(shellcall, txtfile)
            
            # Move utterance to '/tosay/said/saidlog.txt' file
            #archive(sayDir, file)
            
            #os.rename(sayDir + file, saidDir + file)
            
            
            # Give a pause between utterances
            time.sleep(1.0)
    
    # Give the system a break
    time.sleep(2.0)
    
    #repeatLastMsg()
        
if __name__ == "__main__":
    msgReader()
        
