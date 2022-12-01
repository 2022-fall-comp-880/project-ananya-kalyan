## Comp880 Integrated Practicum - Fall 2022 - Project

##  Design Document

### Authors : Ananya Bojja, Kalyan Kumar Gade


**1** How many social media accounts does this particular firm have?

- The input for this question will be the company_name and no_company_socials attributes from the dataset. 

- The input values creates no of social media accounts for every company by using the data information from the .csv file. 

- An accumulator called No_of_social_accounts is used to get the list of companies which as specific social media accounts. At first the accumulator is initialized with an empty dictionary. 

- Iterate through the dictionary social_accounts using for loop by assigning the key with no_of_social_accounts and value with company_list.

- Using If condition check whether the company_list is in no_social_accounts.

- If the condition is satisfied then append the no_social_accounts to the list of company_list.

- Otherwise, Assign the value no_social_accounts to the company_list index in no_social_accounts.

- The outcome for this question will be a list of companies which has same count of social media accounts.

----------------------------------------------------------------------------------------------------------------

