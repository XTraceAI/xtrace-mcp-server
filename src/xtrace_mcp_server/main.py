import argparse
from xtrace_mcp_server.server import XTraceMCPServer
import os

def main():
    """
    Main entry point for the XTrace MCP server.
    """

    parser = argparse.ArgumentParser(description="mcp-server-xtrace")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="stdio",
    )
    args = parser.parse_args()

    xtrace_mcp_server = XTraceMCPServer(
        xtrace_api_key=os.environ["XTRACE_API_KEY"],
        organization_id=os.environ["ORGANIZATION_ID"],
        knowledge_base_id=os.environ["KNOWLEDGE_BASE_ID"],
        AES_key=os.environ['AES_KEY'],
        Homomorphic_key_path=os.environ['HOMOMORPHIC_KEY_PATH'],
        name="XTraceMCPServer",
        instructions="You are an XTrace MCP server. You can store and search for information in the XTrace knowledge base.",
    )
    xtrace_mcp_server.run(transport=args.transport)