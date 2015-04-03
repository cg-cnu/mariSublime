#!/usr/bin/python
import os
import sys
import sublime
import sublime_plugin
from telnetlib import Telnet

HOST = 'localhost'
PORT = 6100

def append_lib_in_sys_paths():
    """add library in sys path
    """
    lib_dir = os.path.abspath(os.path.join(__file__, '..', 'lib'))

    if lib_dir not in sys.path:
        sys.path.append(lib_dir)

class MariCommand(sublime_plugin.TextCommand):
    """send a sublime remote command 
    """
    def run(self, edit):
        """run command
        """
        append_lib_in_sys_paths()

        import mari_remote
        remote = mari_remote.MariRemote(HOST, PORT)
        
        selections = self.view.sel()
        snips = []
        selSize = 0
        
        for sel in selections:
            if not sel.empty():
                selSize += 1
        
        if selSize == 0:
            
            filePath = self.view.file_name()
            if filePath is None:
                sublime.error_message("Save file")
                return

            if self.view.is_dirty():
                sublime.error_message("Save changes")
                return
            
            content = self.view.substr(sublime.Region(0, self.view.size()))
            snips.extend(content.splitlines())
        
        else:
            for sel in selections:
                snips.extend( self.view.substr(sel).splitlines() )
        
        cmd = str('\n'.join(snips))
        
        remote.eval(cmd)
        