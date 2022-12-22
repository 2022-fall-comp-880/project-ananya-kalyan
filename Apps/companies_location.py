"""
Represents a data_set of US_startup Companies over time information.

Author: Kalyan Kumar Gade
Last updated: 12/7/2021
"""

import csv


class CompanyLocation:
    """
    Represents a data_set of US_startup Companies over time information.

    Attributes:
        filename: string
    """

    def __init__(self, filename):
        """
        Instance variable initialization.

        :param filename: string
        """
        self.filename = filename

    def read_data_file_to_d(self, key_idx: int, value_idx: int,
                            idx: int) -> dict:
        """
        Read data from a text file into a dict.

        Reads from text file named `self.filename` using `csv.reader()` method
        and creates a dictionary with the data in column key_file as keys and
        data in column value_file as values.

        :param key_idx: non-negative integer, position of column in the
            text file, with the first column at position 0
        :param value_idx: non-negative integer, position of column in the
            text file, with the first column at position 0
        :param idx: non-negative integer, position of column in the
            text file, with the first column at position 0

        :return: dictionary
            key: string, representing data points in column key_idx
            value: string of corresponding values in column value_idx
        """
        startups_dict = {}
        with open(self.filename, encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for count, row in enumerate(reader):
                if count != 0:  # skip first row that has the headings
                    key = row[key_idx]
                    value = row[value_idx]
                    a_val = row[idx]
                    if key in startups_dict:
                        startups_dict[key].append([value, a_val])
                    else:
                        startups_dict[key] = [[value, a_val]]
        return startups_dict

    def location_by_company_team_size(self) -> dict:
        """
        Create a dictionary of location with company team size.

        Creates and returns a dictionary whose keys are location and
        values are list of company name and team_size.

        :return: dictionary
            key: str, represents location of the company
            value: list of str, integer, represents lists of company name and
            team_size
        """
        location_idx = 6
        company_name_idx = 1
        team_size_idx = 5
        location_with_comp_size_dict =\
            self.read_data_file_to_d(location_idx,
                                     company_name_idx, team_size_idx)
        return location_with_comp_size_dict

    def company_loc_by_team_size(self) -> dict:
        """
        Create a dictionary of location of company list by team size.

        Gets dictionary of location and list of companies for a specific
         location by calling self.location_by_company_team_size().

        Creates and returns a new dictionary whose keys are location
        and value is a list of companies for a specific location.

        :returns: dictionary
           key: string, location.
           value: list of strings, a list of companies which are present in
           a particular location.
        """
        company_location_dict = self.location_by_company_team_size()
        company_location = {}
        for locations, company_list in company_location_dict.items():
            for team_size in company_list:
                if int(team_size[1]) >= 500:
                    if locations in company_location:
                        company_location[locations].append(team_size[0])
                    else:
                        company_location[locations] = [team_size[0]]
        return company_location
