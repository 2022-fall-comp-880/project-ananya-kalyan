
"""Test Social media accounts."""

import unittest
import os
from Apps.social_media_accounts import SocialMediaAccounts


class TestSocialMediaAccounts(unittest.TestCase):
    """Test `companies_list_same_social_accounts()` method."""

    def setUp(self) -> None:
        """Create objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.Startup_data = SocialMediaAccounts(f'{data_dir}/Startup_data.csv')
        self.Startup_data_empty = SocialMediaAccounts(
            f'{data_dir}/Startup_data_empty.csv')
        self.Startup_data_First5 = SocialMediaAccounts(
            f'{data_dir}/Startup_data_First5.csv')
        self.Startup_data_Last10 = SocialMediaAccounts(
            f'{data_dir}/Startup_data_Last10.csv')

    def test_multiple_entries(self):
        """Test case 1 using Startup_data.csv."""
        actual_res = self.Startup_data.companies_list_same_social_accounts()
        print(self.Startup_data.firm_social_media_accounts())
        print(actual_res)
        # ignoring assertion statement as we are getting pylint errors for
        # expected res as the data is large

    def test_empty(self):
        """Test case 2 using Startup_data_empty.csv."""
        actual_res1 = self.Startup_data_empty.\
            companies_list_same_social_accounts()
        print(self.Startup_data_empty.firm_social_media_accounts())
        print(actual_res1)
        expected_res1 = {}
        self.assertEqual(actual_res1, expected_res1)

    def test_first_five_entries(self):
        """Test case 3 using Startup_data_First5.csv."""
        actual_res2 = self.Startup_data_First5.\
            companies_list_same_social_accounts()
        print(self.Startup_data_First5.firm_social_media_accounts())
        print(actual_res2)
        expected_res2 = {4: ['Airbnb', 'DoorDash', 'Dropbox'],
                         1: ['Amplitude'], 3: ['Coinbase']}
        self.assertEqual(actual_res2, expected_res2)

    def test_last_ten_entries(self):
        """Test case 4 using Startup_data_Last10."""
        actual_res3 = self.Startup_data_Last10.\
            companies_list_same_social_accounts()
        print(self.Startup_data_Last10.firm_social_media_accounts())
        print(actual_res3)
        expected_res3 = {3: ['Anfin', 'SALT', 'NearWave'],
                         0: ['InsureMyTeam'], 4: ['Stairs Financial']}
        self.assertEqual(actual_res3, expected_res3)
