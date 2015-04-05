#!/usr/bin/python3

import subprocess


class Subproc:
    def subp(cmd, arg):
    	return subprocess.call([cmd, arg])

print("next command")
