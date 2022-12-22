"""Test Company founded year count."""

import unittest
import os
from Apps.company_founded_year_count import CompanyFoundedYear


class TestCompanyFoundedYearCount(unittest.TestCase):
    """Test `company_founded_year_count()` method."""

    def setUp(self):
        """Create objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.startups_stats = CompanyFoundedYear(
            f'{data_dir}/Startup_data.csv')
        self.startups_stats_empty = CompanyFoundedYear(
            f'{data_dir}/Startup_data_empty.csv')
        self.startups_stats_First5 = CompanyFoundedYear(
            f'{data_dir}/Startup_data_First5.csv')
        self.startups_stats_Last10 = CompanyFoundedYear(
            f'{data_dir}/Startup_data_Last10.csv')

    def test_multiple_entries(self):
        """Test case 1 using Startup_data.csv."""
        actual_res = self.startups_stats.no_of_companies_founded()
        print(self.startups_stats.company_founded_year())
        print(actual_res)
        expected_res = {'2008': 6, '2012': 44, 'unknown': 167, '2016': 30, '2009': 5, '2017': 45, '2020': 80, '2011': 29, '2013': 36, '2018': 39, '2015': 64, '2014': 50, '2019': 52, '2021': 195, '2006': 2, '2007': 2, '2010': 2, '2022': 152}
        self.assertEqual(actual_res, expected_res)

    def test_empty(self):
        """Test case 2 using Startup_data_empty.csv."""
        actual_res1 = self.startups_stats_empty.no_of_companies_founded()
        print(self.startups_stats_empty.company_founded_year())
        print(actual_res1)
        expected_res1 = {}
        self.assertEqual(actual_res1, expected_res1)

    def test_first_five_entries(self):
        """Test case 3 using Startup_data_First5.csv."""
        actual_res2 = self.startups_stats_First5.no_of_companies_founded()
        print(self.startups_stats_First5.company_founded_year())
        print(actual_res2)
        expected_res2 = {'2008': 2, '2012': 2, 'unknown': 1}
        self.assertEqual(actual_res2, expected_res2)

    def test_last_ten_entries(self):
        """Test case 4 using Startup_data_Last10."""
        actual_res3 = self.startups_stats_Last10.no_of_companies_founded()
        print(self.startups_stats_Last10.company_founded_year())
        print(actual_res3)
        expected_res3 = {'2021': 3, '2020': 2}
        self.assertEqual(actual_res3, expected_res3)
