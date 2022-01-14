from alembic import config
from .models import schedule
from pathlib import Path
from sqlalchemy import create_engine
from typing import Dict, List, Optional
from alembic.config import Config
from alembic import command
import typer
import pandas as pd
import os


app = typer.Typer()
engine = create_engine("sqlite:///pga.db")


@app.command()
def load_schedule(file: Path, sheet: Optional[List[str]] = typer.Option(None)):
    """
    Load schedule(s) from an Excel file
    """
    sheets: Dict[str, pd.DataFrame]
    if not sheet:
        sheets = pd.read_excel(file, sheet_name=None)
    else:
        sheets = pd.read_excel(file, sheet_name=list(sheet))

    typer.echo(f"Found sheets: {', '.join(sheets.keys())}")

    insert = schedule.insert().prefix_with("OR REPLACE")

    with engine.begin() as conn:
        results = [
            conn.execute(insert, schedule_df.to_dict("records"))
            for schedule_df in sheets.values()
        ]

    typer.echo(f"Inserted a total of {sum([r.rowcount for r in results])} records")


@app.command()
def foo():
    typer.echo(typer.get_app_dir("pgadb"))
    config = Config(os.path.dirname(__file__) + "/alembic.ini")
    command.upgrade(config, revision="head")
