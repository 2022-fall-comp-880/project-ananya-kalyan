# Students Performance in Exams

**Author**: Ananya Bojja

**Date**: 11/16/2022


## Motivation 

**Q.** What specific investigation will the project carry out?

**A.** The Data set consists of the marks secured by the students in various 
subjects.This data set includes scores from three exams and a variety of 
personal, social, and economic factors that have interaction effects upon them.
It also contain the details of which grade the student belongs to and helps 
us to determine the status of student preparation.



## Investigative Questions 

**Q.** THREE questions that will guide your project work and give interesting insights into the data set?

**A.**

**1** How effective is the test preparation course?

**2** Which major factors contribute to test outcomes?

**3** What would be the best way to improve student scores on each test?



## Approach 

**Q.** Describe the approach you will use to develop the project. Your description must include:
- Brief description of the data set the project will investigate (including source, size, organization, who contributed the data set, date of the most recent update)
- What kind of transformations and data structures you envision you will be using in carrying out the project work.

**A.**

 The data set I have selected has data of 1000 students with the attributes like gender, race, parental level of education, lunch, test preparation course, math score, writing score, reading score.These attributes enable us to determine the effectiveness of a particular student's preparation.
 The output for the question - "How effective is the test preparation course?" would be in the form of the dictionary which contains keys as `race` and value as `gender`.
 The output for the question - "Which major factors contribute to test outcomes?" would be a dictionary with key as `gender` and value is a list of `three subjects scores`.


## Expected Results 

**Q.** Describe what results you anticipate to get. Your description must refer to what results will be finally produced and how they will be presented.

**A.** As a final result, we get a dictionary with "race" as the key and "gender" of the student as the value indicating how well the student has prepared for the exam.


## New Python Packages or Modules 

**Q.** Research and describe what Python packages or modules will be useful to your project. Your description must include a list of helpful references that have good examples.}

**A.**  The python packages that are useful in my project may be `os`, `csv`, `unittest`, `warning` and may be more packages.
- The OS module in Python provides functions for interacting with the operating system.The *os* and *os.path* modules include many functions to interact with the file system.
- Python unittest is a built-in testing framework to test Python code. It has a test runner, which allows us to run the tests without much effort.
- The `warning` module is used to show warning messages. The warning module is actually a subclass of Exception which is a built-in class in Python.




## Dataset Documentation

- The data set has been taken from the website kaggle.com and below is the link

- https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

- This is an open source and the owner of this data set is `JAKKI SESHAPANPU`.

- It was updated 4 years ago.

- This data set contains 1000 Student's data with the attributes - gender, race, parental level of education, lunch, test preparation course, math score, writing score, reading score.
