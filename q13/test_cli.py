import subprocess
import sys

def test_blank_name_exits_with_2():
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "   "],
        capture_output=True,
        text=True
    )
    assert result.returncode == 2
    assert "Error: name cannot be blank" in result.stderr

def test_normal_name():
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "Alice"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, Alice!"
