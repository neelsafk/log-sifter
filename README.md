Project Name: Log-Sifter - An Automated Log File Analyzer

Argument Parsing: This script is a command-line tool. It accept arguments, like the path to a log file. Uses Python's argparse library for this. 

File I/O: The script will read the log file (you can find sample errors.log in the repo).

Regular Expressions (Regex): Regex parses each line of the log to extract key information: the IP address, the timestamp, the request type (GET/POST), etc.

Data Structures: Uses a dictionary to store and count the occurrences of interesting events.

Reporting: At the end, the script prints a clean, formatted summary report to the console. E.g., "IP Addresses by Request Count", "Summary of Status Codes (200s: 5,432, 404s: 123)", etc.

Unit Testing: Uses pytest to write tests for my regex parsing functions. This proves the tool is reliable.