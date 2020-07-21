class Person(object):
    def __init__(self, name):
        self.name = name
    last_word = "word"
    def say(self, stuff):
        last_word = stuff
        return stuff
    def ask(self, stuff):
        return self.say("Would you please " + stuff)
    def greet(self):
        return self.say("Hello, my name is " + self.name)
    def repeat(self):
        last = Person.last_word
        return last
