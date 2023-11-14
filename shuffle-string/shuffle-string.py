import random
import argparse
import sys
import os

def shuffle_text(input_text, length=None, count=1):
    shuffled_texts = []

    for _ in range(count):
        shuffled_text = list(input_text)
        random.shuffle(shuffled_text)
        if length:
            shuffled_text = shuffled_text[:length]
        shuffled_texts.append(''.join(shuffled_text))

    return shuffled_texts

def main():
    parser = argparse.ArgumentParser(description='Shuffle the content of a text file.')
    parser.add_argument('-i', '--input_file', required=True, type=argparse.FileType('r'), help='Path to the input text file')
    parser.add_argument('-l', '--length', type=int, help='Length of the shuffled output')
    parser.add_argument('-o', '--output_file', help='Path to the output text file')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of shuffled strings to generate')

    args = parser.parse_args()

    try:
        input_text = args.input_file.read().strip()
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file.name}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

    if args.output_file and os.path.exists(args.output_file):
        overwrite = input(f"The output file '{args.output_file}' already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print("Operation canceled.")
            sys.exit(0)

    shuffled_texts = shuffle_text(input_text, args.length, args.count)

    if args.output_file:
        with open(args.output_file, 'w') as output_file:
            for i, shuffled_text in enumerate(shuffled_texts, 1):
                output_file.write(f"{shuffled_text}\n")
        print(f"{args.count} shuffled strings saved to '{args.output_file}'")
    else:
        for i, shuffled_text in enumerate(shuffled_texts, 1):
            print(shuffled_text)

if __name__ == "__main__":
    main()
