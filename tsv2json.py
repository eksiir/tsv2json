#! /usr/bin/env python3

import argparse
import csv
import json


def convert_tsv_to_json(input_file, output_file):
  """
  Converts a TSV file to JSON with keywords as an array of strings.

  Args:
    input_file: Path to the input TSV file.
    output_file: Path to the output JSON file.
  """
  data = []
  fieldnames = None

  with open(input_file, 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
      if not fieldnames:
        fieldnames = row.keys()
      # Convert keywords to a list and assign to the row
      row['keywords'] = json.loads(row['keywords'])
      data.append(row)

  with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Convert TSV to JSON.')
  parser.add_argument('-i', '--input', help='Input TSV file', required=True)
  parser.add_argument('-o', '--output', help='Output JSON file', required=True)
  args = parser.parse_args()

  convert_tsv_to_json(args.input, args.output)
  print(f'Converted TSV to JSON: {args.output}')
