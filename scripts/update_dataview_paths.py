import os

VAULT = '/home/skc/Documents/notevault'

files_to_update = ['gate-progress-tracker.md', 'test-series-dashboard.md', 'quiz-dashboard.md']

for fname in files_to_update:
    fpath = os.path.join(VAULT, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace Dataview FROM paths
        content = content.replace('FROM "Tests/GATE CSE PYQs"', 'FROM "tests/gate cse pyqs"')
        content = content.replace('FROM "Tests/GO Test Series"', 'FROM "tests/go test series"')
        content = content.replace('FROM "Tests/GO Test Series DA"', 'FROM "tests/go test series da"')
        content = content.replace('FROM "Tests/GATE Overflow 2027"', 'FROM "tests/gate overflow 2027"')
        content = content.replace('FROM "Tests/CSE Quizzes"', 'FROM "tests/cse quizzes"')
        content = content.replace('FROM "Tests/DA Quizzes"', 'FROM "tests/da quizzes"')
        content = content.replace('FROM "Tests"', 'FROM "tests"')
        
        # Replace links to dashboards
        content = content.replace('[[Test Series Dashboard]]', '[[test-series-dashboard|Test Series Dashboard]]')
        content = content.replace('[[Quiz Dashboard]]', '[[quiz-dashboard|Quiz Dashboard]]')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated Dataview queries in {fname}")

