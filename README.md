# code_challenges
Security Themed coding challenges


secure_password.py
Challenge: Given an input password string, determine if the password is secure or not by using the following rules:
              A password is considered secure if all of the following are true:
              It has at least 8 characters
              It contains at least one uppercase letter
              It contains at least one lowercase letter
              It contains at least one digit
              It does NOT contain any spaces
              Write a function is_secure_password(password) that returns True or False.
learnings:
basic if else syntax and function def.

lazy_caesar_cipher.py
Challenge: write a basic caesar cipher with shift 3
added challenge is to avoid using hardcoded alphabets.

Learnings:
rounding off 

loganalysis.py
Challenge narrative: In this challenge I started small and added complexity.
Start with opening a file access.log and extract all the IPs and the number of requests per IP. write the most visited top 10 IPs to a outputfile
filter out the number of requests by status code given by user via command line input. Then list out the IPs with the given statuscode (pay attention to how to avoid duplicate IP printing using set vs list)
Bruteforce detection using one rule - if an IP has both 401 and 200 status results with in a 5 minute window, flag that IP as bruteforce suspection. 
extended challenge is to solve the bruteforce detection implementing a 'sliding window' solution. 

Learnings:
How to read/write to a file
right data structure use - list vs set, dictionary with tuple as value
building regex patterns and groups
taking input from system arg
using strptime()
list comprehensions
for/else/break 
