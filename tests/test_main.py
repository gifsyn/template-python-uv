import pytest
from _pytest.capture import CaptureFixture

from template_python_uv.main import main


@pytest.mark.asyncio
async def test_main(capsys: CaptureFixture[str]) -> None:
    main()
    stdout = capsys.readouterr().out
    stderr = capsys.readouterr().err
    assert stdout == "Hello from app!\n"
    assert stderr == ""
