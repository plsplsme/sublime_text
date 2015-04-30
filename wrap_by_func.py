import sublime, sublime_plugin
# How to activate?
# 1. Ctrl+`
# 2. view.run_command(commandname)
class WrapByFuncCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("delete_variable_symbol")
        self.view.run_command("insert_snippet", { "name": "Packages/User/snippet/php_wrap_by_func.sublime-snippet"} )
