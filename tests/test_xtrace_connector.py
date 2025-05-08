import pytest
from xtrace_mcp_server.xtrace import XTraceConnector




@pytest.fixture
def xtrace_connector():
    """Fixture to create an instance of XTraceConnector."""
    return XTraceConnector(
        xtrace_api_key="your_api_key",
        organization_id="your_organization_id",
        knowledge_base_id="your_knowledge_base_id",
        AES_key="your_AES_key",
        Homomorphic_key_path="your_homomorphic_key_path"
    )


@pytest.fixture
def mock_data():
    """Fixture to create mock data for testing."""
    return {
        'chunk_content': 'This is a test document.',
        'meta_data': {'key': 'value'}
    }


def test_search(xtrace_connector, mock_data):
    xtrace_connector.store(mock_data)
    results = xtrace_connector.search("test document", top_k=3)

