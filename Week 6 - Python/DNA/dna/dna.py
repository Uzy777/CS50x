import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py [data.csv] [sequence.txt]")

    csv_file = sys.argv[1]
    txt_file = sys.argv[2]

    # TODO: Read database file into a variable
    rows = []
    with open(csv_file) as file:
        reader_csv = csv.DictReader(file)
        for row in reader_csv:
            rows.append(row)
        # print(rows)

    # TODO: Read DNA sequence file into a variable
    with open(txt_file) as file:
        sequence = file.read().strip()
        # print(sequence)

    # TODO: Find longest match of each STR in DNA sequence
    # Extract the STRs from the first row of the CSV file
    strs = reader_csv.fieldnames[1:]

    # Find the longest match of each STR in the DNA sequence
    longest_matches = {}
    for str in strs:
        longest_matches[str] = longest_match(sequence, str)
    # print(longest_matches)

    # TODO: Check database for matching profiles
    for row in rows:
        match = True
        for str in strs:
            if int(row[str]) != longest_matches[str]:
                match = False
                break
        if match:
            print(row["name"])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
