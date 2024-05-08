import unittest
from unittest.mock import MagicMock, patch
import sys
from multiprocessing import Process

from acto.utils.process_with_except import MyProcess


class TestMyProcess(unittest.TestCase):
    def test_run_method_with_exception(self):
        # Set up the exception hook
        original_excepthook = sys.excepthook
        sys.excepthook = MagicMock()

        # Create an instance of MyProcess and run the run() method
        process = MyProcess()
        with patch.object(Process, "run", side_effect=Exception("Test exception")):
            process.run()

        # Restore the original exception hook
        sys.excepthook = original_excepthook


if __name__ == "__main__":
    unittest.main()
