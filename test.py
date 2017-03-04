#!/usr/bin/python


class myClass(object):

    def __init__(self):
        self.name = "newName"

    def change(self):
        self.name = "changedName"

    def _print(self):
        print self.name





c = myClass()
c._print()
c.change()
c._print()

print "done"
