# Intro to Programming Python Assignment 07
**Dev** *PBirkeland*  
**Date:** *6.12.2021*

## Introduction
This week’s assignment asked that we:  

•	Research Exception Handling in Python  
•	Research Pickling in Python  
•	Create a script which utilizes Pickling and Structured Error Handling  
•	Post assignment artifacts to GitHub  
•	Update GitHub Webpage 


## Research Exception Handling in Python
I found the concept of exception handling in Python easily digestible in reading Python Programming for Absolute Beginners and I can say I felt the same when watching the lecture material. However, once I actually tried applying the concepts I must admit I found this concept difficult to apply.

I had many failed attempts to incorporate this concept into my final script for this week and eventually settled on something very simple. The example executes as it should. I understand why it executes successfully. However I am was not successful in expanding on the code in the script.
Table 7.6 on page 207 of Python Programming for Absolute Beginners is a great resource for some common exception types. Where I failed was trying to create a try/except entry in my program for a syntax error based on user input. I settled on an IOError Exception Type as this was easier to implement.

•	https://problemsolvingwithpython.com/08-If-Else-Try-Except/08.05-Try-Except-Statements/
<p>&emsp;o	Very simple examples that help convey the logic of Try-Except Statements</p>  
•	https://jython.readthedocs.io/en/latest/ExceptionHandlingDebug/
<p>&emsp;o	Discusses the differences in how exception handling differs between Java and Python</p>

## Research Pickling in Python
After reading chapter 7 in Python Programming for Absolute Beginners and completing the week 7 lecture material I had a good idea of how to utilize Pickling. However I didn’t really know why someone would utilize Pickling. Therefore this is where focused on my self-learning.

I was able to find two URLs which gave great examples of where it would be beneficial to utilize Pickling and why. I have summarized the main points below in bullet points.

•	https://stackoverflow.com/questions/3438675/common-use-cases-for-pickle-in-python
<p>&emsp;o	Some great examples provided for why someone would utilize Pickling in Python</p>
<p>&emsp;o	Save a program’s state to disk</p>
<p>&emsp;o	Sending Python data over TCP connection</p>
<p>&emsp;o	Storing Python objects in a database</p>
•	https://medium.com/@lokeshsharma596/what-is-pickle-in-python-3d9f261498b4  
<p>&emsp;o	More examples of why someone would utilize Pickling</p>
<p>&emsp;o	It is used for serializing and de-serializing a Python object structure</p>

## Applying Your Knowledge
This week was a departure from previous weeks in that there was no starter file this week.  
Assignment07.py was created from scratch. The file itself is missing the standard structure we have used in this course.  
<p>&emsp;•	Data (Declare variables and constants)</p>  
<p>&emsp;•	Processing</p>  
<p>&emsp;•	Presentation (Input/Output)</p>  
<p>&emsp;•	Main Body</p>  
I did attempt to utilize the standard structure but honestly I discovered I am still not confident in understanding the boundaries between Processing and Presentation. After some hours of frustration I decided to just write the code manually without classes or functions.  
My script has a series of three prompts and each prompt states what the code is going to do and then asks the user to please hit [Enter] to continue. The three prompts are as follows:  

<p>&emsp;•	We are about to create the Pickling lists</p>  
<p>&emsp;•	We are about to read a Pickle list from a file</p>  
<p>&emsp;•	We are about to attempt to open a file which does not exist. We have a try/except condition that will display a targeted error message.</p>  
The data is written to a file named Pickles1.dat.


## Run Your Script

The following figure shows execution of this script through a command shell. (Figure 1).
![Results of Figure 1](https://github.com/x10339966/IntrotoProg-Python-Mod07/blob/main/docs/IntroToPython07-01.jpg)
#### Figure 1: The results of running Assignment07.py from a command shell  

The following figure shows execution of this script through a command shell. (Figure 2).
![Results of Figure 2](https://github.com/x10339966/IntrotoProg-Python-Mod07/blob/main/docs/IntroToPython07-02.jpg) 
####  Figure 2: The results of running Assignment07.py from PyCharm

## Verify the Script Worked

Below is a screen capture showing the text file pickles.dat exists and has been updated from the program interface. (Figure 3).
![Results of Figure 3](https://github.com/x10339966/IntrotoProg-Python-Mod07/blob/main/docs/IntroToPython07-03.jpg) 
#### Figure 3: Screenshot of data file created from script  – pickles1.dat

## Summary
In this assignment we:
<p>&emsp;•	Research Exception Handling in Python</p>
<p>&emsp;•	Research Pickling in Python</p>
<p>&emsp;•	Crete a script which utilizes Pickling and Structured Error Handling</p>
<p>&emsp;•	Post assignment artifacts to GitHub</p>
<p>&emsp;•	Update GitHub Webpage</p>

