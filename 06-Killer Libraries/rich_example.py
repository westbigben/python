"""Rich example — display a colored table and a progress bar."""
from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

console = Console()

def table_demo():
    table = Table(title='Top Sellers')
    table.add_column('id', justify='right')
    table.add_column('name')
    table.add_column('revenue', justify='right')
    table.add_row('1', 'Alpha Widget', '$2998.50')
    table.add_row('2', 'Epsilon Thing', '$4750.00')
    console.print(table)

def progress_demo():
    console.print('\nProgress demo:')
    for i in track(range(20), description='Processing...'):
        time.sleep(0.05)

def main():
    console.print('[bold green]Rich demo[/bold green]')
    table_demo()
    progress_demo()

if __name__ == '__main__':
    main()
