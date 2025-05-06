# xtrace-mcp-server

> The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open protocol that enables
> seamless integration between LLM applications and external data sources and tools. Whether you're building an
> AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to
> connect LLMs with the context they need.


This repository is an example of how to create a MCP server for XTrace vector database which uses partially homomorphic encryption for privacy preserving semantic search. 

## Overview

An official Model Context Protocol server for keeping and retrieving memories in the XTrace encrypted vector db. It acts as a encrypted semantic memory layer for LLMs. 

## Components

### Tools

1. `xtrace-store`
    - Store some data in Xtrace's encrypted vector db for later retrieval
    - Input:
        - `data` (string): textual data to store
        - `meta_data` (JSON): Optional metadata tp store
    - Returns: success msg
2. `xtrace-search`
    - Retrieve relevant data from XTrace with encrypted query. 
    - Input:
        - `query` (string): Query to use for searching
    - Returns: list of most relevant data


## Environment Variables

The configuration of the server is done using environment variables:

| Name                     | Description                                                         | Default Value                                                     |
|--------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------|
| `XTrace_API_KEY`         | API key for the XTrace servvice                                     | None                                                              |
| `KNOWLEDGE_BASE_ID`      | ID of the Knowledge base to use                                     | None                                                              |
| `ORGANIZATION_ID`        | ID of the Organization registered at XTrace                         | None                                                              |
| `HOMOMORPHIC_KEY_PATH`   | Path to the locally stored secret key for homomorphic encryption    | None                                                              |
| `AES_KEY`                | AES Key used for encrypting/decrypting plain text                   | None                                                              |


## Installation

Make sure `xtrace-sdk` is installed. TODO.

## Testing
TODO