import collections

with open('data/source_lists/rw_afiles.txt') as f:
  rw_afiles = [afile.strip() for afile in f]

with open('data/source_lists/gdrive_afiles.txt') as f:
  gdrive_afiles = [afile.strip() for afile in f]

with open('data/source_lists/gh_json_afiles.txt') as f:
  gh_json_afiles = [afile.strip() for afile in f]

with open('data/source_lists/gh_ocr_afiles.txt') as f:
  gh_ocr_afiles = [afile.strip() for afile in f]

rw_dupes      = [item for item, count in collections.Counter(rw_afiles).items() if count > 1]
gd_dupes      = [item for item, count in collections.Counter(gdrive_afiles).items() if count > 1]
gh_json_dupes = [item for item, count in collections.Counter(gh_json_afiles).items() if count > 1]
gh_ocr_dupes = [item for item, count in collections.Counter(gh_ocr_afiles).items() if count > 1]

if rw_dupes:
  print(f'RW has afile number dupes: {rw_dupes}\n')
if gd_dupes:
  print(f'GD has afile number dupes: {gd_dupes}\n')
if gh_json_dupes:
  print(f'GH has json afile number dupes: {gh_json_dupes}\n')
if gh_ocr_dupes:
  print(f'GH has ocr afile number dupes: {gh_ocr_dupes}\n')

in_rw_not_gd          = list(set(rw_afiles) - set(gdrive_afiles))
in_rw_not_gh_json     = list(set(rw_afiles) - set(gh_json_afiles))

in_gd_not_rw          = list(set(gdrive_afiles) - set(rw_afiles))
in_gd_not_gh_json     = list(set(gdrive_afiles) - set(gh_json_afiles))

in_gh_json_not_rw     = list(set(gh_json_afiles) - set(rw_afiles))
in_gh_json_not_gd     = list(set(gh_json_afiles) - set(gdrive_afiles))

rw_missing_gd_vs_gh_missing_gd = list(set(in_gd_not_rw) - set(in_gd_not_gh_json))

# in_gh_json_not_gh_ocr = list(set(gh_json_afiles) - set(gh_ocr_afiles))
# in_gh_ocr_not_gh_json = list(set(gh_ocr_afiles) - set(gh_json_afiles))

with open('data/comps/in_rw_not_gd.txt', 'w+') as file:
  file.write("\n".join(in_rw_not_gd))

with open('data/comps/in_gd_not_rw.txt', 'w+') as file:
  file.write("\n".join(in_gd_not_rw))

with open('data/comps/in_gh_not_rw.txt', 'w+') as file:
  file.write("\n".join(in_gh_json_not_rw))

with open('data/comps/in_gd_not_gh.txt', 'w+') as file:
  file.write("\n".join(in_gd_not_gh_json))
