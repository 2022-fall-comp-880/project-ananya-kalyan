import unittest
import os
from Apps.company_founded_year_count import CompanyFoundedYear


class TestSocialMediaAccounts(unittest.TestCase):
    """Test `company_founded_year_count()` method."""

    def setUp(self):
        """Create  objects for the three testing cases."""

    data_dir = os.path.dirname(__file__) + "/../data"
    self.startups_stats = CompanyFoundedYear(f'{data_dir}/Startup_data.csv')
    self.startups_stats_empty = CompanyFoundedYear(f'{data_dir}/Startup_data_empty.csv')
    self.startups_stats_First5 = CompanyFoundedYear(f'{data_dir}/Startup_data_First5.csv')
    self.startups_stats_Last10 = CompanyFoundedYear(f'{data_dir}/Startup_data_Last10.csv')


def test_multiple_entries(self):
    """Test case 1 using Startup_data.csv."""
    actual_res = self.startups_stats.no_of_companies_founded()
    print(self.startups_stats.company_social_accounts())
    print(actual_res)


def test_empty(self):
    """Test case 2 using Startup_data_empty.csv."""
    actual_res1 = self.startups_stats_empty.no_of_companies_founded()
    print(self.startups_stats_empty.company_social_accounts())
    print(actual_res1)


def test_first_five_entries(self):
    """Test case 3 using Startup_data_First5.csv."""
    actual_res2 = self.startups_stats_First5.no_of_companies_founded()
    print(self.startups_stats_First5.company_social_accounts())
    print(actual_res2)


def test_one_entries(self):
    """Test case 4 using Startup_data_Last10."""
    actual_res3 = self.startups_stats_Last10.no_of_companies_founded()
    print(self.startups_stats_Last10.company_social_accounts())
    print(actual_res3)
