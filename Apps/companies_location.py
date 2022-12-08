"""
companies_location.py
Author: Kalyan Kumar Gade
Last updated: 12/7/2021
"""

import csv


class CompanyLocation:
    """
    Data processing functionality
    Attributes:
        filename: string
    """
    def _init_(self, filename):
        """
        Instance variable initialization
        :param filename: string
        """


    def read_data_file_to_d(self, key_idx, value_idx, idx):
        """
        Reads from text file named self. filename using csv.reader() method
        and creates a dictionary with the data in column key_file as keys and
        data in column value_file as values.
        :param key_idx: non-negative integer, position of column in the
            text file, with the first column at position 0
        :param value_idx: non-negative integer, position of column in the
            text file, with the first column at position 0
        :return: dictionary
            key: string, representing data points in column key_idx
            value: string of corresponding values in column value_idx
        """


    def location_by_company_team_size(self):
        """
        Creates and returns a dictionary whose keys are location
         and values are list of company name and team_size.
        :return: dictionary
            key: str, represents location of the company
            value: list of str, integer, represents lists of company name and
            team_size
        """


    def company_loc_by_team_size(self):
        """
        Gets dictionary of date released and voting average by calling
            self.location_by_company_team_size().
        Creates and returns a new dictionary whose keys are location
            and value is a list of companies for a specific location.
        :returns: dictionary
           key: string, location
           value: a list of companies which are present in a particular
            location of type strings.
        """
