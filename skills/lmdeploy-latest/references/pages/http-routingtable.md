# HTTP Routing Table — lmdeploy

Source: https://lmdeploy.readthedocs.io/en/latest/http-routingtable.html

HTTP Routing Table

/abort_request |
/distserve |
/generate |
/health |
/is_sleeping |
/metrics |
/nodes |
/pooling |
/sleep |
/terminate |
/update_weights |
/v1 |
/wakeup

| | /abort_request | |
| --- | --- | --- |
| | `POST /abort_request` | Abort Request |
| | /distserve | |
| | `GET /distserve/engine_info` | Engine Info |
| | `POST /distserve/connection_warmup` | Connection Warmup |
| | `POST /distserve/free_cache` | Free Cache |
| | `POST /distserve/gc` | Cache Block Gc To Be Migrated |
| | `POST /distserve/p2p_connect` | P2P Connect |
| | `POST /distserve/p2p_drop_connect` | P2P Drop Connect |
| | `POST /distserve/p2p_initialize` | P2P Initialize |
| | /generate | |
| | `POST /generate` | Generate |
| | /health | |
| | `GET /health` | Health |
| | /is_sleeping | |
| | `GET /is_sleeping` | Is Sleeping |
| | /metrics | |
| | `GET /metrics` | Metrics |
| | /nodes | |
| | `GET /nodes/status` | Node Status |
| | `GET /nodes/terminate_all` | Terminate Node All |
| | `POST /nodes/add` | Add Node |
| | `POST /nodes/remove` | Remove Node |
| | `POST /nodes/terminate` | Terminate Node |
| | /pooling | |
| | `POST /pooling` | Pooling |
| | /sleep | |
| | `POST /sleep` | Sleep |
| | /terminate | |
| | `GET /terminate` | Terminate |
| | /update_weights | |
| | `POST /update_weights` | Update Params |
| | /v1 | |
| | `GET /v1/models` | Available Models |
| | `POST /v1/chat/completions` | Chat Completions V1 |
| | `POST /v1/completions` | Completions V1 |
| | `POST /v1/embeddings` | Create Embeddings |
| | `POST /v1/encode` | Encode |
| | /wakeup | |
| | `POST /wakeup` | Wakeup |
