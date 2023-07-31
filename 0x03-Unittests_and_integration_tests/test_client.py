#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient Class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')  # Patch the get_json function
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        test_payload = {'payload_key': 'payload_value'}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), test_payload)
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org_name))

    @patch('client.GithubOrgClient.org')  # Patch the org property
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property"""
        test_payload = {'repos_url': 'https://example.com/repos'}
        mock_org.return_value = test_payload
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, test_payload['repos_url'])

class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient Class"""

    @classmethod
    def setUpClass(cls):
        """Set up for integration test"""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down for integration test"""
        cls.get_patcher.stop()

    @parameterized.expand([
        ('org_payload', 'expected_repos'),
        ('repos_payload', 'apache2_repos'),
    ])
    @patch('client.GithubOrgClient.org')
    def test_public_repos(self, payload_fixture, expected_repos_fixture, mock_org):
        """Integration test for public_repos method"""
        client = GithubOrgClient("test_org")
        mock_org.return_value = globals()[payload_fixture]
        expected_repos = globals()[expected_repos_fixture]
        self.assertEqual(client.public_repos(), expected_repos)

    @patch('client.GithubOrgClient.org')
    def test_public_repos_with_license(self, mock_org):
        """Integration test for public_repos method with license argument"""
        client = GithubOrgClient("test_org")
        mock_org.return_value = globals()['org_payload']
        expected_repos = globals()['apache2_repos']
        self.assertEqual(client.public_repos(license="apache-2.0"), expected_repos)

if __name__ == '__main__':
    unittest.main()
