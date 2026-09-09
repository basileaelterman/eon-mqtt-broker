import subprocess
from utils import run_script


def test_up_script_creates_env_file() -> bool:
    result: subprocess.CompletedProcess = run_script("scripts/up.sh")
    
    assert result.returncode == 0