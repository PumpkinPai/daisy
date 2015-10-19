#!/usr/bin/python3

#  DAISY MAIN!!!


import daisy_speech
import os
import time
import yaml

def getConf(whichConfig):

    # confFile = getenv('HOME') + '/.daisy/config/' + whichConfig +'.yaml'
    confFile = os.getcwd() + '/config/' + whichConfig + '.yaml'

    with open(confFile, 'r') as f:
        conf = yaml.load(f)

    return conf

# check ~/.daisy for config files and add missing entries from new features
# found in ~/daisy/config files
def initConf():
    userDir = '~/.daisy/config/'
    currentDir = os.getcwd()
    daisyDir = currentDir + '/config/' # (these are the masters, loaded with defaults)
    print(daisyDir)
    daisyFilenames = []

    # todo- Get all config filenames from daisyDir
    for i in daisyFilenames:
        daisyFile = open(daisyDir + daisyFilenames[i], 'r')
        daisySettings = yaml.load(daisyFile)
        daisyFile.close

        try:
            # userFile found, merge with daisyFile
            userFile = open(userDir + daisyFilenames[i], 'r')
            userSettings = yaml.load(userFile)
            userFile.close
            # todo- merge
        except Exception as e:
            # Probably a new installation or new feature
            try:
                os.mkdir('~/.daisy')
                os.mkdir('~/.daisy/config')
            except: pass
            newSettings = daisySettings

        userFile = open(userDir + daisyFileNames[i], 'w')
        userFile.write(yaml.dump(newSettings, default_flow_style=True))
        userFile.close


def checkActions(timeNow):
    # timeNow is a dict with 'year', 'month', 'day', 'minutes' values
    # timeNow['minutes'] is minutes since midnight
    # check actions folder for actions. Leave actions that are not due.
    taskDir = '/home/pumpkin/.daisy/tasks/'
    actionFilenames = []

    # get urgent actions regardless of time
    for f in os.listdir(taskDir):
        if f.endswith('.urgent'):
            actionFilenames.append(f)
    if actionFilenames != []:
        actionFilenames.sort()
        return taskDir + actionFilenames[0]

    # look at normal tasks and check for due actions
    for f in os.listdir(taskDir):
        if f.endswith('.task'):
            actionFilenames.append(f)
    if actionFilenames != []:
        actionFilenames.sort()
        return taskDir + actionFilenames[0]

    return False


def performAction(actionFilename):
    actionFile = open(actionFilename, 'r')
    # todo- might as well use yaml files for tasks too
    action = yaml.load(actionFile)
    actionFile.close()
    if action['action'] == 'say':
        daisy_speech.say(action['contents'])


if __name__ == "__main__":
    # Check user configs against installation and add new entries
    # (this also performs the first run installation of configs)
    initConf()

    # Open config file and run that which is true
    conf = getConf('main')

    if conf['speech']['enabled'] == True:
        #daisy_speech.msgReader()
        print('talk talk...')

    # Debug
    print(conf['speech']['enabled'])

    # wakeStart and wakeEnd are minutes since midnight
    wakeStartStr = conf['waketime']['start'].split(':')
    wakeEndStr = conf['waketime']['end'].split(':')
    wakeStart = int(wakeStartStr[0]) * 60 + int(wakeStartStr[1])
    wakeEnd = int(wakeEndStr[0]) * 60 + int(wakeEndStr[1])
    print(str(wakeStart))

    # Main loop
    while True:
        print('entering main loop')
        action = []
        awake = False
        # timeNow is number of minutes since midnight
        minNow = int(time.strftime("%H")) * 60 + int(time.strftime("%M"))
        dateNow = [time.strftime("%Y"), time.strftime("%m"), time.strftime("%d")]
        timeNow = {'minutes': minNow, 'year': int(time.strftime("%Y")), 'month': int(time.strftime("%m")), 'day': int(time.strftime("%d"))}
        print(str(timeNow))
        if timeNow['minutes'] > wakeStart and timeNow['minutes'] < wakeEnd:
            awake = True
        actionFilename = checkActions(timeNow)
        if actionFilename:
            if actionFilename.endswith('.urgent') or awake == True:
                performAction(actionFilename)
                print('actionFilename: ' + actionFilename)
                # todo- logAction(actionFilename)
        else:
            pass


        time.sleep(1)

    #daisy tasks are initiated on a repeating schedule
    #tasks are modular with each being its own .py file
    #

    #do something every minute
        #do .py files in minutely folder
            #for example check email or check for person-tasks

    #do something every 10 minutes
        #do .py files in quarter-hourly folder
            #for example check and adjust room temps

    #do something every hour

    #do things that are time specific

    # OOOOORRRRRRR

    #check once a minute for daisy tasks that are scheduled for that time
        #daisy tasks could be pickles, set from a gui (or shelves (better))
    
