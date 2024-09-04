import collections

with open('data/rw_afiles.txt') as f:
  rw_afiles = [afile.strip() for afile in f]

with open('data/gdrive_afiles.txt') as f:
  gdrive_afiles = [afile.strip() for afile in f]

rw_dupes = [item for item, count in collections.Counter(rw_afiles).items() if count > 1]
gd_dupes = [item for item, count in collections.Counter(gdrive_afiles).items() if count > 1]

if rw_dupes:
  print(f'RW has afile number dupes: {rw_dupes}\n')
if gd_dupes:
  print(f'GD has afile number dupes: {gd_dupes}\n')

in_rw_not_gd = list(set(rw_afiles) - set(gdrive_afiles))
in_gd_not_rw = list(set(gdrive_afiles) - set(rw_afiles))

with open('data/in_rw_not_gd.txt', 'w+') as file:
  file.write("\n".join(in_rw_not_gd))

with open('data/in_gd_not_rw.txt', 'w+') as file:
  file.write("\n".join(in_gd_not_rw))

# File.open('data/in_rw_not_gd.txt', 'w+') do |f|
#   f.puts in_rw_not_gd
# end

# File.open('data/in-gd-not-rw.txt', 'w+') do |f|
#   f.puts in_gd_not_rw
# end





