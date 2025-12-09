#!/usr/bin/env python3

import argparse
import os



def align_text_by_char(text, ch):
	lines = [line.strip() for line in text.split("\n")]
	return "\n".join(lines)


def main():
	parser = argparse.ArgumentParser(description="Align a file")
	parser.add_argument("files", nargs="+", help="Text files to process")
	parser.add_argument("-c", "--char", default=",", help="Specify the character")
	parser.add_argument("-o", "--output", help="Specify the output file")
	parser.add_argument("-r", "--replace", action='store_true', help="Specify the character")
	args = parser.parse_args()

	if args.output and args.replace:
		print(f"Both --output and --replace were specified!")
		return

	for file in args.files:
		if os.path.isfile(file):
			print(f"Found: {file}")
			with open(file) as f:
				text = f.read()

			output_text = align_text_by_char(text, args.char)
			if args.replace:
				with open(file, "w") as f:
					f.write(output_text)
				print(f"Saved: {file}")
			else:
				print(output_text)
		else:
			print(f"Not found: {file}")


if __name__ == '__main__':
	main()
