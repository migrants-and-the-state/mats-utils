import glob
import os

json_glob_path    = 'extracted-data/data/metadata_outputs/*.json'
ocr_glob_path     = 'extracted-data/data/text_ocr/*.txt'

json_paths        = glob.glob(json_glob_path)
ocr_paths         = glob.glob(ocr_glob_path)

json_result_path  = 'data/source_lists/gh_json_afiles.txt'
ocr_result_path   = 'data/source_lists/gh_ocr_afiles.txt'

json_afile_nos  = []
ocr_afile_nos   = []

for path in json_paths:
  afile_no = os.path.basename(path)
  afile_no = afile_no.replace('.json', '')
  afile_no = afile_no.replace('_redacted', '')
  afile_no = afile_no.split('_')[0]
  
  json_afile_nos.append(afile_no)


for path in ocr_paths:
  afile_no = os.path.basename(path)
  afile_no = afile_no.replace('.txt', '')
  afile_no = afile_no.replace('_redacted', '')
  afile_no = afile_no.split('_')[0]
  
  ocr_afile_nos.append(afile_no)

with open(json_result_path, 'w+') as file:
  file.write("\n".join(list(set(json_afile_nos))))

with open(ocr_result_path, 'w+') as file:
  file.write("\n".join(list(set(ocr_afile_nos))))
