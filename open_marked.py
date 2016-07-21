import sublime, sublime_plugin, os

class OpenMarkedCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system('open -a \"Marked 2\" ' + self.view.file_name())
