import random
import argparse
import sys
import os

# Function to shuffle the characters in input_text
def shuffle_text(input_text, length=None, count=1):
    # Create a set of unique characters from input_text and convert it to a list
    char_set = list(set(input_text))
    # List to store shuffled strings
    shuffled_texts = []

    # Iterate for the specified count to generate multiple shuffled strings
    for _ in range(count):
        # Make a copy of char_set to avoid modifying the original set
        shuffled_text = char_set.copy()
        # Shuffle the characters using random.shuffle
        random.shuffle(shuffled_text)
        # If length is specified, truncate the list to the specified length
        if length:
            shuffled_text = shuffled_text[:length]
        # Convert the list of characters back to a string and append to the result list
        shuffled_texts.append(''.join(shuffled_text))

    # Return the list of shuffled strings
    return shuffled_texts

# Main function to handle command-line arguments and execute the shuffling
def main():
    # Set up the argument parser with descriptions and help messages
    parser = argparse.ArgumentParser(description='Shuffle the content of a text file.')
    parser.add_argument('-i', '--input_file', required=True, type=argparse.FileType('r', encoding='utf-8'), help='Path to the input text file')
    parser.add_argument('-l', '--length', type=int, help='Length of the shuffled output')
    parser.add_argument('-o', '--output_file', help='Path to the output text file')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of shuffled strings to generate')

    # Parse the command-line arguments
    args = parser.parse_args()

    try:
        # Read the content of the input file and strip any leading/trailing whitespaces
        input_text = args.input_file.read().strip()
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file.name}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

    # Check if the output file exists and prompt the user for overwrite confirmation
    if args.output_file and os.path.exists(args.output_file):
        overwrite = input(f"The output file '{args.output_file}' already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print("Operation canceled.")
            sys.exit(0)

    # Call the shuffle_text function to generate shuffled strings
    shuffled_texts = shuffle_text(input_text, args.length, args.count)

    # Check if an output file is specified
    if args.output_file:
        # Open the output file in write mode
        with open(args.output_file, 'w') as output_file:
            # Iterate over shuffled strings, write to the file, and print to the console
            for i, shuffled_text in enumerate(shuffled_texts, 1):
                output_file.write(f"{shuffled_text}\n")
                print(f"{shuffled_text}\n")
        print(f"{args.count} shuffled strings saved to '{args.output_file}'")
    else:
        # If no output file is specified, simply print the shuffled strings to the console
        for i, shuffled_text in enumerate(shuffled_texts, 1):
            print(shuffled_text)

# Entry point to the script
if __name__ == "__main__":
    main()
