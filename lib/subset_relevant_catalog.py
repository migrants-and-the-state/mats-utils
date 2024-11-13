import csv
import os
import re

from tqdm import tqdm

LOOKUP_FILE       = 'data/catalog/anum_lookup.csv'
FULL_CATALOG_FILE = 'data/catalog/SF_and_KC_OR_YYYY.csv'
RESULTS_FILE      = 'data/catalog/matched_subset_results.csv'
NOT_FOUND_LOOKUP  = 'data/catalog/unmatched_nara.csv'

def write_to_result(anumber, dict):
  with open(RESULTS_FILE, 'a') as file:
    dict['ANUMBER'] = anumber
    file.write(','.join(dict.values()))
    file.write('\n')

def normalize_anum(anum):
  return re.split(r'^(A0+|0+|A+)', anum)[-1]

print('Getting started...')

# read the lookup file
with open(LOOKUP_FILE, 'r') as file:
  ms_lookup = {}
  reader = csv.reader(file)
  next(reader, None) # skip header row
  for row in reader:
    if not row[1].endswith('USCIS'): # ignore USCIS files, match only NARA
      ms_lookup[normalize_anum(row[0])] = {
        'anumber': row[0],
        'og_id': row[1]
      }
          
print(f"Looking for {len(ms_lookup)} NARA A-Files...")

# get a flat, unique, & sorted list of normalized anums from the lookup file
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
    catalog_anum = normalize_anum(dict['ANUMBER'])
    if catalog_anum in ms_anums: 
      matched_anums.append(catalog_anum)
      write_to_result(ms_lookup[catalog_anum]['anumber'], dict)

unmatched_anums = [item for item in ms_anums if item not in matched_anums]

print(f"Found {len(matched_anums)} matches!")
print(f"Logging {len(unmatched_anums)} unmatched a numbers.")

with open(NOT_FOUND_LOOKUP, 'a') as file:
  for anum in unmatched_anums:
    file.write(f"{ms_lookup[anum]['anumber']},{ms_lookup[anum]['og_id']}")
    file.write('\n')