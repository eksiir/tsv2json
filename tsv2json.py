#! /usr/bin/env python3

import argparse
import csv
import json
import locale

def convert_tsv_to_json(input_file, output_file):
  """
  Converts a TSV file to JSON with keywords as an array of strings.

  Args:
    input_file: Path to the input TSV file.
    output_file: Path to the output JSON file.
  """
  data = []

  # Set the locale to the system default
  locale.setlocale(locale.LC_ALL, '')

  with open(input_file, 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
      row['_deleted'] = False
      row['createdAt'] = '2024-09-17T04:10:13.428+00:00'
      row['updatedAt'] = '2024-09-17T04:10:13.428+00:00'
      row['updatedBy'] = '5f4e994f025923001fdd6bc8'
      
      # `keywords` is one string of comma separated multiple strings.
      # replace that with an array of those strings and make sure there
      # are no empty string elemets in that array which can be created
      # from double commas or the original string ending in comma.
      keywords_arr = row['keywords'].split(',')
      row['keywords'] = [item.strip() for item in keywords_arr if item.strip()]
     
      data.append(row)

  with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Convert TSV to JSON.')
  parser.add_argument('-i', '--input', help='Input TSV file', required=True)
  parser.add_argument('-o', '--output', help='Output JSON file', required=True)
  args = parser.parse_args()

  convert_tsv_to_json(args.input, args.output)
  print(f'Converted TSV to JSON: {args.output}')
