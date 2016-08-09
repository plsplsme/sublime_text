import sublime, sublime_plugin
import os
import sys

#
# Run paticular .bat file before save the current file.
#
# This script run "do_something_on_save.bat" on save if the file exists in project folder root.
#
# Currently Windows Only.
class DoSomethingOnSave(sublime_plugin.TextCommand):
	def run(self, edit):
		data = sublime.active_window().project_data()
		project_basedir = os.path.dirname(sublime.active_window().project_file_name()) + '\\' + data['folders'][0]['path']
		do_something_batch_name = project_basedir + '\\do_something_on_save.bat';
		do_something_batch_cmd  = project_basedir + '\\do_something_on_save.bat > ' + project_basedir + '\\do_something_on_save.log';

		if os.path.isfile(do_something_batch_name):
			sublime.message_dialog(do_something_batch_name)
			sublime.active_window().run_command("exec", {"cmd": do_something_batch_cmd, "shell": True })

		#No matta what we save file
		sublime.active_window().run_command("save", {"encoding": "utf-8" })
