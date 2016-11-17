import sublime, sublime_plugin, os

class OpenMarkedCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path = self.view.file_name()
		if path.endswith(".md"):
			os.system('open -a \"Marked 2\" \"' + self.view.file_name() + "\"")
		else:
			sublime.message_dialog("not markdown file")
