import typer
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
from typing import Dict, List, Optional
from pgadb.models import schedule as _schedule


app = typer.Typer()
engine = create_engine("sqlite:///pga.db")


@app.command()
def schedule(file: Path, sheet: Optional[List[str]] = typer.Option(None)):
    """
    Load schedule(s) from an Excel file
    """
    sheets: Dict[str, pd.DataFrame]
    if not sheet:
        sheets = pd.read_excel(file, sheet_name=None)
    else:
        sheets = pd.read_excel(file, sheet_name=list(sheet))

    typer.echo(f"Found sheets: {', '.join(sheets.keys())}")

    insert = _schedule.insert().prefix_with("OR REPLACE")

    with engine.begin() as conn:
        results = [
            conn.execute(insert, schedule_df.to_dict("records"))
            for schedule_df in sheets.values()
        ]

    typer.echo(f"Inserted a total of {sum([r.rowcount for r in results])} records")
