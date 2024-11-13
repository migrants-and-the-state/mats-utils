import csv
import os
import re

from tqdm import tqdm

LOOKUP_FILE       = 'data/catalog/anum_lookup.csv'
FULL_CATALOG_FILE = 'data/catalog/SF_and_KC_OR_YYYY.csv'
RESULTS_FILE      = 'data/catalog/matched_subset_results.csv'
NOT_FOUND_LOOKUP  = 'data/catalog/unmatched_nara.csv'

print('Getting started...')

# read the lookup file
with open(LOOKUP_FILE, 'r') as file:
  ms_lookup = {}
  reader = csv.reader(file)
  next(reader, None) # skip header row
  for row in reader:
    if not row[1].endswith('USCIS'): # ignore USCIS files, match only NARA
      ms_lookup[row[0]] = row[1]
          
print(f"Looking for {len(ms_lookup)} NARA A-Files...")

# get a flat, unique, & sorted list of anums from the lookup file
ms_anums = list(set(ms_lookup.keys()))
ms_anums.sort() 

matched_anums = []

# remove the previous results files if exist
try:
  os.remove(RESULTS_FILE)
except OSError:
  pass

try:
  os.remove(NOT_FOUND_LOOKUP)
except OSError:
  pass

# open bryan's full catalog csv
with open(FULL_CATALOG_FILE, 'r') as file:
  reader    = csv.DictReader(file)
  dictList  = list(reader)

  # create the results file and add the first header line
  with open(RESULTS_FILE, 'a') as file:
    file.write(','.join(dictList[0].keys()))
    file.write('\n')

  # create not matched table and add the first header line
  with open(NOT_FOUND_LOOKUP, 'a') as file:
    file.write('anumber,og_id')
    file.write('\n')

  # iterate through full catalog
  for dict in tqdm(dictList):
    tokens = re.split(r'^(0+|A+)', dict['ANUMBER'])
    normalized_anum = f"A{tokens[-1]}"

    # if a match is found, append it to the subset results file
    if normalized_anum in ms_anums:
      matched_anums.append(normalized_anum)
      with open(RESULTS_FILE, 'a') as file:
        dict['ANUMBER'] = normalized_anum
        file.write(','.join(dict.values()))
        file.write('\n')

with open(NOT_FOUND_LOOKUP, 'a') as file:
  for anum in [item for item in ms_anums if item not in matched_anums]:
    file.write(f"{anum},{ms_lookup[anum]}")
    file.write('\n')