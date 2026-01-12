PS C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis> .venv/scripts/activate
(.venv) PS C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis> streamlit run frontend/app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.131.132.26:8501

Chroma query failed: Error executing plan: Error sending backfill request to compactor: Error constructing hnsw segment reader: Error creating hnsw segment reader: Error loading hnsw index
Traceback (most recent call last):
  File "C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\backend\retrieval.py", line 77, in retrieve_relevant_schema_chroma
    results = coll.query(

    ...<5 lines>...

    )
  File "C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\chromadb\api\models\Collection.py", line 229, in query
    query_results = self._client._query(
        collection_id=self.id,
    ...<7 lines>...
        database=self.database,
    )
  File "C:\Users\2097831\Source\OSPAI_QNXT_Schema_Analysis\.venv\Lib\site-packages\chromadb\api\rust.py", line 539, in _query
    rust_response = self.bindings.query(
        str(collection_id),
    ...<7 lines>...
        database,
    )
chromadb.errors.InternalError: Error executing plan: Error sending backfill request to compactor: Error constructing hnsw segment reader: Error creating hnsw segment reader: Error loading hnsw index
