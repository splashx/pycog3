from testbundle.commands.level1.level2.level3.base import Level3


class Commandd(Level3):
    def __init__(self):
        super().__init__()

    def run(self):
        self.run_command()

    def run_command(self):
        level = self.level3_function()
        level = level + "d"
        self.response.content(level, template="template").send()