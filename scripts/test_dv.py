import os
import shutil

VAULT = '/home/skc/Documents/notevault'
TESTS = os.path.join(VAULT, 'tests')

# Clean out old duplicate files with space in prefix
for root, dirs, files in os.walk(TESTS):
    for f in files:
        if ' - ' in f:
            os.remove(os.path.join(root, f))

# Update dashboards to use simplest dataview syntax
def make_simple_dv(folder_name):
    return f"""TABLE 
  choice(done, "✅", "❌") AS Done,
  file.link AS "Test Note",
  subject AS Subject,
  questions AS Questions,
  marks AS Marks,
  duration AS Duration
FROM "{folder_name}"
SORT file.name ASC"""

print("Cleaned up old files.")
