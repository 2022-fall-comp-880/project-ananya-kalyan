The dataset used for the project is regarding the US Start-up Companies over time
•	This dataset is taken from Kaggle website - https://www.kaggle.com/datasets/thedevastator/empowering-the-next-wave-of-entrepreneurs
•	Author of this dataset is unknown.
•	The dataset was last updated on December 5,2022.
•	The dataset has 1000 rows and 9 attributes which provides details about the companies and their social media accounts.
•	The attributes are:
•	company name - The name of the start-up company. (String)
•	link - A link to the company's website. (String)
•	short description - A short description of the company. (String)
•	founded - The year the company was founded. (Integer)
•	team size - The number of people on the company's team. (Integer)
•	location - The city where the company is located. (String)
•	country - The country where the company is located. (String)
•	no founders - The number of founders of the company. (Integer)
•	nocompanysocials - The number of social media accounts associated with the company. (Integer)
•	In this project, we have investigated on the below questions:
•	 1 How many social media accounts does this particular firm have?
•	 2 How many companies with its team size are present in specific location?
•	 3 How many companies are founded in a specific year?

2. Approach
1 How many social media accounts does this particular firm have?
•	The input for this question will be the company_name and no_company_socials attributes from the dataset.
•	The input values creates no of social media accounts for every company by using the data information from the .csv file.
•	An accumulator called No_of_social_accounts is used to get the list of companies which as specific social media accounts. At first the accumulator is initialized with an empty dictionary.
•	Iterate through the dictionary social_accounts using for loop by assigning the key with no_of_social_accounts and value with company_list.
•	Using If condition check whether the company_list is in accumulator no_social_accounts.
•	If the condition is satisfied, then append the accumulator no_social_accounts to the list of company_list.
•	Otherwise, Assign the value no_social_accounts to the company_list index in no_social_accounts.
•	The outcome for this question will be a list of companies which has same count of social media accounts.
2  How many companies with its team size are present in specific location?
•	The inputs for this question will be the location and list of company_name and team_size attributes from the dataset.
•	Using the team size of the company divide list of companies at particular location by using the data information from the .csv file.
•	An accumulator called company_location is used to get the list of companies which has a team_size greater than 500. At first the accumulator is initialized with an empty dictionary.
•	Iterate through the dictionary using for loop by assigning the key with locations and value with company_list.
•	Using If condition check whether the team_size is greater than or equal to the value 500.
•	If the condition is true then update the first index of dictionary with location.
•	Otherwise, Assign the value first index of team_size to the locations index in company_location.
•	The outcome for this question will be a list of companies with certain range of team size at particular location
3  How many companies are founded in a specific year?
•	The inputs for this question will be the companies founded year and year from the dataset.
•	Using the year we will find no of companies founded in a specific year by using the data information from the .csv file.
•	An accumulator called companies_founded_year_d is used to get the list of no of companies found in a specific year. At first the accumulator is initialized with an empty dictionary.
•	Iterate through the dictionary using for loop with the iterable no_companies.
•	Using If condition check whether the no_companies are in accumulator companies_founded_year_d.
•	If the condition is true then the count of no_companies is increased to the accumulator .
•	Otherwise, Assign the accumulator companies_founded_year_d with the value 1.
•	This is a histogram of attributes with founded, count of company_names from the data.
•	The outcome for this question will be a dictionary of year founded and no of startup companies emerged.

3. Testing
4. Results
   Heading
•	The output of this method is a dictionary. The keys of the dictionary are the number of social media accounts and values are the company list.
#Heading 
•	The output of this method is a dictionary. The keys of the dictionary are the locations and values company list . The outcome for this question will be a list of companies with certain range of team size at particular location.
#Heading
The output of this method is a dictionary. The keys of the dictionary are the names of city and values are the percentage of impact in each city.
5. Evaluation
5.1 What Works and Scope Assumptions
.
5.2 Immediate Further Development
•	.

The dataset used for the project is regarding the US Start-up Companies over time
•	This dataset is taken from Kaggle website - https://www.kaggle.com/datasets/thedevastator/empowering-the-next-wave-of-entrepreneurs
•	Author of this dataset is unknown.
•	The dataset was last updated on December 5,2022.
•	The dataset has 1000 rows and 9 attributes which provides details about the companies and their social media accounts.
•	The attributes are:
•	company name - The name of the start-up company. (String)
•	link - A link to the company's website. (String)
•	short description - A short description of the company. (String)
•	founded - The year the company was founded. (Integer)
•	team size - The number of people on the company's team. (Integer)
•	location - The city where the company is located. (String)
•	country - The country where the company is located. (String)
•	no founders - The number of founders of the company. (Integer)
•	nocompanysocials - The number of social media accounts associated with the company. (Integer)
•	In this project, we have investigated on the below questions:
•	 1 How many social media accounts does this particular firm have?
•	 2 How many companies with its team size are present in specific location?
•	 3 How many companies are founded in a specific year?

2. Approach
1 How many social media accounts does this particular firm have?
•	The input for this question will be the company_name and no_company_socials attributes from the dataset.
•	The input values creates no of social media accounts for every company by using the data information from the .csv file.
•	An accumulator called No_of_social_accounts is used to get the list of companies which as specific social media accounts. At first the accumulator is initialized with an empty dictionary.
•	Iterate through the dictionary social_accounts using for loop by assigning the key with no_of_social_accounts and value with company_list.
•	Using If condition check whether the company_list is in accumulator no_social_accounts.
•	If the condition is satisfied, then append the accumulator no_social_accounts to the list of company_list.
•	Otherwise, Assign the value no_social_accounts to the company_list index in no_social_accounts.
•	The outcome for this question will be a list of companies which has same count of social media accounts.
2  How many companies with its team size are present in specific location?
•	The inputs for this question will be the location and list of company_name and team_size attributes from the dataset.
•	Using the team size of the company divide list of companies at particular location by using the data information from the .csv file.
•	An accumulator called company_location is used to get the list of companies which has a team_size greater than 500. At first the accumulator is initialized with an empty dictionary.
•	Iterate through the dictionary using for loop by assigning the key with locations and value with company_list.
•	Using If condition check whether the team_size is greater than or equal to the value 500.
•	If the condition is true then update the first index of dictionary with location.
•	Otherwise, Assign the value first index of team_size to the locations index in company_location.
•	The outcome for this question will be a list of companies with certain range of team size at particular location
3  How many companies are founded in a specific year?
•	The inputs for this question will be the companies founded year and year from the dataset.
•	Using the year we will find no of companies founded in a specific year by using the data information from the .csv file.
•	An accumulator called companies_founded_year_d is used to get the list of no of companies found in a specific year. At first the accumulator is initialized with an empty dictionary.
•	Iterate through the dictionary using for loop with the iterable no_companies.
•	Using If condition check whether the no_companies are in accumulator companies_founded_year_d.
•	If the condition is true then the count of no_companies is increased to the accumulator .
•	Otherwise, Assign the accumulator companies_founded_year_d with the value 1.
•	This is a histogram of attributes with founded, count of company_names from the data.
•	The outcome for this question will be a dictionary of year founded and no of startup companies emerged.

3. Testing
4. Results
   Heading
•	The output of this method is a dictionary. The keys of the dictionary are the number of social media accounts and values are the company list.
#Heading 
•	The output of this method is a dictionary. The keys of the dictionary are the locations and values company list . The outcome for this question will be a list of companies with certain range of team size at particular location.
#Heading
The output of this method is a dictionary. The keys of the dictionary are the names of city and values are the percentage of impact in each city.
5. Evaluation
5.1 What Works and Scope Assumptions
.
5.2 Immediate Further Development
•	.

