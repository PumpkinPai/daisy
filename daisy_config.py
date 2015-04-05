#!/usr/bin/python3

"""
This has been depreciated (it was so small I just stuck it in the main)
This will be done for other simple core functions

This is the main config parser for DAISY
It reads configs/daisy.yaml and assigns values to variables
That's all.
"""

def getConf(whichConfig):
    from os import getenv
    import yaml

    confFile = getenv('HOME') + '/.daisy/config/' + whichConfig +'.yaml'

    with open(confFile, 'r') as f:
        conf = yaml.load(f)
        
    return conf


if __name__ == '__main__':
    getConf()
