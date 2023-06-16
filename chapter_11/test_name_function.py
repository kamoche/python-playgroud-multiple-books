import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test name_function"""

    def test_first_last_name(self):
        """Do name like Kamoche Jackson works"""
        formatted_name = get_formatted_name('kamoche', 'jackson')
        self.assertEqual(formatted_name,'Kamoche jackson')

    def test_first_middle_last_name(self):
        """Do name like kamoche Githinji Works"""
        formatted_name =get_formatted_name('Kamoche','Jackson','githinji')
        self.assertEqual(formatted_name,'Kamoche Githinji Jackson')

unittest.main()


