import sublime, sublime_plugin
from telnetlib import Telnet

class MariCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):
		
		try:
			connection = Telnet('localhost', 6100)
		except:
			sublime.error_message("Enable command port in mari")
			return
		
		selections = self.view.sel()
		commands = []
		selSize = 0
		
		for sel in selections:
			if not sel.empty():
				selSize += 1
		
		if selSize == 0:
			
			filePath = self.view.file_name()
			if filePath is None:
				sublime.error_message("Save file")

			if self.view.is_dirty():
				sublime.error_message("Save changes")
				return
			
			content = self.view.substr(sublime.Region(0, self.view.size()))
			snips.extend(content.splitlines())
		
		else:
			for sel in selections:
				snips.extend( self.veiw.substr(sel).splitlines() )
		
		cmd = str('\n'.join(snips))
		
		connection.write(message)
		connection.write("\x04")
		connection.close()
