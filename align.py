#!/usr/bin/env python3

import argparse
import os



def align_one_line(line, ch, col_lengths):
	columns = [col.strip() for col in line.split(ch)]
	if len(columns) == len(col_lengths):
		columns = [c.rjust(w) for c, w in zip(columns, col_lengths)]
		return f"{ch} ".join(columns)
	return line


def align_text_by_char(text, ch):
	lines = [line.strip() for line in text.split("\n")]
	non_empty_lines = [line for line in lines if line]

	if non_empty_lines:
		col_count = len(non_empty_lines[0].split(ch))
		col_lengths = [0 for _ in range(col_count)]

		for line in non_empty_lines:
			columns = [col.strip() for col in line.split(ch)]
			if len(columns) == col_count:
				for i in range(col_count):
					if len(columns[i]) > col_lengths[i]:
						col_lengths[i] = len(columns[i])

	lines = [align_one_line(line, ch, col_lengths) for line in text.split("\n")]
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
