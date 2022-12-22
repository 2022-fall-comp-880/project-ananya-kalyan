"""
Represents a data_set of US_startup Companies over time information.

Author: Ananya Bojja
Last updated: 12/7/2022
"""

import csv


class SocialMediaAccounts:
    """
        Represent a data-set of US_startup Companies over time information.

        Attributes:
        filename: string
    """

    def __init__(self, filename):
        """
        Initialize instance variables.

        Parameters:
            filename: string
        """
        self.filename = filename

    def read_data_to_dictionary(self, key_idx: int, value_idx: int) -> dict:
        """
        Read data from a text file into a dict.

        Reads from text file named `self.filename` using `csv.reader()` method
        and creates a dictionary with the data in column `key_idx` as keys and
        data in column `value_idx` as values.
        :param key_idx: non-negative integer, position of column in the
            text file, with the first column at position 0

        :param value_idx: non-negative integer, position of column in the
            text file, with the first column at position 0

        :return: dictionary
            key: string, representing data points in column `key_idx`
            value: string of corresponding values in column `value_idx`
        """
        startups_dict = {}
        with open(self.filename, encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for count, row in enumerate(reader):
                if count != 0:  # skip first row that has the headings
                    key = row[key_idx]
                    value = int(row[value_idx])
                    startups_dict[key] = value
        return startups_dict

    def firm_social_media_accounts(self) -> dict:
        """
        Create a dictionary of company social media accounts.

        Creates and returns a dictionary whose keys are name of companies and
        values are no of social media accounts corresponding to that specific
        firm.

        :return: dictionary
            key: str, represents the company name
            value: integer, represents the no of social media accounts
        """
        company_name_idx = 1
        no_company_socials_idx = 9
        no_of_social_accounts_dict = self.read_data_to_dictionary(
            company_name_idx,
            no_company_socials_idx)
        return no_of_social_accounts_dict

    def companies_list_same_social_accounts(self):
        """
        Create a dictionary of same social media with company list.

        Gets dictionary of company names and their social media accounts count
         by calling self.firm_social_media_accounts.

        Creates and returns a new dictionary whose keys are no_social_accounts
            and value is a list of company names corresponding to the no of
            social media accounts.

        :returns: dictionary
           key: integer, no of social media accounts associated with the
           company.
           value: list of strings, list of companies corresponding to the no of
            social media accounts.
        """
        social_accounts_d = self.firm_social_media_accounts()
        no_social_accounts_dict = {}
        for no_social_accounts, company_list in social_accounts_d.items():
            if company_list in no_social_accounts_dict:
                no_social_accounts_dict[company_list].append(
                    no_social_accounts)
            else:
                no_social_accounts_dict[company_list] = [no_social_accounts]

        return no_social_accounts_dict
