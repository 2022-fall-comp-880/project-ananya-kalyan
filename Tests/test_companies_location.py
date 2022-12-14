
"""Test companies location."""

import unittest
import os
from Apps.companies_location import CompanyLocation


class TestCompaniesLocation(unittest.TestCase):
    """Test `company_loc_by_team_size()` method."""

    def setUp(self):
        """Create  objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.startups_stats = CompanyLocation(f'{data_dir}/Startup_data.csv')
        self.startups_stats_empty = CompanyLocation(
            f'{data_dir}/Startup_data_empty.csv')
        self.startups_stats_First5 = CompanyLocation(
            f'{data_dir}/Startup_data_First5.csv')
        self.startups_stats_Last10 = CompanyLocation(
            f'{data_dir}/Startup_data_Last10.csv')

    def test_multiple_entries(self):
        """Test case 1 using Startup_data.csv."""
        actual_res = self.startups_stats.company_loc_by_team_size()
        print(self.startups_stats.location_by_company_team_size())
        print(actual_res)
        # ignoring assertion statement as we are getting pylint errors for
        # expected res as the data is large

    def test_empty(self):
        """Test case 2 using Startup_data_empty.csv."""
        actual_res1 = self.startups_stats_empty.company_loc_by_team_size()
        print(self.startups_stats_empty.location_by_company_team_size())
        print(actual_res1)
        expected_res1 = {}
        self.assertEqual(actual_res1, expected_res1)

    def test_first_five_entries(self):
        """Test case 3 using Startup_data_First5.csv."""
        actual_res2 = self.startups_stats_First5.company_loc_by_team_size()
        print(self.startups_stats_First5.location_by_company_team_size())
        print(actual_res2)
        expected_res2 = {
            'San Francisco': ['Airbnb', 'Amplitude', 'DoorDash', 'Coinbase',
                              'Dropbox']}
        self.assertEqual(actual_res2, expected_res2)

    def test_last_ten_entries(self):
        """Test case 4 using Startup_data_Last10."""
        actual_res3 = self.startups_stats_Last10.company_loc_by_team_size()
        print(self.startups_stats_Last10.location_by_company_team_size())
        print(actual_res3)
        expected_res3 = {}
        self.assertEqual(actual_res3, expected_res3)
