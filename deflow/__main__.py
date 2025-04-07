import typer

main = typer.Typer()


@main.command()
def hello(name: str):
    print(f"Hello {name}, this is DeFlow package.")


if __name__ == "__main__":
    main()
