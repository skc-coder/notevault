import os
import shutil

VAULT = '/home/skc/Documents/notevault'

# 1. Rename root created markdown dashboard files
files_to_rename = {
    'GATE Progress Tracker.md': 'gate-progress-tracker.md',
    'Test Series Dashboard.md': 'test-series-dashboard.md',
    'Quiz Dashboard.md': 'quiz-dashboard.md'
}

for old_name, new_name in files_to_rename.items():
    old_path = os.path.join(VAULT, old_name)
    new_path = os.path.join(VAULT, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed file: {old_name} -> {new_name}")

# 2. Rename Tests folder to tests
tests_old = os.path.join(VAULT, 'Tests')
tests_new = os.path.join(VAULT, 'tests')

if os.path.exists(tests_old):
    # Rename subfolders and files inside Tests
    for root, dirs, files in os.walk(tests_old, topdown=False):
        for f in files:
            old_f_path = os.path.join(root, f)
            new_f_name = f.lower()
            new_f_path = os.path.join(root, new_f_name)
            if old_f_path != new_f_path:
                os.rename(old_f_path, new_f_path)
                
        for d in dirs:
            old_d_path = os.path.join(root, d)
            new_d_name = d.lower()
            new_d_path = os.path.join(root, new_d_name)
            if old_d_path != new_d_path:
                os.rename(old_d_path, new_d_path)
                
    os.rename(tests_old, tests_new)
    print("Renamed directory: Tests -> tests and all subdirectories/files to lowercase.")

print("Lowercasing complete.")
