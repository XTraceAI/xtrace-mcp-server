from mcp.server.fastmcp import Context, FastMCP
from xtrace_mcp_server.xtrace import XTraceConnector


class XTraceMCPServer(FastMCP):
    """MCP server for XTrace.
    """
    def __init__(self, xtrace_api_key: str, organization_id: str, knowledge_base_id: str, AES_key: str, Homomorphic_key_path: str):
        super().__init__()
        self.xtrace_connector = XTraceConnector(xtrace_api_key, organization_id, knowledge_base_id, AES_key, Homomorphic_key_path)
    

    def setup_tools(self):
        """Setup tools for the MCP server.
        """
        def store(context: Context, data: str, meta_data: dict = None) -> str:
            """Store data in the knowledge base.
            """
            self.xtrace_connector.store({'chunk_content': data, 'meta_data': meta_data})
            return f"Remembered: {data} with meta data: {meta_data} in the knowledge base {self.xtrace_connector.knowledge_base_id}."

        
        def search(context: Context, query: str, top_k: int = 3, meta_filter: dict = None) -> str:
            """Search for the most relevant documents in the knowledge base.
            """
            results = self.xtrace_connector.search(query, top_k, meta_filter)
            return f"Found {len(results)} results for query: {query} in the knowledge base {self.xtrace_connector.knowledge_base_id}."