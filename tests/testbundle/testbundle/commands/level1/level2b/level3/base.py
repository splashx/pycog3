from testbundle.commands.level1.level2b.base import Level2b

class Level3(Level2b):
    def run(self):
        pass

    def __init__(self):
        super().__init__()

    def level3_function(self):
        return "3"