import logging

import pytest
from _pytest.capture import CaptureFixture

from app.main import main

logger = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_main(capsys: CaptureFixture[str]) -> None:
    main()
    stdout = capsys.readouterr().out
    stderr = capsys.readouterr().err
    assert stdout == "Hello from app!\n"
    assert stderr == ""
