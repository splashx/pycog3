from testbundle.commands.level1.base import Level1

class Level2a(Level1):
    def run(self):
        pass

    def __init__(self):
        super().__init__()

    def level2a_function(self):
        return "2a" #string 0 representing level 0

    def level2b_function(self):
        return "2a" #string 0 representing level 0
