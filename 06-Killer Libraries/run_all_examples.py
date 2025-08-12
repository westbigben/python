"""Interactive runner for all demos in this folder.
Press Enter to continue to the next demo, or type 'q' then Enter to quit.
"""
import subprocess, sys, os, time
from pathlib import Path

BASE = Path(__file__).parent
SCRIPTS = [
    'pandas_example.py',
    'requests_example.py',
    'beautifulsoup_example.py',
    'pathlib_example.py',
    'typer_example.py',        # note: Typer prints help when called with --help
    'rich_example.py',
    'schedule_example.py',
    'playwright_example.py'
]

def run_script(script):
    path = BASE / script
    print('\n' + '='*60)
    print(f'▶ Running: {script}')
    print('='*60 + '\n')
    # Run the script as a subprocess so missing deps don't crash this runner.
    try:
        completed = subprocess.run([sys.executable, str(path)], check=False)
    except Exception as e:
        print('Failed to run', script, 'Error:', e)

def prompt_continue():
    ans = input('\nPress Enter to continue to the next demo (or type q + Enter to quit): ').strip().lower()
    if ans == 'q':
        print('Quitting interactive demo. Goodbye!')
        return False
    return True

def main():
    print('Interactive demo runner: run_all_examples.py')
    for script in SCRIPTS:
        run_script(script)
        if script == 'typer_example.py':
            print('\nTip: Try `python typer_example.py --help` to see CLI usage.')
        cont = prompt_continue()
        if not cont:
            break
        # small pause so output is readable
        time.sleep(0.2)
    print('\nAll demos finished (or stopped by user).')

if __name__ == "__main__":
    main()
