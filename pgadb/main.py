from alembic import config
from pathlib import Path
from typing import Dict, List, Optional
from alembic.config import Config
from alembic import command
from pgadb import import_commands
import typer
import pandas as pd
import os


app = typer.Typer()
app.add_typer(import_commands.app, name="import")


@app.command()
def foo():
    typer.echo(typer.get_app_dir("pgadb", force_posix=True))
    config = Config(os.path.join(os.path.dirname(__file__), "alembic.ini"))
    command.upgrade(config, revision="head")
