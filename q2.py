class Person(object):
    def __init__(self, name):
        self.name = name
    last_word = "word"
    def say(self, stuff):
        self.last_word = stuff
        return stuff
    def ask(self, stuff):
        return self.say("Would you please " + stuff)
    def greet(self):
        return self.say("Hello, my name is " + self.name)
    def repeat(self):
        return self.last_word

class DoubleTalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def say(self, stuff):
        return Person.say(self, stuff + " " + stuff)