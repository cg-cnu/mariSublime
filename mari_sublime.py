#!/usr/bin/python
import os
import re
import sys
import sublime
import sublime_plugin
from telnetlib import Telnet


def message(message):
    """ Display message to the user
    """
    return sublime.error_message("mariSublime: {}".format(message))


class MariRemote:
    """ Mari Remote connection
    """

    def __init__(self, host="127.0.0.1", port=7002):
        """construct
        Args:
            host (str): name of the host
            remote (int: port number
        """
        self.host = host
        self.port = port

    def __call__(self, code):
        """evaluate given python code

        Args:
            code (str): python code string
        """
        try:
            connection = Telnet(self.host, self.port)
        except ConnectionRefusedError:
            message(
                "Connection refused on host {} at port {}.".format(self.host, self.port)
            )
            return

        if sys.version_info[0] < 3:
            connection.write(code)
            connection.write("\x04")
        else:
            connection.write(code.encode(encoding="UTF-8"))
            connection.write("\x04".encode(encoding="UTF-8"))

        connection.close()


class send_to_mariCommand(sublime_plugin.TextCommand):
    """send to Mari
    """

    def run(self, edit):
        """run command
        """
        syntax = self.view.settings().get("syntax")
        if not re.search(r"python", syntax, re.I):
            message("Not a valid Language")
            return

        file_path = self.view.file_name()
        if file_path is None:
            message("Please save the file")
            return

        if self.view.is_dirty():
            message("Please save the changes")
            return

        snippets = []
        selection_size = 0

        for selection in self.view.sel():
            if not selection.empty():
                selection_size += 1
                snippets.extend(self.view.substr(selection).splitlines())

        if selection_size == 0:
            content = self.view.substr(sublime.Region(0, self.view.size()))
            snippets.extend(content.splitlines())

        cmd = str("/n".join(snippets))

        settings = sublime.load_settings("mariSublime.sublime-settings")
        remote = MariRemote(settings.get("host"), settings.get("port"))

        remote(cmd)
