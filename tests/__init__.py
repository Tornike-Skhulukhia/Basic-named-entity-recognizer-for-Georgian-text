import sys
from pathlib import Path

# FIX: add base directory to make absolute imports work in tests
# otherwise, pytest does not run files as modules, so absolute imports does not work
base_dir = Path(".").absolute()

sys.path.insert(0, str(base_dir))
