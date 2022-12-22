## Comp880 Integrated Practicum - Fall 2022 - Project

##  Design Document

### Authors : Ananya Bojja, Kalyan Kumar Gade


**1** How many social media accounts does this particular firm have?

- The input for this question will be the company_name and no_company_socials attributes from the dataset. 

- The input values creates no of social media accounts for every company by using the data information from the .csv file. 

- An accumulator called No_of_social_accounts is used to get the list of companies which as specific social media accounts. At first the accumulator is initialized with an empty dictionary. 

- Iterate through the dictionary social_accounts using for loop by assigning the key with no_of_social_accounts and value with company_list.

- Using If condition check whether the company_list is in accumulator no_social_accounts.

- If the condition is satisfied then append the accumulator no_social_accounts to the list of company_list.

- Otherwise, Assign the value no_social_accounts to the company_list index in no_social_accounts.

- The outcome for this question will be a list of companies which has same count of social media accounts.

----------------------------------------------------------------------------------------------------------------

**2** How many companies with its team size are present in specific location?

- The inputs for this question will be the location and list of company_name and team_size attributes from the dataset. 

- Using the team size of the company divide list of companies at particular location by using the data information from the .csv file. 

- An accumulator called company_location is used to get the list of companies which has a team_size greater than 500. At first the accumulator is initialized with an empty dictionary. 

- Iterate through the dictionary using for loop by assigning the key with locations and value with company_list.

- Using If condition check whether the team_size is greater than or equal to the value 500. 

- If the condition is true then update the first index of dictionary with location.

- Otherwise, Assign the value first index of team_size to the locations index in company_location.

- The outcome for this question will be a list of companies with certain range of team size at particular location.

-------------------------------------------------------------------------------------------------------------------------

**3** How many companies are founded in a specific year?

- The inputs for this question will be the companies founded year and year  from the dataset. 

- Using the year we will find no of companies founded in a specific year by using the data information from the .csv file. 

- An accumulator called companies_founded_year_d is used to get the list of no of companies found in a specific year. At first the accumulator is initialized with an empty dictionary. 

- Iterate through the dictionary using for loop with the iterable no_companies.

- If the no_companies is equal to "-1".
       
- If the "unknown" is in the accumulator then increment the unknown index of dictionary by the value 1.

-  Else assign the unknown index of accumulator dictionary with the value 1.

- Using If condition check whether the no_companies are in accumulator companies_founded_year_d. 

- If the condition is true then the count of no_companies is increased to the accumulator .

- Otherwise, Assign the accumulator companies_founded_year_d with the value 1.

- This is a histogram of attributes with founded, count of company_names from the data. 

- The outcome for this question will be a dictionary of  year founded and no of startup companies emerged.

