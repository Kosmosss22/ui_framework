import os
import tempfile

import pytest
from logger import setup_logger


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()

@pytest.fixture
def temp_file():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Hello world")
        file_path = f.name

    yield file_path

    os.unlink(file_path)