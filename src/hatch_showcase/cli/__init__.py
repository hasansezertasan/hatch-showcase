# SPDX-FileCopyrightText: 2021-present Ofek Lev <oss@ofek.dev>
#
# SPDX-License-Identifier: MIT
import typer

from hatch_showcase._version import version
from hatch_showcase.fib import fibonacci

app = typer.Typer()


def version_callback(value: bool) -> None:  # noqa: FBT001
    if value:
        typer.echo(f'hatch-showcase {version}')
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(  # noqa: FBT001
        False,
        '--version',
        '-V',
        callback=version_callback,
        is_eager=True,
        help='Show version and exit.',
    ),
) -> None:
    """A project showcasing features and plugins for Hatch."""


@app.command()
def fib(n: int) -> None:
    """Calculate the nth Fibonacci number."""
    typer.echo(fibonacci(n))


hatch_showcase = app
