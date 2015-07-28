import sublime, sublime_plugin
import re

"""
#HOW
 1. put cursor on the word (any position should work)
 2. Ctrl+`
 3. view.run_command('add_variable_symbol')

#EXAMPLE OF KEY MAPPING
{ "keys": ["alt+4"], "command": "add_variable_symbol", "args": {"language": "PHP"}},


#TODO
 - check if the symbol has been already out there[must]
 - check if current word is function[may]
 - add symbol to multiple selected words[may]
 - add languages[may]
"""

class AddVariableSymbol(sublime_plugin.TextCommand):
    regs = {'PHP':'[a-zA-Z0-9_]+'}
    symbols = {'PHP':'$'}

    def run(self, edit, **args):
        #get current word
        current_word_region = self.view.word(self.view.sel()[0].begin())
        current_word = self.view.substr(current_word_region)

        #add symbol
        if (self.checkIfVariable(current_word,args['language'])):
            self.addSymbol(edit,current_word_region,args['language'])

    #chck if the string is variable
    def checkIfVariable(self,string,lang):
        reg = self.regs[lang]
        if (re.match(reg,string)):
            return True
        else:
            return False

    #add symbol to the top of word
    def addSymbol(self,edit,current_word_region,lang):
        symbol = self.symbols[lang]
        add_point = current_word_region.begin()
        self.view.insert(edit, add_point, symbol)

