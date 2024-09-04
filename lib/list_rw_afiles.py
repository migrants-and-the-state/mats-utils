import glob
import os

glob_path   = '/Volumes/migrants_state/pdfs/*.pdf'
pdf_paths   = glob.glob(glob_path)
result_path = 'data/rw_afiles.txt'
afile_nos   = []

for path in pdf_paths:
  afile_no = os.path.basename(path)
  afile_no = afile_no.replace('.pdf', '')
  afile_no = afile_no.replace('_redacted', '')
  afile_no = afile_no.replace('_withdrawal', '')
  
  afile_nos.append(afile_no)

with open(result_path, 'w+') as file:
  file.write("\n".join(afile_nos))