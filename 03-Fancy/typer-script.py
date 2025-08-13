import typer

def greet(name: str = typer.Argument("World", help="Name to greet")):
    print(f"Hello {name}")

if __name__ == "__main__":
    typer.run(greet)