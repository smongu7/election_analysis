# election_analysis
## Project Overview
In this project, we were given the following scenario: An employee of the Colorado Board of Elections tasked us to complete an audit of a local congressional election. The tasks were as follows:
1. Calculate the total number of votes cast.
2. Make a list of all the candidates who recieved votes.
3. Calculate the number of votes that each candidate recieved.
4. Calculate the percentage of votes that each candidate won.
5. Determine which candidate won based on the popular vote.
## Resources
- Data Source: election_results.csv
- Software: Python 3.9.7
## Summary
These were the results according to the analysis:
- There were 369,711 total votes cast in the election.
- These were the candidates:
    - Charles Casper Stockham
    - Diana Degette
    - Raymon Anthony Doane
- The results of each candidate were as follows:
  - Charles Casper Stockham recieved 23.0% of the popular vote with 85,213 votes.
  - Diana Degette recieved 73.8% of the popular vote with 272,892 votes.
  - Raymon Anthony Doane recieved 3.1% of the popular vote with 11,606 votes.

## Challenge Overview
The purpose this challenge was to apply what we learned in the project. In the project, we learned how to:
 - import, open and read a file
 - add a variable to load or save a file path
 - initialize each of the following: 
    - list 
    - dictionary
    - counter
    - variable
    - empty string
 - iterate through every row in a list
 - count the number of an item (for example, the number of votes) in a list
 - calculate percentage
 - create an f string
 - create for loops
 - use conditionals
 - Print the results to the terminal
 - Save the results to a text file.

## RESULTS
These were the results according to the analysis:
- These were the counties:
    - Arapahoe
    - Denver
    - Jefferson
- The results of each county were as follows:
    - Arapahoe had a 6.7% turnout with 24,801 votes.
    - Denver had an 82.8% turnout with 306,055 votes.
    - Jefferson had a 10.5% turnout with 38.855 votes.
- Jefferson county had the largest turnout.

## Challenge Summary
This script could be used to audit any election; one would just have to replace the names of counties and candidates. Additionally, if the columns are in a different order-- or there are more than 3 of them-- then the index might need to be changed to ensure the script is retrieving data from the correct column. One way this code could be modified would be to calculate how many votes each candidate recieved per county; with this data, we would be able to see if a candidates won the popular vote of a county but not the overall popular vote. Another way we could modify this script would be to add the population of each county. Using this data, we could calculate the voter turnout of each county in this election.
