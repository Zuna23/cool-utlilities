import sys
import os
import subprocess
import csv
import argparse

def host_name_ping(input_file, output_file):
    successful = []
    unsuccessful = []

    if not os.path.isfile(input_file):
        print(f"Input file '{input_file}' does not exist.")
        sys.exit(1)

    with open(input_file, "r") as hostsFile:
        lines = [line.strip().strip(',') for line in hostsFile if line.strip()]

    print(f"Pinging {len(lines)} hosts...")

    for line in lines:
        param = '-n' if os.name == 'nt' else '-c'
        command = ['ping', param, '2', line]
        print(f"Pinging {line}...", end=' ')
        try:
            result = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result == 0:
                successful.append(line)
                print("Success")
            else:
                unsuccessful.append(line)
                print("Failed")
        except Exception as e:
            unsuccessful.append(line)
            print(f"Error: {e}")

    csv_columns = ['Successful', 'Unsuccessful', 'Success_Count', 'Fail_Count']
    dict_data = [{
        'Successful': ', '.join(successful),
        'Unsuccessful': ', '.join(unsuccessful),
        'Success_Count': len(successful),
        'Fail_Count': len(unsuccessful)
    }]

    try:
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
        print(f"\nResults written to '{output_file}'")
    except IOError:
        print("I/O error while writing CSV.")

def main():
    parser = argparse.ArgumentParser(description="Ping hosts from a file and save results to CSV.")
    parser.add_argument('--input', required=True, help="Path to input file containing hostnames/IPs (one per line).")
    parser.add_argument('--output', default="hosts_results.csv", help="Path to output CSV file (default: hosts_results.csv).")
    args = parser.parse_args()

    host_name_ping(args.input, args.output)

if __name__ == '__main__':
    main()
