import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    people = []
    with open(sys.argv[1], 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            person = {row[0]: row[1:]}
            people.append(person)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as f:
        reader = csv.reader(f)
        sequence = next(reader)

    # TODO: Find longest match of each STR in DNA sequence
    counts = []
    for srt in header[1:]:
        x = str(longest_match(sequence[0], srt))
        counts.append(x)
    # TODO: Check database for matching profiles
    for person in people:
        for key, val in person.items():
            if counts == val:
                return print(key)

    return print("No match")


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
