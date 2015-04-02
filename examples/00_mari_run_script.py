from mari_remote import MariRemote

remote = MariRemote('localhost', 6100)
remote.execfile('01_hello_world.py')