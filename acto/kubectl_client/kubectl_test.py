import unittest
from unittest.mock import MagicMock, patch
from acto.kubectl_client.kubectl import KubectlClient, subprocess

class TestKubectlClient(unittest.TestCase):
    """Test KubectlClient"""

    def setUp(self):
        """Set up test data"""
        self.kubeconfig = "/test/kube/config"
        self.context_name = "test_context"
        self.client = KubectlClient(self.kubeconfig, self.context_name)

    def test_kubectl_client_initialization(self):
        """Test KubectlClient initialization"""
        self.assertEqual(self.client.kubeconfig, self.kubeconfig)
        self.assertEqual(self.client.context_name, self.context_name)

    @patch("subprocess.run")
    def test_exec_method(self, mock_run):
        """Test exec method"""
        pod = "test_pod"
        namespace = "test_namespace"
        commands = ["command1", "command2"]
        expected_cmd = [
            "exec", pod, "--namespace", namespace, "--", "command1", "command2"
        ]
        mock_result = MagicMock(spec=subprocess.CompletedProcess)
        mock_run.return_value = mock_result

        result = self.client.exec(pod, namespace, commands)


    @patch("subprocess.run")
    def test_kubectl_method(self, mock_run):
        """Test kubectl method"""
        args = ["get", "pods"]
        expected_cmd = [
            "kubectl", "--kubeconfig", self.kubeconfig, "--context", self.context_name,
            "get", "pods"
        ]
        mock_result = MagicMock(spec=subprocess.CompletedProcess)
        mock_run.return_value = mock_result

        result = self.client.kubectl(args)

        mock_run.assert_called_once_with(expected_cmd, capture_output=False, text=False, timeout=600)
        self.assertEqual(result, mock_result)

    @patch("subprocess.run")
    def test_kubectl_method_with_capture_output_and_text(self, mock_run):
        """Test kubectl method with capture_output and text parameters"""
        args = ["get", "pods"]
        expected_cmd = [
            "kubectl", "--kubeconfig", self.kubeconfig, "--context", self.context_name,
            "get", "pods"
        ]
        mock_result = MagicMock(spec=subprocess.CompletedProcess)
        mock_run.return_value = mock_result

        result = self.client.kubectl(args, capture_output=True, text=True)

        mock_run.assert_called_once_with(expected_cmd, capture_output=True, text=True, timeout=600)
        self.assertEqual(result, mock_result)

if __name__ == "__main__":
    unittest.main()
