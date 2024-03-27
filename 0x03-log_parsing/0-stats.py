#!/usr/bin/python3

"""
Define  a script that reads stdin line by line and computes metrics
"""


import sys


def print_stats(stats, file_size):
    """
    Prints the statistics, including file size and status code counts.
    """
    print(f"File size: {file_size}")
    for code, count in sorted(stats.items()):
        if count:
            print(f"{code}: {count}")


if __name__ == '__main__':
    # Initialize variables
    filesize, count = 0, 0
    codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    stats = {code: 0 for code in codes}

    try:
        # Read input line by line
        for line in sys.stdin:
            count += 1
            data = line.split()

            # Extract and update status code count
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except (IndexError, ValueError):
                # Skip invalid lines
                pass

            # Extract and update file size
            try:
                filesize += int(data[-1])
            except (IndexError, ValueError):
                # Skip invalid lines
                pass

            # Print statistics every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)

        # Print final statistics
        print_stats(stats, filesize)

    except KeyboardInterrupt:
        # Handle keyboard interruption and print final statistics
        print_stats(stats, filesize)
        raise
