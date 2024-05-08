import unittest
from queue import Queue
from threading import Event
from acto.utils.acto_timer import ActoTimer

class TestActoTimer(unittest.TestCase):

    def test_cancel(self):
        # Create timer
        queue = Queue()
        timer = ActoTimer(10, queue, "message")
        
        # Start timer
        timer.start()
        
        # Cancel timer
        timer.cancel()
        
        # Assert that timer is finished
        self.assertTrue(timer.finished.is_set())
        
        # Assert that queue is empty
        self.assertTrue(queue.empty())

    def test_reset(self):
        # Create timer
        queue = Queue()
        timer = ActoTimer(10, queue, "message")
        
        # Start timer
        timer.start()
        
        # Reset timer
        timer.reset()
        
        # Assert that resetted flag is set
        self.assertTrue(timer.resetted)
        
        # Assert that queue is empty
        self.assertTrue(queue.empty())

    def test_run(self):
        # Create timer
        queue = Queue()
        timer = ActoTimer(0.5, queue, "message")
        
        # Start timer
        timer.start()
        
        # Wait for timer to finish
        timer.join()
        
        # Assert that queue contains the message
        self.assertEqual(queue.get(), "message")
        
        # Assert that timer is finished
        self.assertTrue(timer.finished.is_set())

if __name__ == '__main__':
    unittest.main()
