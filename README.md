In cybersecurity, everything comes down to logs. SOC (Security Operations Center) analysts spend their lives sifting through millions of lines of log data to find signs of an attack. I am going to build a tool to automate the boring part.

Project Name: Log-Sifter - An Automated Log File Analyzer

Concept: In cybersecurity, everything comes down to logs. SOC (Security Operations Center) analysts spend their lives sifting through millions of lines of log data to find signs of an attack. You are going to build a tool to automate the boring part.

Argument Parsing: Your script should be a command-line tool. It should accept arguments, like the path to the log file. Use Python's argparse library for this. This is a huge step up from input().

File I/O: The script will read a log file (you can find sample apache_logs.txt files online) line by line. You've already mastered this.

Regular Expressions (Regex): This is the core. You'll use regex to parse each line of the log to extract key information: the IP address, the timestamp, the request type (GET/POST), the status code (200, 404, 500), and the user agent.

Data Structures: Use a dictionary to store and count the occurrences of interesting events. For example: a dictionary where keys are IP addresses and values are the number of requests from that IP.

Reporting: At the end, the script should print a clean, formatted summary report to the console. E.g., "Top 10 IP Addresses by Request Count," "Summary of Status Codes (200s: 5,432, 404s: 123)," etc.

Unit Testing: Use pytest to write tests for your regex parsing functions. Can your function correctly extract an IP address from a sample log line? This proves your tool is reliable.

Why this project is critical: You are combining everything from CS50P into a single, useful, real-world cybersecurity tool. This is a foundational skill for any kind of digital forensics or defense.

