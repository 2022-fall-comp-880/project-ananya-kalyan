## Project Report

### Authors: Ananya Bojja, Kalyan Kumar Gade

### 1. Purpose

- The dataset used for the project is the US Start-up Companies over time. This project helps to find the companies location with company lists, no of companies founded in specific year, company's no of social media accounts.
- For the project `US Startup Companies over time` we have used `US Startup Companies over time data`.
  - This dataset is taken from Kaggle website - https://www.kaggle.com/datasets/thedevastator/empowering-the-next-wave-of-entrepreneurs
  - Author of this dataset is unknown.
  - The dataset was last updated on December 5,2022.
  - The dataset has 1000 rows and 9 attributes which provides details about the companies, their locations, founded year and their social media accounts etc.
  -	The attributes are:
  
    - **company_name**	   - The name of the startup company. (String)

    - **link**	           - A link to the company's website. (String)

    - **short_description**- A short description of the company. (String)
 
    - **founded**	         - The year the company was founded. (Integer)
 
    - **team_size**	       - The number of people on the company's team. (Integer)

    - **location**	       - The city where the company is located. (String)

    - **country**          - The country where the company is located. (String)

    - **no_founders**	     - The number of founders of the company. (Integer)

    - **nocompanysocials** - The number of social media accounts associated with the company. (Integer)


- In this project, we have investigated on the below questions:

  1 How many social media accounts does this particular firm have?

  2 How many companies with its team size are present in specific location?

  3 How many companies are founded in a specific year?

---------------------------------------------------------------------------------


### 2. Approach

- We have created a .py file for every investigative question and placed them in the src directory.
- The dataset is in the form of csv, so we have imported the csv reader for reading the file.
- For every investigative question we have created a method to read the column names that will be used in transformation.
- For each investigative question we have created read_data_file_to_dictionary method to read the data from the data.

### def read_data_file_to_d(self, key_idx: int, value_idx: int, idx: int) -> dict:
        
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

### **2.1 How many social media accounts does this particular firm have?**

### def companies_list_same_social_accounts(self):
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

- Create a variable called `social_accounts_d` and call the function `firm_social_media_accounts.`
- Initialize a new variable with `no_social_accounts_dict` as an empty dictionary `{}` which is the accumulator.
- Using for loop iterate on `social_accounts_d` by using the iterables no_social_accounts, company_list.
    - If the `company_list` is in `no_social_accounts_dict`.
    - If the condition is satisfied, then append the accumulator `no_social_accounts` to the list of `company_list`.
    -	Else, Assign the value `no_social_accounts` to the `company_list index` in `no_social_accounts`.
- Return the output `no_social_accounts_dict` after the completion of for loop. 



### **2.2  How many companies with its team size are present in specific location?**

### def company_loc_by_team_size(self) -> dict:
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


- Create a variable called `company_location_dict` and call the function `location_by_company_team_size().`
- Initialize a new variable with `company_location` as an empty dictionary `{}` which is the accumulator.
- Using for loop iterate on `social_accounts_d` by using the iterables `locations`, `company_list`.
  - Again use for loop and iterate on `company_list` with iterable as `team_size`.
    - If the `team_size[1]` is greater than or equal to the value 500.
       - If the `location` is in `company_location`.
       - If the both conditions are satisfied, then update the first index of dictionary with location.
    -	Else, Assign the value first index of `team_size` to the `locations` index in `company_location`.
- Return the output `company_location` after the completion of for loop.


### **2.3  How many companies are founded in a specific year?**

### def no_of_companies_founded(self):
        """
        Create a dictionary of year founded and no of companies founded.

        Gets dictionary of year founded and no of companies founded
         by calling self.company_social_accounts().

        Creates and returns a new dictionary whose keys are the year founded
            and value is total no of companies founded in specific year.

        :returns: dictionary
           key: int, founded_year
           value: int, no of companies founded in specific year
        """


- Initialize a new variable with `companies_founded_year_d` as an empty dictionary `{}` which is the accumulator.
- Create a variable called `year` and call the function `location_by_company_team_size().`
- Using for loop iterate on `year` with the iterable `no_companies`.
    - If the `no_companies` is equal to `-1`.
       - If the `unknown` is in `companies_founded_year_d`.
         - Then increment the unknown index of `companies_founded_year_d` by the value 1.
       - Else assign the unknown index of `companies_founded_year_d` with the value 1.
    - Else
       - If the `no_companies` is in `companies_founded_year_d`.
        - If the condition is true then the count of `no_companies` is increased to the accumulator.
        - Otherwise, Assign the accumulator `companies_founded_year_d` with the value 1.
- Return the output `companies_founded_year_d` after the completion of for loop.

----------------------------------------------------------------------------------------------------


### 3. Testing

- We have created a test directory with three test files one each for every investigative question.
- For every test file we have created three scenarios to test the code along with actual dataset.
   - Testing will actual dataset.
   - Testing with empty dataset.
   - Testing with first five entries in the data file.
   - Testing with last ten entries in the data file.
- `unittest` module is imported to write testcases and evaluate the result using assert statements.
- `os` module is used to create the file paths.

### 3.1 class TestSocialMediaAccounts(unittest.TestCase):

    """Test `companies_list_same_social_accounts()` method."""

### 3.1.1 def test_multiple_entries(self):

        """Test case 1 using Startup_data.csv."""
        
- This method takes the entire dataset.
- The Output will be a dictionary of all entries in the dataset.
- In this method the data in `Startup_data.csv` file is tested.
- The actual_result is calculated by calling companies_list_same_social_accounts() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.


    
### 3.1.2 def test_empty(self):

        """Test case 2 using Startup_data_empty.csv."""

- This method takes the empty dataset.
- The Output will be an empty dictionary.
- In this method the data in `Startup_data_empty.csv` file is tested.
- The actual_result is calculated by calling companies_list_same_social_accounts() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.

        

### 3.1.3 def test_first_five_entries(self):

        """Test case 3 using Startup_data_First5.csv."""

- This method takes the file with five entries.
- The Output will be a dictionary of first five entries.
- In this method the data in `Startup_data_First5.csv` file is tested.
- The actual_result is calculated by calling companies_list_same_social_accounts() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.


### 3.1.4 def test_last_ten_entries(self):

        """Test case 4 using Startup_data_Last10."""

- This method takes the file with single entry.
- The Output will be a dictionary of last ten entries.
- In this method the data in `Startup_data_Last10.csv` file is tested.
- The actual_result is calculated by calling companies_list_same_social_accounts() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.

--------------

### 3.2 class TestCompaniesLocation(unittest.TestCase):

    """Test `company_loc_by_team_size()` method."""


### 3.2.1 def test_multiple_entries(self):

        """Test case 1 using Startup_data.csv."""
        
- This method takes the entire dataset.
- The Output will be a dictionary of all entries in the dataset.
- In this method the data in `Startup_data.csv` file is tested.
- The actual_result is calculated by calling company_loc_by_team_size() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.



    
### 3.2.2 def test_empty(self):

        """Test case 2 using Startup_data_empty.csv."""

- This method takes the empty dataset.
- The Output will be an empty dictionary.
- - In this method the data in `Startup_data_empty.csv` file is tested.
- The actual_result is calculated by calling company_loc_by_team_size() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.

        

### 3.2.3 def test_first_five_entries(self):

        """Test case 3 using Startup_data_First5.csv."""

- This method takes the file with five entries.
- The Output will be a dictionary of first five entries.
- In this method the data in `Startup_data_First5.csv` file is tested.
- The actual_result is calculated by calling company_loc_by_team_size() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.


### 3.2.4 def test_last_ten_entries(self):

        """Test case 4 using Startup_data_Last10."""

- This method takes the file with single entry.
- The Output will be a dictionary of last ten entries.
- In this method the data in `Startup_data_Last10.csv` file is tested.
- The actual_result is calculated by calling company_loc_by_team_size() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.

----------------

### 3.3 class TestCompanyFoundedYearCount(unittest.TestCase):

    """Test `company_founded_year_count()` method."""


### 3.3.1 def test_multiple_entries(self):

        """Test case 1 using Startup_data.csv."""
        
- This method takes the entire dataset.
- The Output will be a dictionary of all entries in the dataset.
- In this method the data in `Startup_data.csv` file is tested.
- The actual_result is calculated by calling no_of_companies_founded() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.


    
### 3.3.2 def test_empty(self):

        """Test case 2 using Startup_data_empty.csv."""

- This method takes the empty dataset.
- The Output will be an empty dictionary.
- The Output will be a dictionary of all entries in the dataset.
- In this method the data in `Startup_data_empty.csv` file is tested.
- The actual_result is calculated by calling no_of_companies_founded() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.


        

### 3.3.3 def test_first_five_entries(self):

        """Test case 3 using Startup_data_First5.csv."""

- This method takes the file with five entries.
- The Output will be a dictionary of first five entries.
- The Output will be a dictionary of all entries in the dataset.
- In this method the data in `Startup_data_First5.csv` file is tested.
- The actual_result is calculated by calling no_of_companies_founded() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.



### 3.3.4 def test_one_entries(self):

        """Test case 4 using Startup_data_Last10."""

- This method takes the file with single entry.
- The Output will be a dictionary of last ten entries.
- The Output will be a dictionary of all entries in the dataset.
- In this method the data in `Startup_data_Last10.csv` file is tested.
- The actual_result is calculated by calling no_of_companies_founded() method.
- The expected_result is precalculated by examining the data.
- Using the assertEqual statement the actual_result and expected_result is compared.
- If the contents are equal then the testcase will pass.


----------------------------------------------------------------------------------------

### 4. Results

### 4.1 Social media Accounts with list of companies.

- def companies_list_same_social_accounts(self) -> dict[str, int]:

- Output returns a dictionary (key: str, count of social media accounts)(value: list of int, list of comapies).


### 4.2 Company locations with respect team size.

- def company_loc_by_team_size(self) -> dict[str, str]:

- Output returns a dictionary with (key: str, location)(value: list of str, list of companies).

### 4.3 Company fall under same founded year.

- def no_of_companies_founded(self) -> dict[int, int]:

- Output returns a dictionary with (key: str, founded_year)(value: int, count of companies).


---------------------------------------------------------------------------------------

### 5. Evaluation

### 5.1 What Works and Scope Assumptions :

- The Assumption is that all the data in the dataset is legitimate and practical data.

- The company's location, social media account count and founded year are evaluated based on the data of 1000 companies information.

- From our work we can provide certain details of startup companies that makes people to get the clear picture and can predict the scope of a particular company.

- From the investigative questions we can know the details of no of companies which has specific social media accounts, locations which has specific companies and no of companies which fall under specific founded year.

### 5.2 Immediate Further Development :

- Data visualizations can be created to show a graph in which list of companies has specific social media accounts, which location has a list of companies which has a team size of more than 500 and in specific year how many companies are founded.
