import os
import subprocess
from pathlib import Path


def is_file(file: str) -> bool:
    """Checks whether the provided path is a file.

    Args:
        file (str): The path to the file.

    Returns:
        bool: True if the file exists, False if it does not.
    """
    return os.path.isfile(file)


def has_suffix(file: str, suffix: str) -> bool:
    """Checks whether the provided file's suffix matches.

    Args:
        file (str): The path to a file.
        suffix (str): The suffix of a file.

    Returns:
        bool: True if the suffix of the file matches, False if it does not.
    """
    return Path(file).suffix == suffix


def run_script(script: str) -> subprocess.CompletedProcess:
    """Run the script from the provided location.

    Args:
        script (str): A location of the script to be run.

    Raises:
        FileNotFoundError: When the provided path does not contain a file.
        ValueError: When the provided path is not a bash script.

    Returns:
        subprocess.CompletedProcess: The result of running the script.
    """
    if not is_file(script):
        raise FileNotFoundError(f"No file found at {script}")

    suffix: str = ".sh"
    
    if not has_suffix(script, suffix):
        raise ValueError(f"Expected a {suffix} file, got: {script}")

    return subprocess.run(["bash", script], capture_output=True, check=True)