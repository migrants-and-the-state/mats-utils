import csv
import os

from tqdm import tqdm

LOOKUP_FILE       = 'data/catalog/anum_lookup.csv'
FULL_CATALOG_FILE = 'data/catalog/SF_and_KC_OR_YYYY.csv'
RESULTS_FILE      = 'data/catalog/matched_subset_results.csv'

def extract_value(hash_list, key):
  return [h[key] for h in hash_list if key in h]

print('Getting started...')

# read the lookup file
with open(LOOKUP_FILE, 'r') as file:
  lookup = list(csv.DictReader(file))

# get a flat, sorted list of anums from the lookup file
anums = extract_value(lookup, 'anumber')
anums.sort() 

# remove the previous results file if it exists
try:
  os.remove(RESULTS_FILE)
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

  # iterate through full catalog
  for dict in tqdm(dictList):
    # if a match is found, append it to the subset results file
    if dict['ANUMBER'] in anums:
      with open(RESULTS_FILE, 'a') as file:
        file.write(','.join(dict.values()))
        file.write('\n')
    elif f"A{dict['ANUMBER']}" in anums: 
      dict['ANUMBER'] = f"A{dict['ANUMBER']}"
      with open(RESULTS_FILE, 'a') as file:
        file.write(','.join(dict.values()))
        file.write('\n')