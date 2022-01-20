import typer
from pgadb import import_commands, db_commands


app = typer.Typer()
app.add_typer(import_commands.app, name="import")
app.add_typer(db_commands.app, name="db")
