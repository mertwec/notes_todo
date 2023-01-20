import click


@click.group()
def cli():
    print("Notes to do: ")


@cli.command("run")
@click.option("-r", "--auto-reload", default=True)
@click.option("--host", default='localhost')
@click.option("--port", type=int, default='5500')
def runserver(auto_reload, host, port):
    import uvicorn
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=auto_reload,
        workers=1,
    )

if __name__ == "__main__":
    cli()
