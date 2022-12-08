"""
social_media_accounts.py
Author: Ananya Bojja
Last updated: 12/7/2022
"""

import csv


class SocialMediaAccounts:
    """
        Represent a data-set of US startup Companies over time information.

        Concepts:
            Data processing functionality.
            Reading and writing from CSV files.
    """

    def __init__(self, filename):
        """
        Instance variable initialization
        :param filename: string
        """


    def read_data_to_dictionary(self, key_idx, value_idx):
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


    def firm_social_media_accounts(self) -> dict:
        """
        Creates and returns a dictionary whose keys are name of companies and
        values are no of social media accounts corresponding to that specific
        firm.
        :return: dictionary
            key: str, represents the company name
            value: integer, represents the no of social media accounts
        """


    def companies_list_same_social_accounts(self):
        """
        Gets dictionary of company names and their social media accounts count
         by calling self.firm_social_media_accounts and number of accounts can
          be extracted by calling "()"
        Creates and returns a new dictionary whose keys are no_social_accounts
            and value is a list of company names corresponding to the no of
            social media accounts.
        :returns: dictionary
           key: int, no of social media accounts associated with the company.
           value: list, list of companies corresponding to the no of
            social media accounts.
        """
