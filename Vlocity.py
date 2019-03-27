import unittest
import sys


class StringSplitter(object):
    """
    This class is used for splitting strings into lists of substrings
    based on the delimiters set.

    """

    def __init__(self, *seps):
        """
        @summary: Initializes an object representing 2 or more delimiters
                  based on which any input string will be split.
        @param seps: Tuple of Seperators acting as delimiters
        @type seps: Tuple
        """
        self.sep_list = seps

    def __str__(self):

        return "class to split the strings"

    @staticmethod
    def _validate_ip_string(input_str):
        """
        @summary: Validate the input data/string provided by the user,
                  to be an object of basestrin or its subclss
        @param input_str: input string to split.
        @type input_str: basestring
        @return: None
        """

        if not isinstance(input_str, basestring):
            print("Invalid Input: Input is of type:%s " % type(input_str))
            sys.exit(-1)  # terminate the execution as input is not a string.

    def split_string(self, input_str):
        """
        @summary: Split the string provided using the delimiters of the class object
        @param input_str: Input strig that needs to be split
        @type: basestring
        @return: list of substrings split from actual string
        @type: List
        """

        # Validate the input string is valid.

        StringSplitter._validate_ip_string(input_str)

        # Initialize the substring list to the actual string.
        subs = [input_str]

        # Logic to generate the list of substrings generated from parent string
        # using the delimiters of the class object.

        for sep in self.sep_list:
            s, subs = subs, []
            for seq in s:
                subs += seq.split(sep)

        return subs


class test_String_Splitter(unittest.TestCase):

    def test_split_string_all_delim(self):

        my_string = StringSplitter('$', '&', '#')
        my_substring = my_string.split_string('Kapil$Mathur&Accion#Employee')
        self.assertEquals(my_substring, ['Kapil', 'Mathur', 'Accion', 'Employee'])

    def test_split_string_one_delim(self):

        my_string = StringSplitter('$')
        my_substring = my_string.split_string('Kapil$Mathur&Accion#Employee')
        self.assertEquals(my_substring, ['Kapil', 'Mathur&Accion#Employee'])

    def test_split_string_two_delim(self):

        my_string = StringSplitter('$', '&')
        my_substring = my_string.split_string('Kapil$Mathur&Accion#Employee')
        self.assertEquals(my_substring, ['Kapil', 'Mathur', 'Accion#Employee'])

    def test_split_string_no_delim(self):

        my_string = StringSplitter()
        my_substring = my_string.split_string('Kapil$Mathur&Accion#Employee')
        self.assertEquals(my_substring, ['Kapil$Mathur&Accion#Employee'])


if __name__ == '__main__':
    unittest.main()



