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
    Represents a data_set of Us_startup Companies over time information.

    Attributes:
        filename: string
    """
    def __init__(self, filename):
        """
        Instance variable initialization.

        :param filename: string
        """
        self.filename = filename

    def read_data_file_to_d(self, value: int) -> list:
        """
        Reads from text file named `self.filename` using `csv.reader()` method
        and creates a dictionary with the data in column key_file as keys and
        data in column value_file as values.
        :param value: non-negative integer.
        :return: list
            value: list of integers, list of founded year of the companies.
        """
        year_list = []
        with open(self.filename, encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for count, row in enumerate(reader):
                if count != 0:
                    key = row[value]
                    year_list.append(key)
        return year_list


    def company_social_accounts(self):
        """
        Creates and returns a dictionary whose keys are founded year of
        and values are no of companies founded in the year corresponding to that year.
        :return: dictionary
            key: integer, represents the year founded
            value: integer, represents the no of companies founded in that year.
        """
        no_company_socials = 4
        comp_social_accounts_dict = self.read_data_file_to_d(no_company_socials)
        return comp_social_accounts_dict


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
        companies_founded_year_d = {}
        year = self.company_social_accounts()
        for no_companies in year:
            if no_companies == "-1":
                if "unknown" in companies_founded_year_d:
                    companies_founded_year_d["unknown"] += 1
                else:
                    companies_founded_year_d["unknown"] = 1
            else:
                if no_companies in companies_founded_year_d:
                    companies_founded_year_d[no_companies] += 1
                else:
                    companies_founded_year_d[no_companies] = 1
        return companies_founded_year_d




