import logging
from pathlib import Path
from typing import Optional

import pathspec

logger = logging.getLogger(__name__)


class KBIgnoreParser:
    """
    Parses a .kbignore file and determines if paths should be ignored.
    Uses pathspec for .gitignore-like matching.
    """

    def __init__(self, ignore_file_path: Optional[Path] = None):
        self._spec = None
        if ignore_file_path:
            self.load_patterns(ignore_file_path)

    def load_patterns(self, ignore_file_path: Path):
        """
        Loads patterns from the specified ignore file.
        """
        if not ignore_file_path.is_file():
            logger.warning(f"KBIgnore file not found at: {ignore_file_path}. No patterns will be loaded.")
            self._spec = None
            return

        try:
            with open(ignore_file_path, encoding="utf-8") as f:
                patterns = f.readlines()
            self._spec = pathspec.PathSpec.from_lines("gitwildmatch", patterns)
            logger.info(f"Loaded {len(patterns)} patterns from {ignore_file_path}.")
        except Exception as e:
            logger.error(f"Error loading KBIgnore file {ignore_file_path}: {e}")
            self._spec = None

    def is_ignored(self, file_path_relative_to_root: str) -> bool:
        """
        Checks if a file path (relative to the directory being scanned)
        should be ignored based on the loaded patterns.

        Args:
            file_path_relative_to_root: The file path relative to the root
                                        directory from which patterns are applied.
                                        Example: "subdir/file.txt", "another_file.log"
        Returns:
            True if the file_path should be ignored, False otherwise.
        """
        if not self._spec:
            return False

        # pathspec expects Unix-style paths for matching, even on Windows
        unix_path = file_path_relative_to_root.replace("\\", "/")

        if self._spec.match_file(unix_path):
            logger.debug(f"Path '{unix_path}' matches ignore pattern.")
            return True

        logger.debug(f"Path '{unix_path}' does not match ignore pattern.")
        return False


# Example Usage (for testing/demonstration)
if __name__ == "__main__":
    # Create a dummy .kbignore file and some test files structure
    test_dir = Path("./test_kbignore_dir")
    test_dir.mkdir(exist_ok=True)
    (test_dir / "test.txt").touch()
    (test_dir / "temp.log").touch()
    (test_dir / "subdir").mkdir(exist_ok=True)
    (test_dir / "subdir" / "another.txt").touch()
    (test_dir / "subdir" / "ignore_me.tmp").touch()
    (test_dir / "build").mkdir(exist_ok=True)
    (test_dir / "build" / "output.bin").touch()

    ignore_file_path = test_dir / ".kbignore"
    with open(ignore_file_path, "w") as f:
        f.write("# This is a test .kbignore file\n")
        f.write("*.log\n")  # Ignore all .log files
        f.write("subdir/*.tmp\n")  # Ignore .tmp files in subdir
        f.write("/build/\n")  # Ignore 'build' directory at root
        f.write("temp_dir/\n")  # Ignore 'temp_dir' anywhere (if it were created)
        f.write("!subdir/important.txt\n")  # Unignore specific file (not created here, but for example)

    print(f"--- Testing KBIgnoreParser with {ignore_file_path} ---")
    parser = KBIgnoreParser(ignore_file_path)

    # Test file paths relative to `test_dir`
    test_paths = [
        "test.txt",
        "temp.log",
        "subdir/another.txt",
        "subdir/ignore_me.tmp",
        "build/output.bin",
        "non_existent.file",
        "subdir/important.txt",  # Would be unignored if it existed
    ]

    for p in test_paths:
        print(f"Path '{p}': Ignored? {parser.is_ignored(p)}")

    # Clean up test files
    import shutil

    shutil.rmtree(test_dir)
