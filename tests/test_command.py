import os
import unittest
from subprocess import check_output

# test summary for command
# `!commanda
# `!level1 - commanda
# `!level1 - level2a - commandc
# `!level1 - level2b - leveln - commandz

class TestCommand(unittest.TestCase):

    fixed_output_prefix = "COG_TEMPLATE: template\nJSON\n"

    def setUp(self):
        os.environ['dyn_config_var1'] = '1'
        os.environ['COG_BUNDLE'] = 'testbundle'
        pass

    def test_level0(self):
        os.environ['COG_COMMAND'] = 'commanda'
        result = check_output(["cog-command"])

        self.assertEqual(result.decode("utf-8"), self.fixed_output_prefix + '"0a"\n')

    def test_level1_commandb(self):
        os.environ['COG_COMMAND'] = 'level1-commandb'
        result = check_output(["cog-command"])

        self.assertEqual(result.decode("utf-8") , self.fixed_output_prefix+'"1b"\n')

    def test_level1_level2a_commandb(self):
        os.environ['COG_COMMAND'] = 'level1-level2a-commandc'
        result = check_output(["cog-command"])

        self.assertEqual(result.decode("utf-8"), self.fixed_output_prefix + '"2ac"\n')

    def test_level1_level2b_leveln_commandz(self):
        os.environ['COG_COMMAND'] = 'level1-level2b-leveln-commandz'
        result = check_output(["cog-command"])

        self.assertEqual(result.decode("utf-8"), self.fixed_output_prefix + '"nz"\n')


if __name__ == '__main__':
    unittest.main()