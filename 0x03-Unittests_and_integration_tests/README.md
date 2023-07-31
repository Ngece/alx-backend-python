test_client.py              Contains: 
    unit tests for utils.access_nested_map.

    Implements TestAccessNestedMap.test_access_nested_map_exception. Uses the assertRaises context manager to test that a KeyError is raised for the inputs (using @parameterized.expand)

    Defines the TestGetJson(unittest.TestCase) class and implements the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.

    Implements the TestMemoize(unittest.TestCase) class with a test_memoize method.





test_client.py              Contains:
    a new test_client.py file, declares the TestGithubOrgClient(unittest.TestCase) class and implements the test_org method.
    This method tests that GithubOrgClient.org returns the correct value.
    Uses @patch as a decorator to make sure get_json is called once with the expected argument and is not executed.
    Uses @parameterized.expand as a decorator to parameterize the test with a couple of org examples to pass to GithubOrgClient, in this order:
        google
        abc

    Implements the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.
    Uses patch as a context manager to patch GithubOrgClient.org and makes it return a known payload.
    Tests that the result of _public_repos_url is the expected one based on the mocked payload.

    Implements TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.
    Uses @patch as a decorator to mock get_json and makes it return a payload of choice.
    Uses patch as a context manager to mock GithubOrgClient._public_repos_url and returns a value of choice.
    Tests that the list of repos is what is expected from the chosen payload.
    Tests that the mocked property and the mocked get_json was called once.

    Implements TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.
    Contains TestIntegrationGithubOrgClient(unittest.TestCase) class and implements the setUpClass and tearDownClass which are part of the unittest.TestCase API.
    Uses @parameterized_class to decorate the class and parameterizes it with fixtures found in fixtures.py. The file contains the following fixtures:
        org_payload, repos_payload, expected_repos, apache2_repos
    The setupClass mocks requests.get to return example payloads found in the fixtures.
    Uses patch to start a patcher named get_patcher, and uses side_effect to make sure the mock of requests.get(url).json() returns the correct fixtures for the various values of url that you anticipate to receive.
    Implements the tearDownClass class method to stop the patcher.


    Implements the test_public_repos method to test GithubOrgClient.public_repos.
    Makes sure that the method returns the expected results based on the fixtures.
    Implements test_public_repos_with_license to test the public_repos with the argument license="apache-2.0" and makes sure the result matches the expected value from the fixtures.