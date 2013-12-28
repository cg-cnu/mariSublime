import sublime, sublime_plugin
from telnetlib import Telnet

class MariCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			connection = Telnet('localhost', 6100)
			sels = self.view.sel()
			for sel in sels:
				message = str(self.veiw.substr(sel))
				connection.write(message)
				connection.write("\x04")
			connection.close()
		except:
			sublime.error_message("Enable command port in mari")
			
