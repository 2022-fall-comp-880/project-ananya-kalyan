### Project Proposal

## US Startup Companies over time

**Author-1**: Ananya Bojja

**Author-2**: Kalyan Kumar Gade

**Date**: 11/30/2022


## Motivation 

**Q.** What specific investigation will the project carry out?

**A.**  The dataset contains information on startup companies in the US from  the year 2008 which includes company name, location, team size, number of founders, and other relevant information. 
 This data can be used to empower the next wave of entrepreneurs by providing insights on
 what types of startups are being founded, where they are located, and how large their teams are. 
 Additionally, this dataset can be used to understand trends in the startup industry over time.



## Investigative Questions 

**Q.** THREE questions that will guide your project work and give interesting insights into the data set?

**A.**

**1** How many social media accounts does this particular firm have?

**2** How many companies with its team size are present in specific location?

**3** How many companies are founded in a specific year?



## Approach 

**Q.** Describe the approach you will use to develop the project. Your description must include:
- Brief description of the data set the project will investigate (including source, size, organization, who contributed the data set, date of the most recent update)
- What kind of transformations and data structures you envision you will be using in carrying out the project work.

**A.**  The data set I have selected has data of US startup companies overtime  with the attributes like company_name, link ,short_description	,founded, team_size,location	,country ,no_founders ,no_company_socials .
 
  These attributes enable us to determine the Information about the Startup companies and they founded year at what locations they are size of the company how many accounts they have .
- The output for the question - "How many social media accounts does this particular firm have?" - would be in the form of dictionary which contains keys as `no_company_socials` and value as list of `company_name`. 
- The output for the question - "How many companies with its team size are present in specific location?" - would be in the form of dictionary which contains keys as `location` and values as list of `company_name` and `team_size`. 
- The output for the question - "How many companies are founded in a specific year?" - would be in the form of dictionary which contains keys as `founded` and values as total count of companies.


## Expected Results 

**Q.** Describe what results you anticipate to get. Your description must refer to what results will be finally produced and how they will be presented.

**A.**  As a final result, We will get three dictionaries with keys - `no_company_socials`,`location`, `founded` and values as a list of `company_name`, `team_size`, `count of companies`. This results provide insights on
 what types of startups are being founded, where they are located, and how large their teams are. 


## New Python Packages or Modules 

**Q.** Research and describe what Python packages or modules will be useful to your project. Your description must include a list of helpful references that have good examples.}

**A.**  The python packages that are useful in my project may be `os`, `csv`, `unittest`.
- The `OS` module in Python provides functions for interacting with the operating system.The *os* and *os.path* modules include many functions to interact with the file system.
- Python `unittest` is a built-in testing framework to test Python code. It has a test runner, which allows us to run the tests without much effort.
- The `csv` module implements classes to read and write tablular design in csv format.



## Dataset Documentation

- The data set has been taken from the website kaggle.com and below is the link

- https://www.kaggle.com/datasets/thedevastator/empowering-the-next-wave-of-entrepreneurs

- This is an open source Data set.

- It was updated 14 days ago.

- The data set we have selected has data of US startup companies overtime  with the attributes like 
 
 **company_name**	   - The name of the startup company. (String)

 **link**	           - A link to the company's website. (String)

 **short_description** - A short description of the company. (String)
 
 **founded**	       - The year the company was founded. (Integer)
 
 **team_size**	       - The number of people on the company's team. (Integer)

 **location**	       - The city where the company is located. (String)

 **country**           - The country where the company is located. (String)

 **no_founders**	   - The number of founders of the company. (Integer)

 **nocompanysocials**  - The number of social media accounts associated with the company. (Integer)
