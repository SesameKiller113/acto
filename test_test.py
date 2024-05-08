import unittest
from unittest.mock import MagicMock, patch
import kubernetes
import kubernetes.client.models as kubernetes_models
from acto.system_state.deployment import DeploymentState

class TestDeploymentState(unittest.TestCase):

    def test_from_api_client_namespaced(self):
        api_client_mock = MagicMock()
        namespace = "test_namespace"

        with patch('your_module_name.list_namespaced_object_helper') as mock_list_helper:
            mock_list_helper.return_value = {
                "deployment1": kubernetes_models.V1Deployment(),
                "deployment2": kubernetes_models.V1Deployment(),
            }
            result = DeploymentState.from_api_client_namespaced(api_client_mock, namespace)

        self.assertIsInstance(result, DeploymentState)
        self.assertTrue(mock_list_helper.called)
        mock_list_helper.assert_called_once_with(
            kubernetes.client.AppsV1Api(api_client_mock).list_namespaced_deployment,
            namespace,
        )
        # Add more assertions if necessary

    def test_check_health(self):
        deployment_mock = MagicMock(spec=kubernetes_models.V1Deployment)
        deployment_mock.metadata.generation = 1
        deployment_mock.status.observed_generation = 1
        deployment_mock.spec.replicas = 2
        deployment_mock.status.ready_replicas = 2
        condition_mock1 = MagicMock()
        condition_mock1.type = "Available"
        condition_mock1.status = "True"
        condition_mock2 = MagicMock()
        condition_mock2.type = "Progressing"
        condition_mock2.status = "True"
        deployment_mock.status.conditions = [condition_mock1, condition_mock2]
        deployment_mock.status.replicas = 2
        deployment_mock.status.ready_replicas = 2
        deployment_mock.status.unavailable_replicas = None

        deployment_state = DeploymentState(root={"deployment1": deployment_mock})

        # Test healthy deployment
        is_healthy, reason = deployment_state.check_health()
        self.assertTrue(is_healthy)
        self.assertEqual(reason, "")

        # Test unhealthy deployment
        deployment_mock.status.ready_replicas = 1
        is_healthy, reason = deployment_state.check_health()
        self.assertFalse(is_healthy)
        self.assertEqual(reason, "Deployment[deployment1] replicas mismatch")
        # Add more assertions if necessary

    def test_serialize(self):
        deployment_mock = MagicMock(spec=kubernetes_models.V1Deployment)
        deployment_mock.to_dict.return_value = {"mock_key": "mock_value"}
        deployment_state = DeploymentState(root={"deployment1": deployment_mock})

        result = deployment_state.serialize()

        self.assertIsInstance(result, dict)
        self.assertEqual(result, {"deployment1": {"mock_key": "mock_value"}})
        # Add more assertions if necessary

if __name__ == '__main__':
    unittest.main()
