 You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8502
  Network URL: http://10.131.132.26:8502

────────────────────────── Traceback (most recent call last) ───────────────────────────
  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\streamlit
  \runtime\scriptrunner\exec_code.py:129 in exec_func_with_error_handling

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\streamlit
  \runtime\scriptrunner\script_runner.py:671 in code_to_exec

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\frontend\app.py:6 in <module>

     3 sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
     4 import streamlit as st
     5 from backend.blob_utils import load_schema_from_blob
  ❱  6 from backend.index_manager import create_collection_if_not_exists, upload_schem
     7 from backend.retrieval import retrieve_relevant_schema_chroma
     8 from backend.sql_generator import generate_sql
     9 def main():

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\backend\index_manager.py:7 in
  <module>

      4 
      5 from typing import List, Union
      6 
  ❱   7 from backend.chroma_client import get_or_create_collection
      8 
      9 from backend.embeddings import generate_embedding
     10 

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\backend\chroma_client.py:3 in
  <module>

     1 # chroma_client.py
     2 import os
  ❱  3 from chromadb import PersistentClient
     4 from backend import config
     5 from backend.azure_clients import logger  # optional reuse of your logger
     6 

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\chromadb\
  __init__.py:3 in <module>

      1 from typing import Dict, Optional
      2 import logging
  ❱   3 from chromadb.api.client import Client as ClientCreator
      4 from chromadb.api.client import AdminClient as AdminClientCreator
      5 from chromadb.auth.token import TokenTransportHeader
      6 import chromadb.config

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\chromadb\
  api\__init__.py:7 in <module>

      4 
      5 from overrides import override
      6 from chromadb.config import DEFAULT_DATABASE, DEFAULT_TENANT
  ❱   7 from chromadb.api.models.Collection import Collection
      8 from chromadb.api.types import (
      9 │   CollectionMetadata,
     10 │   Documents,

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\chromadb\
  api\models\Collection.py:7 in <module>

      4 from pydantic import BaseModel, PrivateAttr
      5 
      6 from uuid import UUID
  ❱   7 import chromadb.utils.embedding_functions as ef
      8 
      9 from chromadb.api.types import (
     10 │   URI,

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\chromadb\
  utils\embedding_functions.py:6 in <module>

      3 
      4 from tenacity import stop_after_attempt, wait_random, retry, retry_if_exceptio
      5 
  ❱   6 from chromadb.api.types import (
      7 │   Document,
      8 │   Documents,
      9 │   Embedding,

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\chromadb\
  api\types.py:101 in <module>

     98 
     99 
    100 # Images
  ❱ 101 ImageDType = Union[np.uint, np.int_, np.float_]
    102 Image = NDArray[ImageDType]
    103 Images = List[Image]
    104 

  C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\numpy\__i
  nit__.py:791 in __getattr__

    788 │   │   │   raise AttributeError(__former_attrs__[attr], name=None)
    789 │   │   
    790 │   │   if attr in __expired_attributes__:
  ❱ 791 │   │   │   raise AttributeError(
    792 │   │   │   │   f"`np.{attr}` was removed in the NumPy 2.0 release. "
    793 │   │   │   │   f"{__expired_attributes__[attr]}",
    794 │   │   │   │   name=None
────────────────────────────────────────────────────────────────────────────────────────
AttributeError: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64`
instead.
