"""all common code for mari remote
"""
import sys
from telnetlib import Telnet

class MariRemote(object):
    """remote system for mari
    """
    def __init__(self, host, port):
        """construct
        Args:
            host (str): name of the host
            remote (int: port number
        """
        self.host = host
        self.port = port

    def execfile(self, script):
        """run given script file

        Args:
            script (str): filepath to a python script
        """
        cmd = 'execfile("%s")' % script
        self.eval(cmd)

    def eval(self, code):
        """evaluate given python code

        Args:
            code (str): python code string
        """
        connection = Telnet(self.host, self.port)

        # write
        if sys.version_info[0] < 3:
            connection.write(code)
            connection.write("\x04")
        else:
            connection.write(code.encode(encoding='UTF-8'))
            connection.write("\x04".encode(encoding='UTF-8'))

        connection.close()

    def construct_open_port_code(self):
        """return string that is needed for mari to open a port
        """
        return """mari.app.enableCommandPort( not ( mari.app.commandPortEnabled() ) )"""