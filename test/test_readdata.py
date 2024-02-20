import unittest
import os
import sys
application_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(application_path+'..'))
from Dialogs import LoadMacros, GetFunctionList


class STMThread_test(unittest.TestCase):
    def test_ReadMacro(self):
        application_path = os.path.dirname(__file__)
        os.chdir(os.path.realpath(application_path))
        ThisMacro = LoadMacros("datafiles\\TestMacro.json")
        
    def test_ReadFunctions(self):
        application_path = os.path.dirname(__file__)
        os.chdir(os.path.realpath(application_path))
        TheseFunctions = GetFunctionList("datafiles\\TestFunctions.py")

if __name__ == '__main__':
    unittest.main()