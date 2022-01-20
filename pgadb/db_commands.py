import typer
import os
from alembic.config import Config
from alembic import command


app = typer.Typer()


@app.command()
def upgrade():
    typer.echo(typer.get_app_dir("pgadb", force_posix=True))
    config = Config(os.path.join(os.path.dirname(__file__), "alembic.ini"))
    command.upgrade(config, revision="head")
