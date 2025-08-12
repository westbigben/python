"""Typer example — small CLI with a greet command."""
import typer

app = typer.Typer(help='Small Typer demo')

@app.command()
def greet(name: str, excited: bool = False):
    """Greet someone by name. Use --excited for an exclamation."""
    msg = f'Hello, {name}'
    if excited:
        msg += '!!!'
    typer.echo(msg)

if __name__ == '__main__':
    app()
