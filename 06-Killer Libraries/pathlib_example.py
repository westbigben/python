"""Pathlib example — traverse current folder and search files containing a pattern."""
from pathlib import Path

BASE = Path(__file__).parent

def main():
    print(f'Pathlib demo — listing files in {BASE}')
    files = list(BASE.iterdir())
    for p in files:
        print("-", p.name)
    # Search for files with 'sample' in name
    print('\nFiles containing "sample":')
    for p in BASE.rglob('*'):
        if p.is_file() and 'sample' in p.name.lower():
            print('-', p.name)

if __name__ == '__main__':
    main()
