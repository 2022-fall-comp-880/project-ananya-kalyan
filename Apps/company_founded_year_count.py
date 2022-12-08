"""
company_founded_year_count.py
Authors:
  - Ananya Bojja
  - Kalyan Kumar Gade
Created : 12/7/2021
"""

import csv


class CompanyFoundedYear:
    """
    Data processing functionality
    Attributes:
        filename: string
    """
    def __init__(self, filename):
        """
        Instance variable initialization
        :param filename: string
        """
        self.filename = filename

    def read_data_file_to_d(self, key_idx, value_idx):
        """
        Reads from text file named self.filename using csv.reader() method
        and creates a dictionary with the data in column key_file as keys and
        data in column value_file as values.
        :param key_idx: non-negative integer, position of column in the
            text file, with the first column at position 0
        :param value_idx: non-negative integer, position of column in the
            text file, with the first column at position 0
        :return: dictionary
            key: integer, representing data points in column key_idx
            value: string of corresponding values in column value_idx
        """


    def company_social_accounts(self):
        """
        Creates and returns a dictionary whose keys are founded year of
        and values are no of companies founded in the year corresponding to that year.
        :return: dictionary
            key: integer, represents the year founded
            value: integer, represents the no of companies founded in that year.
        """


    def no_of_companies_founded(self):
        """
        Gets dictionary of year founded and voting average by calling
            self.company_social_accounts().
        Creates and returns a new dictionary whose keys are the year founded
            and value is total no of companies founded in specific year
        :returns: dictionary
           key: int, founded_year
           value: int, no of companies founded in specific year
        """





