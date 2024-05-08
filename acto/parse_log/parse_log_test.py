import unittest
from acto.parse_log.parse_log import parse_log

class TestLogParser(unittest.TestCase):
    def test_klog_format(self):
        line = 'E0714 23:11:19.386396       1 pd_failover.go:70] PD failover replicas (0) reaches the limit (0), skip failover'
        parsed_log = parse_log(line)
        self.assertEqual(parsed_log['level'], 'error')
        self.assertEqual(parsed_log['msg'], 'PD failover replicas (0) reaches the limit (0), skip failover')


    def test_logrus_format(self):
        line = 'time="2022-08-08T03:21:56Z" level=info msg="deployment updated" deployment=rfs-test-cluster namespace=acto-namespace service=k8s.deployment src="deployment.go:102"'
        parsed_log = parse_log(line)
        self.assertEqual(parsed_log['level'], 'info')
        self.assertEqual(parsed_log['msg'], 'deployment updated')

    def test_json_format(self):
        line = '{"level":"error","ts":1655678404.9488907,"logger":"controller-runtime.injectors-warning","msg":"Injectors are deprecated, and will be removed in v0.10.x"}'
        parsed_log = parse_log(line)
        self.assertEqual(parsed_log['level'], 'error')
        self.assertEqual(parsed_log['msg'], 'Injectors are deprecated, and will be removed in v0.10.x')

if __name__ == '__main__':
    unittest.main()
