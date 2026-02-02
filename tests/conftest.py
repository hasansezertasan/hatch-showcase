# SPDX-FileCopyrightText: 2021-present Ofek Lev <oss@ofek.dev>
#
# SPDX-License-Identifier: MIT
import pytest
from typer.testing import CliRunner

from hatch_showcase.cli import app


@pytest.fixture(scope='session')
def runner():
    return CliRunner()


@pytest.fixture(scope='session')
def hatch_showcase(runner):
    def invoke(*args, **kwargs):
        return runner.invoke(app, args, **kwargs)

    return invoke
