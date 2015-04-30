import sublime, sublime_plugin
# How to activate?
# 1. Ctrl+`
# 2. view.run_command(commandname)
class DeleteVariableSymbolCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                pos = region.begin()
                check_region = sublime.Region(pos,pos-1)

                if self.view.substr(check_region) == '$':
                    self.view.erase(edit,check_region)
