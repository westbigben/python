from rich.progress import Progress
from rich.console import Console
import time

console = Console()

with Progress(console=console) as progress:
    task = progress.add_task("Processing", total=100)

    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.1)