from xtrace_sdk.crypto.paillier_client import PaillierClient
from xtrace_sdk.retrievers.simple_retriever import SimpleRetriever
from xtrace_sdk.crypto.encryption.aes import AESClient
from xtrace_sdk.utils.embedding import Embedding
from xtrace_sdk.integrations.xtrace.storage import XTraceStorage
from xtrace_sdk.integrations.xtrace.compute import XTraceCompute
from xtrace_sdk.data_loaders.txt_loader import TxtLoader


class XTraceConnector:
    """Implements the connection to XTrace service.
    """
    def __init__(self, xtrace_api_key: str, organization_id: str, knowledge_base_id: str, AES_key: str, Homomorphic_key_path: str):
        storage = XTraceStorage(xtrace_api_key)
        compute = XTraceCompute(xtrace_api_key)
        self.organization_id = organization_id
        self.knowledge_base_id = knowledge_base_id
        embedding = Embedding()
        aes_client = AESClient(AES_key)
        paillier_client = PaillierClient(512,1024,Homomorphic_key_path)
        self.retriever = SimpleRetriever(embedding, aes_client, paillier_client, compute)
        self.data_loader = TxtLoader(embedding, aes_client, paillier_client, storage) #could be any data loader

    def search(self, query: str, top_k: int = 3, meta_filter:dict = None) -> list:
        """Search for the most relevant documents in the knowledge base.
        """
        ids = self.retriever.nn_search_for_ids(query,top_k,meta_filter=meta_filter, kb_id=self.knowledge_base_id, org_id=self.organization_id)
        results = self.retrieve_and_decrypt(ids,kb_id=self.knowledge_base_id)
        return results

    def store(self, data):
        """Store data in the knowledge base.
        """
        documents = [data] # data should be of format {'chunk_content': '...', 'meta_data': {'key': 'value'}}
        index,db = self.data_loader.load_data_from_memory(documents)
        self.data_loader.dump_db(db,index=index,kb_id=self.knowledge_base_id, org_id=self.organization_id,meta_data=[data['meta_data']])