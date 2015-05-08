#!/usr/bin/python3

#  DAISY MAIN!!!


import daisy_speech
import os
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
    # daisyDir = '~/daisy/config/' # (these are the masters, loaded with defaults)
    daisyDir = '~/git/daisy/config/' # temp
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


def checkActions():
    pass
    # check actions folder for actions. Leave actions that are not due.
    action = '' 
    return action


if __name__ == "__main__":
    # Check user configs against installation and add new entries
    # (this also performs the first run installation of configs)
    initConf()

    # Open config file and run that which is true
    conf = getConf('main')
    
    if conf['speech']['enabled'] == True:
        daisy_speech.msgReader()
        print('should have said something...')
    
    # Debug
    print(conf['speech']['enabled'])

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
    
