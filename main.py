import argparse
import sys
import re

ip_count = {}
error_counts = {}


def get_log_file():
    parser = argparse.ArgumentParser(description="Log-Sifter: Analyze log files")
    parser.add_argument("logfile", help="Path to the log file", type=str)

    args = parser.parse_args()

    if not args.logfile.endswith(".log"):
        sys.exit("Error: File must be a .log file")

    return args.logfile


def analyse_IPs(file):
    try:
        with open(file, "r") as f:
            content = f.read()
            print(f"Analyzing IP addresses")
            regex = re.compile(r"\[client (\d+\.\d+\.\d+\.\d+):(\d+)\]")
            ips = regex.findall(content)
            for ip in ips:
                print(f"Found IP address: {ip}")
                if ip in ip_count:
                    ip_count[ip] += 1
                else:
                    ip_count[ip] = 1
            return ip_count
    except FileNotFoundError:
        sys.exit("Error: File not found")


def analyse_errors(file):
    try:
        with open(file, "r") as f:
            content = f.read()
            print(f"Analyzing error logs")
            regex = re.compile(r"\[(\w+):(\w+)\]")
            found_errors = regex.findall(content)   
            for error in found_errors:
                if error in error_counts:
                    error_counts[error] += 1
                else:
                    error_counts[error] = 1
                    print(f"New error added: {error}")
            return error_counts
    except FileNotFoundError:
        sys.exit("Error: File not found")


def main():
    log_file = get_log_file()
    IP_analysis = analyse_IPs(log_file)
    error_analysis = analyse_errors(log_file)
    print(f"IP Analysis:")
    for i in IP_analysis:
        print(f"{i}: {IP_analysis[i]}")
    print(f"Error Analysis:")
    for e in error_analysis:
        print(f"{e}: {error_analysis[e]}")

if __name__ == "__main__":
    main()
