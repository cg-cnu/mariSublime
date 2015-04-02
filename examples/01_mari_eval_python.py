"""example snippet to eval python code
"""
from mari_remote import MariRemote
remote = MariRemote('localhost', 6100)
remote.eval('print "adsf"')