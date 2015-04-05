#!/usr/bin/python3

#  DAISY MAIN!!!

import daisy_speech


def getConf(whichConfig):
    from os import getenv
    import yaml

    confFile = getenv('HOME') + '/.daisy/config/' + whichConfig +'.yaml'

    with open(confFile, 'r') as f:
        conf = yaml.load(f)
        
    return conf

def checkActions()
    pass
    # check actions folder for actions. Leave actions that are not due.
    action = '' 
    return action


if __name__ == "__main__":

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
    
