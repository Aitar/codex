# OpenAPI Endpoints — lmdeploy

Source: https://lmdeploy.readthedocs.io/en/latest/api/openapi.html

OpenAPI Endpoints

OpenAPI Endpoints#

OpenAI Compatible API Endpoints#

POST/abort_request#

Abort Request

Abort an ongoing request.

Request body:

```text
{
  "abort_all":{
    "default":false,
    "title":"Abort All",
    "type":"boolean"
  },
  "abort_message":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"Abort Message"
  },
  "finished_reason":{
    "anyOf":[
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "title":"Finished Reason"
  },
  "session_id":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":-1,
    "title":"Session Id"
  }
}
```

Example request:

```text
POST /abort_request HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "abort_all": true,
    "abort_message": "string",
    "finished_reason": {},
    "session_id": 1
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

GET/distserve/engine_info#

Engine Info

Example request:

```text
GET /distserve/engine_info HTTP/1.1
Host: example.com
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

POST/distserve/free_cache#

Free Cache

Request body:

```text
{
  "remote_engine_id":{
    "title":"Remote Engine Id",
    "type":"string"
  },
  "remote_session_id":{
    "title":"Remote Session Id",
    "type":"integer"
  }
}
```

Example request:

```text
POST /distserve/free_cache HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "remote_engine_id": "string",
    "remote_session_id": 1
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/distserve/p2p_connect#

P2P Connect

Request body:

```text
{
  "protocol":{
    "description":"Migration Transport Protocol.\n\nAttributes:\n    RDMA: IB or RoCEv1/v2.\n    NVLINK: High device-to-device link.\n\nWarning: By now, only `GPU Directed RDMA` is supported in DistServe.\n    We preserve several protocol and will be implemented in the future.",
    "enum":[
      1,
      2,
      3
    ],
    "title":"MigrationProtocol",
    "type":"integer"
  },
  "remote_engine_endpoint_info":{
    "properties":{
      "zmq_address":{
        "title":"Zmq Address",
        "type":"string"
      }
    },
    "required":[
      "zmq_address"
    ],
    "title":"DistServeEngineEndpointInfo",
    "type":"object"
  },
  "remote_engine_id":{
    "title":"Remote Engine Id",
    "type":"string"
  },
  "remote_kvtransfer_endpoint_info":{
    "items":{
      "properties":{
        "endpoint_info":{
          "title":"Endpoint Info",
          "type":"string"
        },
        "protocol":{
          "description":"Migration Transport Protocol.\n\nAttributes:\n    RDMA: IB or RoCEv1/v2.\n    NVLINK: High device-to-device link.\n\nWarning: By now, only `GPU Directed RDMA` is supported in DistServe.\n    We preserve several protocol and will be implemented in the future.",
          "enum":[
            1,
            2,
            3
          ],
          "title":"MigrationProtocol",
          "type":"integer"
        }
      },
      "required":[
        "protocol",
        "endpoint_info"
      ],
      "title":"DistServeKVTransferEndpointInfo",
      "type":"object"
    },
    "title":"Remote Kvtransfer Endpoint Info",
    "type":"array"
  }
}
```

Example request:

```text
POST /distserve/p2p_connect HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "protocol": 1,
    "remote_engine_endpoint_info": {
        "zmq_address": "string"
    },
    "remote_engine_id": "string",
    "remote_kvtransfer_endpoint_info": [
        {
            "endpoint_info": "string",
            "protocol": 1
        }
    ]
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/distserve/p2p_drop_connect#

P2P Drop Connect

Request body:

```text
{
  "engine_id":{
    "title":"Engine Id",
    "type":"string"
  },
  "remote_engine_id":{
    "title":"Remote Engine Id",
    "type":"string"
  }
}
```

Example request:

```text
POST /distserve/p2p_drop_connect HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "engine_id": "string",
    "remote_engine_id": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/distserve/p2p_initialize#

P2P Initialize

Request body:

```text
{
  "local_engine_config":{
    "description":"DistServe Engine Config.\n\nIn Disaggregated LLM Serving, we need to get engine info of each\nPD Peer for the following reason:\n    1. Cache: The stride of cache block for correct offset of KV Transfer.\n    2. Parallel: Prefill and decode use different parallel strategy to\n        achieve high SLO Attainment or high throughput. In this situation,\n        we need to caclculate which prefill-decode worker peers need to connect.\n        For example, prefill worker use pp4 and decode worker use tp2pp2,\n        the perfill-decode worker conn peer is (0, 0), (0, 1), (1, 0), (1, 1),\n        (2, 2), (2, 3), (3, 2), (3, 3). Instead, under the situation of\n        (tp4, tp4), perfill-decode worker conn peer is (0, 0), (1, 1), (2, 2),\n        (3, 3).",
    "properties":{
      "block_size":{
        "title":"Block Size",
        "type":"integer"
      },
      "dp_rank":{
        "title":"Dp Rank",
        "type":"integer"
      },
      "dp_size":{
        "title":"Dp Size",
        "type":"integer"
      },
      "ep_size":{
        "title":"Ep Size",
        "type":"integer"
      },
      "num_cpu_blocks":{
        "title":"Num Cpu Blocks",
        "type":"integer"
      },
      "num_gpu_blocks":{
        "title":"Num Gpu Blocks",
        "type":"integer"
      },
      "pp_size":{
        "anyOf":[
          {
            "type":"integer"
          },
          {
            "type":"null"
          }
        ],
        "title":"Pp Size"
      },
      "tp_size":{
        "title":"Tp Size",
        "type":"integer"
      }
    },
    "required":[
      "tp_size",
      "ep_size",
      "dp_size",
      "pp_size",
      "dp_rank",
      "block_size",
      "num_cpu_blocks",
      "num_gpu_blocks"
    ],
    "title":"DistServeEngineConfig",
    "type":"object"
  },
  "local_engine_id":{
    "title":"Local Engine Id",
    "type":"string"
  },
  "nvlink_config":{
    "anyOf":[
      {
        "description":"TODO: Add NVLink Protocol",
        "properties":{},
        "title":"DistServeNVLinkConfig",
        "type":"object"
      },
      {
        "type":"null"
      }
    ]
  },
  "protocol":{
    "description":"Migration Transport Protocol.\n\nAttributes:\n    RDMA: IB or RoCEv1/v2.\n    NVLINK: High device-to-device link.\n\nWarning: By now, only `GPU Directed RDMA` is supported in DistServe.\n    We preserve several protocol and will be implemented in the future.",
    "enum":[
      1,
      2,
      3
    ],
    "title":"MigrationProtocol",
    "type":"integer"
  },
  "rank":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Rank"
  },
  "rdma_config":{
    "anyOf":[
      {
        "description":"DistServe RDMA Config.\n\nArgs:\n    with_gdr: default to True.\n    link_type: default to `RDMALinkType.RoCE`.\n\nWarning: Only GDR is supported by now.\nWarning: Technically, both RoCE and IB are supported.\n    However, IB mode is not tested because of unavailable\n    testing envoriment.",
        "properties":{
          "link_type":{
            "description":"RDMA Link Type.",
            "enum":[
              1,
              2
            ],
            "title":"RDMALinkType",
            "type":"integer"
          },
          "with_gdr":{
            "default":true,
            "title":"With Gdr",
            "type":"boolean"
          }
        },
        "title":"DistServeRDMAConfig",
        "type":"object"
      },
      {
        "type":"null"
      }
    ]
  },
  "remote_engine_config":{
    "description":"DistServe Engine Config.\n\nIn Disaggregated LLM Serving, we need to get engine info of each\nPD Peer for the following reason:\n    1. Cache: The stride of cache block for correct offset of KV Transfer.\n    2. Parallel: Prefill and decode use different parallel strategy to\n        achieve high SLO Attainment or high throughput. In this situation,\n        we need to caclculate which prefill-decode worker peers need to connect.\n        For example, prefill worker use pp4 and decode worker use tp2pp2,\n        the perfill-decode worker conn peer is (0, 0), (0, 1), (1, 0), (1, 1),\n        (2, 2), (2, 3), (3, 2), (3, 3). Instead, under the situation of\n        (tp4, tp4), perfill-decode worker conn peer is (0, 0), (1, 1), (2, 2),\n        (3, 3).",
    "properties":{
      "block_size":{
        "title":"Block Size",
        "type":"integer"
      },
      "dp_rank":{
        "title":"Dp Rank",
        "type":"integer"
      },
      "dp_size":{
        "title":"Dp Size",
        "type":"integer"
      },
      "ep_size":{
        "title":"Ep Size",
        "type":"integer"
      },
      "num_cpu_blocks":{
        "title":"Num Cpu Blocks",
        "type":"integer"
      },
      "num_gpu_blocks":{
        "title":"Num Gpu Blocks",
        "type":"integer"
      },
      "pp_size":{
        "anyOf":[
          {
            "type":"integer"
          },
          {
            "type":"null"
          }
        ],
        "title":"Pp Size"
      },
      "tp_size":{
        "title":"Tp Size",
        "type":"integer"
      }
    },
    "required":[
      "tp_size",
      "ep_size",
      "dp_size",
      "pp_size",
      "dp_rank",
      "block_size",
      "num_cpu_blocks",
      "num_gpu_blocks"
    ],
    "title":"DistServeEngineConfig",
    "type":"object"
  },
  "remote_engine_id":{
    "title":"Remote Engine Id",
    "type":"string"
  },
  "tcp_config":{
    "anyOf":[
      {
        "description":"TODO: Add TCP Protocol",
        "properties":{},
        "title":"DistServeTCPConfig",
        "type":"object"
      },
      {
        "type":"null"
      }
    ]
  }
}
```

Example request:

```text
POST /distserve/p2p_initialize HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "local_engine_config": {
        "block_size": 1,
        "dp_rank": 1,
        "dp_size": 1,
        "ep_size": 1,
        "num_cpu_blocks": 1,
        "num_gpu_blocks": 1,
        "pp_size": 1,
        "tp_size": 1
    },
    "local_engine_id": "string",
    "protocol": 1,
    "rank": 1,
    "rdma_config": {
        "link_type": 1,
        "with_gdr": true
    },
    "remote_engine_config": {
        "block_size": 1,
        "dp_rank": 1,
        "dp_size": 1,
        "ep_size": 1,
        "num_cpu_blocks": 1,
        "num_gpu_blocks": 1,
        "pp_size": 1,
        "tp_size": 1
    },
    "remote_engine_id": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/generate#

Generate

Request body:

```text
{
  "ignore_eos":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Ignore Eos"
  },
  "image_data":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "items":{
          "anyOf":[
            {
              "type":"string"
            },
            {
              "additionalProperties":true,
              "type":"object"
            }
          ]
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "title":"Image Data"
  },
  "include_stop_str_in_output":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Include Stop Str In Output"
  },
  "input_ids":{
    "anyOf":[
      {
        "items":{
          "type":"integer"
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "title":"Input Ids"
  },
  "max_tokens":{
    "default":128,
    "title":"Max Tokens",
    "type":"integer"
  },
  "media_io_kwargs":{
    "anyOf":[
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "description":"Additional kwargs to pass to the media IO processing, keyed by modality.",
    "title":"Media Io Kwargs"
  },
  "min_p":{
    "default":0.0,
    "title":"Min P",
    "type":"number"
  },
  "mm_processor_kwargs":{
    "anyOf":[
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "description":"Additional kwargs to pass to the HF processor",
    "title":"Mm Processor Kwargs"
  },
  "prompt":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"Prompt"
  },
  "repetition_ngram_size":{
    "default":0,
    "title":"Repetition Ngram Size",
    "type":"integer"
  },
  "repetition_ngram_threshold":{
    "default":0,
    "title":"Repetition Ngram Threshold",
    "type":"integer"
  },
  "repetition_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":1.0,
    "title":"Repetition Penalty"
  },
  "return_logprob":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "title":"Return Logprob"
  },
  "return_routed_experts":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Return Routed Experts"
  },
  "session_id":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":-1,
    "title":"Session Id"
  },
  "skip_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Skip Special Tokens"
  },
  "spaces_between_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Spaces Between Special Tokens"
  },
  "stop":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "type":"string"
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "title":"Stop"
  },
  "stop_token_ids":{
    "anyOf":[
      {
        "items":{
          "type":"integer"
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "title":"Stop Token Ids"
  },
  "stream":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Stream"
  },
  "temperature":{
    "default":1.0,
    "title":"Temperature",
    "type":"number"
  },
  "top_k":{
    "default":0,
    "title":"Top K",
    "type":"integer"
  },
  "top_p":{
    "default":1.0,
    "title":"Top P",
    "type":"number"
  }
}
```

Example request:

```text
POST /generate HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "ignore_eos": true,
    "image_data": "string",
    "include_stop_str_in_output": true,
    "input_ids": [
        1
    ],
    "max_tokens": 1,
    "media_io_kwargs": {},
    "min_p": 1.0,
    "mm_processor_kwargs": {},
    "prompt": "string",
    "repetition_ngram_size": 1,
    "repetition_ngram_threshold": 1,
    "repetition_penalty": 1.0,
    "return_logprob": true,
    "return_routed_experts": true,
    "session_id": 1,
    "skip_special_tokens": true,
    "spaces_between_special_tokens": true,
    "stop": "string",
    "stop_token_ids": [
        1
    ],
    "stream": true,
    "temperature": 1.0,
    "top_k": 1,
    "top_p": 1.0
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

GET/health#

Health

Health check.

Example request:

```text
GET /health HTTP/1.1
Host: example.com
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

GET/is_sleeping#

Is Sleeping

Example request:

```text
GET /is_sleeping HTTP/1.1
Host: example.com
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

GET/metrics#

Metrics

[Optional] Prometheus metrics endpoint.

Example request:

```text
GET /metrics HTTP/1.1
Host: example.com
```

Status Codes:

200 OK – Prometheus metrics data

404 Not Found – Metrics Endpoint not enabled

POST/pooling#

Pooling

Pooling prompts for reward model.

In vLLM documentation, https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#pooling-api_1,
the input format of Pooling API is the same as Embeddings API.

Go to https://platform.openai.com/docs/api-reference/embeddings/create
for the Embeddings API specification.

The request should be a JSON object with the following fields:

model (str): model name. Available from /v1/models.

input (list[int] | list[list[int]] | str | list[str]): input text to be embed

Request body:

```text
{
  "dimensions":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Dimensions"
  },
  "encoding_format":{
    "default":"float",
    "enum":[
      "float",
      "base64"
    ],
    "title":"Encoding Format",
    "type":"string"
  },
  "input":{
    "anyOf":[
      {
        "items":{
          "type":"integer"
        },
        "type":"array"
      },
      {
        "items":{
          "items":{
            "type":"integer"
          },
          "type":"array"
        },
        "type":"array"
      },
      {
        "type":"string"
      },
      {
        "items":{
          "type":"string"
        },
        "type":"array"
      }
    ],
    "title":"Input"
  },
  "model":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"Model"
  },
  "user":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"User"
  }
}
```

Example request:

```text
POST /pooling HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "dimensions": 1,
    "encoding_format": "float",
    "input": [
        1
    ],
    "model": "string",
    "user": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/sleep#

Sleep

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

GET/terminate#

Terminate

Terminate server.

Example request:

```text
GET /terminate HTTP/1.1
Host: example.com
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

POST/update_weights#

Update Params

Update weights for the model.

Request body:

```text
{
  "finished":{
    "default":false,
    "title":"Finished",
    "type":"boolean"
  },
  "load_format":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"Load Format"
  },
  "serialized_named_tensors":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "type":"string"
        },
        "type":"array"
      },
      {
        "additionalProperties":true,
        "type":"object"
      }
    ],
    "title":"Serialized Named Tensors"
  }
}
```

Example request:

```text
POST /update_weights HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "finished": true,
    "load_format": "string",
    "serialized_named_tensors": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/v1/chat/completions#

Chat Completions V1

Completion API similar to OpenAI’s API.

Refer to https://platform.openai.com/docs/api-reference/chat/create
for the API specification.

The request should be a JSON object with the following fields:

model: model name. Available from /v1/models.

messages: string prompt or chat history in OpenAI format. Chat history example:
`[{"role":"user","content":"hi"}]`.

temperature (float): to modulate the next token probability

top_p (float): If set to float < 1, only the smallest set of most
probable tokens with probabilities that add up to top_p or higher
are kept for generation.

n (int): How many chat completion choices to generate for each input
message. Only support one here.

stream: whether to stream the results or not. Default to false.

stream_options: Options for streaming response. Only set this when you
set stream: true.

max_completion_tokens (int | None): output token nums. Default to None.

max_tokens (int | None): output token nums. Default to None.
Deprecated: Use max_completion_tokens instead.

repetition_penalty (float): The parameter for repetition penalty.
1.0 means no penalty

stop (str | list[str] | None): To stop generating further
tokens. Only accept stop words that’s encoded to one token idex.

response_format (dict | None): To generate response according to given
schema. Examples:

```text
{
  "type": "json_schema",
  "json_schema":{
    "name": "test",
    "schema":{
      "properties":{
        "name":{"type":"string"}
      },
      "required":["name"],
      "type":"object"
    }
  }
}
```

or `{"type":"regex_schema","regex_schema":"callme[A-Za-z]{1,10}"}`

logit_bias (dict): Bias to logits. Only supported in pytorch engine.

tools (list): A list of tools the model may call. Currently, only
internlm2 functions are supported as a tool. Use this to specify a
list of functions for which the model can generate JSON inputs.

tool_choice (str | object): Controls which (if any) tool is called by
the model. none means the model will not call any tool and instead
generates a message. Specifying a particular tool via
`{"type":"function","function":{"name":"my_function"}}`
forces the model to call that tool. auto or required will put all
the tools informationto the model.

Additional arguments supported by LMDeploy:

top_k (int): The number of the highest probability vocabulary
tokens to keep for top-k-filtering

ignore_eos (bool): indicator for ignoring eos

skip_special_tokens (bool): Whether or not to remove special tokens
in the decoding. Default to be True.

spaces_between_special_tokens (bool): Whether or not to add spaces
around special tokens. The behavior of Fast tokenizers is to have
this to False. This is setup to True in slow tokenizers.

min_new_tokens (int): To generate at least numbers of tokens.

min_p (float): Minimum token probability, which will be scaled by the
probability of the most likely token. It must be a value between
0 and 1. Typical values are in the 0.01-0.2 range, comparably
selective as setting top_p in the 0.99-0.8 range (use the
opposite of normal top_p values)

Currently we do not support the following features:

presence_penalty (replaced with repetition_penalty)

frequency_penalty (replaced with repetition_penalty)

Request body:

```text
{
  "chat_template_kwargs":{
    "anyOf":[
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "description":"Additional keyword args to pass to the template renderer. Will be accessible by the chat template.",
    "title":"Chat Template Kwargs"
  },
  "do_preprocess":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Do Preprocess"
  },
  "enable_thinking":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "title":"Enable Thinking"
  },
  "frequency_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.0,
    "title":"Frequency Penalty"
  },
  "ignore_eos":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Ignore Eos"
  },
  "include_stop_str_in_output":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Include Stop Str In Output"
  },
  "logit_bias":{
    "anyOf":[
      {
        "additionalProperties":{
          "type":"number"
        },
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Logit Bias"
  },
  "logprobs":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Logprobs"
  },
  "max_completion_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "description":"An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens",
    "examples":[
      null
    ],
    "title":"Max Completion Tokens"
  },
  "max_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "deprecated":true,
    "examples":[
      null
    ],
    "title":"Max Tokens"
  },
  "media_io_kwargs":{
    "anyOf":[
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "description":"Additional kwargs to pass to the media IO processing, keyed by modality.",
    "title":"Media Io Kwargs"
  },
  "messages":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "additionalProperties":true,
          "type":"object"
        },
        "type":"array"
      }
    ],
    "examples":[
      [
        {
          "content":"hi",
          "role":"user"
        }
      ]
    ],
    "title":"Messages"
  },
  "min_new_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Min New Tokens"
  },
  "min_p":{
    "default":0.0,
    "title":"Min P",
    "type":"number"
  },
  "mm_processor_kwargs":{
    "anyOf":[
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "description":"Additional kwargs to pass to the HF processor",
    "title":"Mm Processor Kwargs"
  },
  "model":{
    "title":"Model",
    "type":"string"
  },
  "n":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":1,
    "title":"N"
  },
  "presence_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.0,
    "title":"Presence Penalty"
  },
  "reasoning_effort":{
    "anyOf":[
      {
        "enum":[
          "low",
          "medium",
          "high"
        ],
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"Reasoning Effort"
  },
  "repetition_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":1.0,
    "title":"Repetition Penalty"
  },
  "response_format":{
    "anyOf":[
      {
        "properties":{
          "json_schema":{
            "anyOf":[
              {
                "properties":{
                  "description":{
                    "anyOf":[
                      {
                        "type":"string"
                      },
                      {
                        "type":"null"
                      }
                    ],
                    "title":"Description"
                  },
                  "name":{
                    "title":"Name",
                    "type":"string"
                  },
                  "schema":{
                    "anyOf":[
                      {
                        "additionalProperties":true,
                        "type":"object"
                      },
                      {
                        "type":"null"
                      }
                    ],
                    "examples":[
                      null
                    ],
                    "title":"Schema"
                  },
                  "strict":{
                    "anyOf":[
                      {
                        "type":"boolean"
                      },
                      {
                        "type":"null"
                      }
                    ],
                    "default":false,
                    "title":"Strict"
                  }
                },
                "required":[
                  "name"
                ],
                "title":"JsonSchema",
                "type":"object"
              },
              {
                "type":"null"
              }
            ]
          },
          "regex_schema":{
            "anyOf":[
              {
                "type":"string"
              },
              {
                "type":"null"
              }
            ],
            "title":"Regex Schema"
          },
          "type":{
            "enum":[
              "text",
              "json_object",
              "json_schema",
              "regex_schema"
            ],
            "title":"Type",
            "type":"string"
          }
        },
        "required":[
          "type"
        ],
        "title":"ResponseFormat",
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ]
  },
  "return_token_ids":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Return Token Ids"
  },
  "seed":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Seed"
  },
  "session_id":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":-1,
    "title":"Session Id"
  },
  "skip_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Skip Special Tokens"
  },
  "spaces_between_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Spaces Between Special Tokens"
  },
  "stop":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "type":"string"
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Stop"
  },
  "stream":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Stream"
  },
  "stream_options":{
    "anyOf":[
      {
        "description":"The stream options.",
        "properties":{
          "include_usage":{
            "anyOf":[
              {
                "type":"boolean"
              },
              {
                "type":"null"
              }
            ],
            "default":false,
            "title":"Include Usage"
          }
        },
        "title":"StreamOptions",
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ]
  },
  "temperature":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.7,
    "title":"Temperature"
  },
  "tool_choice":{
    "anyOf":[
      {
        "description":"The tool choice definition.",
        "properties":{
          "function":{
            "description":"The name of tool choice function.",
            "properties":{
              "name":{
                "title":"Name",
                "type":"string"
              }
            },
            "required":[
              "name"
            ],
            "title":"ToolChoiceFuncName",
            "type":"object"
          },
          "type":{
            "const":"function",
            "default":"function",
            "examples":[
              "function"
            ],
            "title":"Type",
            "type":"string"
          }
        },
        "required":[
          "function"
        ],
        "title":"ToolChoice",
        "type":"object"
      },
      {
        "enum":[
          "auto",
          "required",
          "none"
        ],
        "type":"string"
      }
    ],
    "default":"auto",
    "examples":[
      "none"
    ],
    "title":"Tool Choice"
  },
  "tools":{
    "anyOf":[
      {
        "items":{
          "description":"Function wrapper.",
          "properties":{
            "function":{
              "description":"Function descriptions.",
              "properties":{
                "description":{
                  "anyOf":[
                    {
                      "type":"string"
                    },
                    {
                      "type":"null"
                    }
                  ],
                  "examples":[
                    null
                  ],
                  "title":"Description"
                },
                "name":{
                  "title":"Name",
                  "type":"string"
                },
                "parameters":{
                  "anyOf":[
                    {
                      "additionalProperties":true,
                      "type":"object"
                    },
                    {
                      "type":"null"
                    }
                  ],
                  "title":"Parameters"
                }
              },
              "required":[
                "name"
              ],
              "title":"Function",
              "type":"object"
            },
            "type":{
              "default":"function",
              "examples":[
                "function"
              ],
              "title":"Type",
              "type":"string"
            }
          },
          "required":[
            "function"
          ],
          "title":"Tool",
          "type":"object"
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Tools"
  },
  "top_k":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":40,
    "title":"Top K"
  },
  "top_logprobs":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Top Logprobs"
  },
  "top_p":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":1.0,
    "title":"Top P"
  },
  "user":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"User"
  }
}
```

Example request:

```text
POST /v1/chat/completions HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "chat_template_kwargs": {},
    "do_preprocess": true,
    "enable_thinking": true,
    "frequency_penalty": 1.0,
    "ignore_eos": true,
    "include_stop_str_in_output": true,
    "logit_bias": {},
    "logprobs": true,
    "max_completion_tokens": 1,
    "max_tokens": 1,
    "media_io_kwargs": {},
    "messages": "string",
    "min_new_tokens": 1,
    "min_p": 1.0,
    "mm_processor_kwargs": {},
    "model": "string",
    "n": 1,
    "presence_penalty": 1.0,
    "reasoning_effort": "low",
    "repetition_penalty": 1.0,
    "response_format": {
        "json_schema": {
            "description": "string",
            "name": "string",
            "schema": {},
            "strict": true
        },
        "regex_schema": "string",
        "type": "text"
    },
    "return_token_ids": true,
    "seed": 1,
    "session_id": 1,
    "skip_special_tokens": true,
    "spaces_between_special_tokens": true,
    "stop": "string",
    "stream": true,
    "stream_options": {
        "include_usage": true
    },
    "temperature": 1.0,
    "tool_choice": {
        "function": {
            "name": "string"
        },
        "type": "string"
    },
    "tools": [
        {
            "function": {
                "description": "string",
                "name": "string",
                "parameters": {}
            },
            "type": "string"
        }
    ],
    "top_k": 1,
    "top_logprobs": 1,
    "top_p": 1.0,
    "user": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/v1/completions#

Completions V1

Completion API similar to OpenAI’s API.

Go to https://platform.openai.com/docs/api-reference/completions/create
for the API specification.

The request should be a JSON object with the following fields:

model (str): model name. Available from /v1/models.

prompt (str): the input prompt.

suffix (str): The suffix that comes after a completion of inserted text.

max_completion_tokens (int | None): output token nums. Default to None.

max_tokens (int | None): output token nums. Default to 16.
Deprecated: Use max_completion_tokens instead.

temperature (float): to modulate the next token probability

top_p (float): If set to float < 1, only the smallest set of most
probable tokens with probabilities that add up to top_p or higher
are kept for generation.

n (int): How many chat completion choices to generate for each input
message. Only support one here.

stream: whether to stream the results or not. Default to false.

stream_options: Options for streaming response. Only set this when you
set stream: true.

repetition_penalty (float): The parameter for repetition penalty.
1.0 means no penalty

user (str): A unique identifier representing your end-user.

stop (str | list[str] | None): To stop generating further
tokens. Only accept stop words that’s encoded to one token idex.

Additional arguments supported by LMDeploy:

ignore_eos (bool): indicator for ignoring eos

skip_special_tokens (bool): Whether or not to remove special tokens
in the decoding. Default to be True.

spaces_between_special_tokens (bool): Whether or not to add spaces
around special tokens. The behavior of Fast tokenizers is to have
this to False. This is setup to True in slow tokenizers.

top_k (int): The number of the highest probability vocabulary
tokens to keep for top-k-filtering

min_p (float): Minimum token probability, which will be scaled by the
probability of the most likely token. It must be a value between
0 and 1. Typical values are in the 0.01-0.2 range, comparably
selective as setting top_p in the 0.99-0.8 range (use the
opposite of normal top_p values)

Currently we do not support the following features:

logprobs (not supported yet)

presence_penalty (replaced with repetition_penalty)

frequency_penalty (replaced with repetition_penalty)

Request body:

```text
{
  "echo":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Echo"
  },
  "frequency_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.0,
    "title":"Frequency Penalty"
  },
  "ignore_eos":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Ignore Eos"
  },
  "logprobs":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Logprobs"
  },
  "max_completion_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "description":"An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens",
    "examples":[
      null
    ],
    "title":"Max Completion Tokens"
  },
  "max_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":16,
    "deprecated":true,
    "examples":[
      16
    ],
    "title":"Max Tokens"
  },
  "min_p":{
    "default":0.0,
    "title":"Min P",
    "type":"number"
  },
  "model":{
    "title":"Model",
    "type":"string"
  },
  "n":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":1,
    "title":"N"
  },
  "presence_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.0,
    "title":"Presence Penalty"
  },
  "prompt":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{},
        "type":"array"
      }
    ],
    "title":"Prompt"
  },
  "repetition_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":1.0,
    "title":"Repetition Penalty"
  },
  "return_token_ids":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Return Token Ids"
  },
  "seed":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Seed"
  },
  "session_id":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":-1,
    "title":"Session Id"
  },
  "skip_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Skip Special Tokens"
  },
  "spaces_between_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Spaces Between Special Tokens"
  },
  "stop":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "type":"string"
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Stop"
  },
  "stream":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Stream"
  },
  "stream_options":{
    "anyOf":[
      {
        "description":"The stream options.",
        "properties":{
          "include_usage":{
            "anyOf":[
              {
                "type":"boolean"
              },
              {
                "type":"null"
              }
            ],
            "default":false,
            "title":"Include Usage"
          }
        },
        "title":"StreamOptions",
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ]
  },
  "suffix":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"Suffix"
  },
  "temperature":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.7,
    "title":"Temperature"
  },
  "top_k":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":40,
    "title":"Top K"
  },
  "top_p":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":1.0,
    "title":"Top P"
  },
  "user":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"User"
  }
}
```

Example request:

```text
POST /v1/completions HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "echo": true,
    "frequency_penalty": 1.0,
    "ignore_eos": true,
    "logprobs": 1,
    "max_completion_tokens": 1,
    "max_tokens": 1,
    "min_p": 1.0,
    "model": "string",
    "n": 1,
    "presence_penalty": 1.0,
    "prompt": "string",
    "repetition_penalty": 1.0,
    "return_token_ids": true,
    "seed": 1,
    "session_id": 1,
    "skip_special_tokens": true,
    "spaces_between_special_tokens": true,
    "stop": "string",
    "stream": true,
    "stream_options": {
        "include_usage": true
    },
    "suffix": "string",
    "temperature": 1.0,
    "top_k": 1,
    "top_p": 1.0,
    "user": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/v1/embeddings#

Create Embeddings

Creates embeddings for the text.

Request body:

```text
{
  "input":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "type":"string"
        },
        "type":"array"
      }
    ],
    "title":"Input"
  },
  "model":{
    "title":"Model",
    "type":"string"
  },
  "user":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"User"
  }
}
```

Example request:

```text
POST /v1/embeddings HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "input": "string",
    "model": "string",
    "user": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/v1/encode#

Encode

Encode prompts.

The request should be a JSON object with the following fields:

input: the prompt to be encoded. In str or list[str] format.

do_preprocess: whether do preprocess or not. Default to False.

add_bos: True when it is the beginning of a conversation. False when it
is not. Default to True.

Request body:

```text
{
  "add_bos":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Add Bos"
  },
  "do_preprocess":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Do Preprocess"
  },
  "input":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "type":"string"
        },
        "type":"array"
      }
    ],
    "title":"Input"
  }
}
```

Example request:

```text
POST /v1/encode HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "add_bos": true,
    "do_preprocess": true,
    "input": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

GET/v1/models#

Available Models

Show available models.

Example request:

```text
GET /v1/models HTTP/1.1
Host: example.com
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

POST/wakeup#

Wakeup

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

Proxy Server API#

POST/distserve/connection_warmup#

Connection Warmup

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

POST/distserve/gc#

Cache Block Gc To Be Migrated

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

POST/nodes/add#

Add Node

Add a node to the manager.

url (str): A http url. Can be the url generated by
lmdeploy serve api_server.

status (dict): The description of the node. An example:
`{models:['internlm-chat-7b],speed:1}`. The speed here can be
RPM or other metric. All the values of nodes should be the same metric.

Request body:

```text
{
  "status":{
    "anyOf":[
      {
        "description":"Status protocol consists of models' information.",
        "properties":{
          "latency":{
            "default":[],
            "examples":[
              []
            ],
            "items":{},
            "title":"Latency",
            "type":"array"
          },
          "models":{
            "default":[],
            "examples":[
              []
            ],
            "items":{
              "type":"string"
            },
            "title":"Models",
            "type":"array"
          },
          "role":{
            "description":"Role of Engine.\n\nNote: In the implementation of LMDeploy-Distserve, all engine is hybrid\n    engine technically, the role of engine is up to what kind of request is\n    sent to the engine. However, taking implementation into the consideration,\n    the role is still need to be identified when starting the engine server\n    for the following reasons:\n        1. Make sure the engine can be correctly discovered by the proxy.\n        2. The create of ModelInputs is different among hybrid, prefill and\n            decode engines in DP Engine (DSV3 DP + EP).",
            "enum":[
              1,
              2,
              3
            ],
            "title":"EngineRole",
            "type":"integer"
          },
          "speed":{
            "anyOf":[
              {
                "type":"integer"
              },
              {
                "type":"null"
              }
            ],
            "examples":[
              null
            ],
            "title":"Speed"
          },
          "unfinished":{
            "default":0,
            "title":"Unfinished",
            "type":"integer"
          }
        },
        "title":"Status",
        "type":"object"
      },
      {
        "type":"null"
      }
    ]
  },
  "url":{
    "title":"Url",
    "type":"string"
  }
}
```

Example request:

```text
POST /nodes/add HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "status": {
        "latency": [
            {}
        ],
        "models": [
            "string"
        ],
        "role": 1,
        "speed": 1,
        "unfinished": 1
    },
    "url": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/nodes/remove#

Remove Node

Show available models.

Request body:

```text
{
  "status":{
    "anyOf":[
      {
        "description":"Status protocol consists of models' information.",
        "properties":{
          "latency":{
            "default":[],
            "examples":[
              []
            ],
            "items":{},
            "title":"Latency",
            "type":"array"
          },
          "models":{
            "default":[],
            "examples":[
              []
            ],
            "items":{
              "type":"string"
            },
            "title":"Models",
            "type":"array"
          },
          "role":{
            "description":"Role of Engine.\n\nNote: In the implementation of LMDeploy-Distserve, all engine is hybrid\n    engine technically, the role of engine is up to what kind of request is\n    sent to the engine. However, taking implementation into the consideration,\n    the role is still need to be identified when starting the engine server\n    for the following reasons:\n        1. Make sure the engine can be correctly discovered by the proxy.\n        2. The create of ModelInputs is different among hybrid, prefill and\n            decode engines in DP Engine (DSV3 DP + EP).",
            "enum":[
              1,
              2,
              3
            ],
            "title":"EngineRole",
            "type":"integer"
          },
          "speed":{
            "anyOf":[
              {
                "type":"integer"
              },
              {
                "type":"null"
              }
            ],
            "examples":[
              null
            ],
            "title":"Speed"
          },
          "unfinished":{
            "default":0,
            "title":"Unfinished",
            "type":"integer"
          }
        },
        "title":"Status",
        "type":"object"
      },
      {
        "type":"null"
      }
    ]
  },
  "url":{
    "title":"Url",
    "type":"string"
  }
}
```

Example request:

```text
POST /nodes/remove HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "status": {
        "latency": [
            {}
        ],
        "models": [
            "string"
        ],
        "role": 1,
        "speed": 1,
        "unfinished": 1
    },
    "url": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

GET/nodes/status#

Node Status

Show nodes status.

Example request:

```text
GET /nodes/status HTTP/1.1
Host: example.com
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

POST/nodes/terminate#

Terminate Node

Terminate nodes.

Request body:

```text
{
  "status":{
    "anyOf":[
      {
        "description":"Status protocol consists of models' information.",
        "properties":{
          "latency":{
            "default":[],
            "examples":[
              []
            ],
            "items":{},
            "title":"Latency",
            "type":"array"
          },
          "models":{
            "default":[],
            "examples":[
              []
            ],
            "items":{
              "type":"string"
            },
            "title":"Models",
            "type":"array"
          },
          "role":{
            "description":"Role of Engine.\n\nNote: In the implementation of LMDeploy-Distserve, all engine is hybrid\n    engine technically, the role of engine is up to what kind of request is\n    sent to the engine. However, taking implementation into the consideration,\n    the role is still need to be identified when starting the engine server\n    for the following reasons:\n        1. Make sure the engine can be correctly discovered by the proxy.\n        2. The create of ModelInputs is different among hybrid, prefill and\n            decode engines in DP Engine (DSV3 DP + EP).",
            "enum":[
              1,
              2,
              3
            ],
            "title":"EngineRole",
            "type":"integer"
          },
          "speed":{
            "anyOf":[
              {
                "type":"integer"
              },
              {
                "type":"null"
              }
            ],
            "examples":[
              null
            ],
            "title":"Speed"
          },
          "unfinished":{
            "default":0,
            "title":"Unfinished",
            "type":"integer"
          }
        },
        "title":"Status",
        "type":"object"
      },
      {
        "type":"null"
      }
    ]
  },
  "url":{
    "title":"Url",
    "type":"string"
  }
}
```

Example request:

```text
POST /nodes/terminate HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "status": {
        "latency": [
            {}
        ],
        "models": [
            "string"
        ],
        "role": 1,
        "speed": 1,
        "unfinished": 1
    },
    "url": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

GET/nodes/terminate_all#

Terminate Node All

Terminate nodes.

Example request:

```text
GET /nodes/terminate_all HTTP/1.1
Host: example.com
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

POST/v1/chat/completions#

Chat Completions V1

Completion API similar to OpenAI’s API.

Refer to https://platform.openai.com/docs/api-reference/chat/create
for the API specification.

The request should be a JSON object with the following fields:

model: model name. Available from /v1/models.

messages: string prompt or chat history in OpenAI format. Chat history
example: [{“role”: “user”, “content”: “hi”}].

temperature (float): to modulate the next token probability

top_p (float): If set to float < 1, only the smallest set of most
probable tokens with probabilities that add up to top_p or higher
are kept for generation.

n (int): How many chat completion choices to generate for each input
message. Only support one here.

stream: whether to stream the results or not. Default to false.

max_completion_tokens (int | None): output token nums. Default to None.

max_tokens (int | None): output token nums. Default to None.
Deprecated: Use max_completion_tokens instead.

repetition_penalty (float): The parameter for repetition penalty.
1.0 means no penalty

stop (str | list[str] | None): To stop generating further
tokens. Only accept stop words that’s encoded to one token idex.

response_format (dict | None): To generate response according to given
schema. Examples:

```text
{
  "type": "json_schema",
  "json_schema":{
    "name": "test",
    "schema":{
      "properties":{
        "name":{"type":"string"}
      },
      "required":["name"],
      "type":"object"
    }
  }
}
```

or
`{"type":"regex_schema","regex_schema":"callme[A-Za-z]{1,10}"}`

logit_bias (dict): Bias to logits. Only supported in pytorch engine.

tools (list): A list of tools the model may call. Currently, only
internlm2 functions are supported as a tool. Use this to specify a
list of functions for which the model can generate JSON inputs.

tool_choice (str | object): Controls which (if any) tool is called by
the model. none means the model will not call any tool and instead
generates a message. Specifying a particular tool via
`{"type":"function","function":{"name":"my_function"}}`
forces the model to call that tool. auto or required will put all
the tools information to the model.

Additional arguments supported by LMDeploy:

top_k (int): The number of the highest probability vocabulary
tokens to keep for top-k-filtering

ignore_eos (bool): indicator for ignoring eos

skip_special_tokens (bool): Whether or not to remove special tokens
in the decoding. Default to be True.

min_new_tokens (int): To generate at least numbers of tokens.

min_p (float): Minimum token probability, which will be scaled by the
probability of the most likely token. It must be a value between
0 and 1. Typical values are in the 0.01-0.2 range, comparably
selective as setting top_p in the 0.99-0.8 range (use the
opposite of normal top_p values)

Currently we do not support the following features:

presence_penalty (replaced with repetition_penalty)

frequency_penalty (replaced with repetition_penalty)

Request body:

```text
{
  "chat_template_kwargs":{
    "anyOf":[
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "description":"Additional keyword args to pass to the template renderer. Will be accessible by the chat template.",
    "title":"Chat Template Kwargs"
  },
  "do_preprocess":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Do Preprocess"
  },
  "enable_thinking":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "title":"Enable Thinking"
  },
  "frequency_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.0,
    "title":"Frequency Penalty"
  },
  "ignore_eos":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Ignore Eos"
  },
  "include_stop_str_in_output":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Include Stop Str In Output"
  },
  "logit_bias":{
    "anyOf":[
      {
        "additionalProperties":{
          "type":"number"
        },
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Logit Bias"
  },
  "logprobs":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Logprobs"
  },
  "max_completion_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "description":"An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens",
    "examples":[
      null
    ],
    "title":"Max Completion Tokens"
  },
  "max_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "deprecated":true,
    "examples":[
      null
    ],
    "title":"Max Tokens"
  },
  "media_io_kwargs":{
    "anyOf":[
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "description":"Additional kwargs to pass to the media IO processing, keyed by modality.",
    "title":"Media Io Kwargs"
  },
  "messages":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "additionalProperties":true,
          "type":"object"
        },
        "type":"array"
      }
    ],
    "examples":[
      [
        {
          "content":"hi",
          "role":"user"
        }
      ]
    ],
    "title":"Messages"
  },
  "min_new_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Min New Tokens"
  },
  "min_p":{
    "default":0.0,
    "title":"Min P",
    "type":"number"
  },
  "mm_processor_kwargs":{
    "anyOf":[
      {
        "additionalProperties":true,
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "description":"Additional kwargs to pass to the HF processor",
    "title":"Mm Processor Kwargs"
  },
  "model":{
    "title":"Model",
    "type":"string"
  },
  "n":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":1,
    "title":"N"
  },
  "presence_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.0,
    "title":"Presence Penalty"
  },
  "reasoning_effort":{
    "anyOf":[
      {
        "enum":[
          "low",
          "medium",
          "high"
        ],
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"Reasoning Effort"
  },
  "repetition_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":1.0,
    "title":"Repetition Penalty"
  },
  "response_format":{
    "anyOf":[
      {
        "properties":{
          "json_schema":{
            "anyOf":[
              {
                "properties":{
                  "description":{
                    "anyOf":[
                      {
                        "type":"string"
                      },
                      {
                        "type":"null"
                      }
                    ],
                    "title":"Description"
                  },
                  "name":{
                    "title":"Name",
                    "type":"string"
                  },
                  "schema":{
                    "anyOf":[
                      {
                        "additionalProperties":true,
                        "type":"object"
                      },
                      {
                        "type":"null"
                      }
                    ],
                    "examples":[
                      null
                    ],
                    "title":"Schema"
                  },
                  "strict":{
                    "anyOf":[
                      {
                        "type":"boolean"
                      },
                      {
                        "type":"null"
                      }
                    ],
                    "default":false,
                    "title":"Strict"
                  }
                },
                "required":[
                  "name"
                ],
                "title":"JsonSchema",
                "type":"object"
              },
              {
                "type":"null"
              }
            ]
          },
          "regex_schema":{
            "anyOf":[
              {
                "type":"string"
              },
              {
                "type":"null"
              }
            ],
            "title":"Regex Schema"
          },
          "type":{
            "enum":[
              "text",
              "json_object",
              "json_schema",
              "regex_schema"
            ],
            "title":"Type",
            "type":"string"
          }
        },
        "required":[
          "type"
        ],
        "title":"ResponseFormat",
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ]
  },
  "return_token_ids":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Return Token Ids"
  },
  "seed":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Seed"
  },
  "session_id":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":-1,
    "title":"Session Id"
  },
  "skip_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Skip Special Tokens"
  },
  "spaces_between_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Spaces Between Special Tokens"
  },
  "stop":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "type":"string"
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Stop"
  },
  "stream":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Stream"
  },
  "stream_options":{
    "anyOf":[
      {
        "description":"The stream options.",
        "properties":{
          "include_usage":{
            "anyOf":[
              {
                "type":"boolean"
              },
              {
                "type":"null"
              }
            ],
            "default":false,
            "title":"Include Usage"
          }
        },
        "title":"StreamOptions",
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ]
  },
  "temperature":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.7,
    "title":"Temperature"
  },
  "tool_choice":{
    "anyOf":[
      {
        "description":"The tool choice definition.",
        "properties":{
          "function":{
            "description":"The name of tool choice function.",
            "properties":{
              "name":{
                "title":"Name",
                "type":"string"
              }
            },
            "required":[
              "name"
            ],
            "title":"ToolChoiceFuncName",
            "type":"object"
          },
          "type":{
            "const":"function",
            "default":"function",
            "examples":[
              "function"
            ],
            "title":"Type",
            "type":"string"
          }
        },
        "required":[
          "function"
        ],
        "title":"ToolChoice",
        "type":"object"
      },
      {
        "enum":[
          "auto",
          "required",
          "none"
        ],
        "type":"string"
      }
    ],
    "default":"auto",
    "examples":[
      "none"
    ],
    "title":"Tool Choice"
  },
  "tools":{
    "anyOf":[
      {
        "items":{
          "description":"Function wrapper.",
          "properties":{
            "function":{
              "description":"Function descriptions.",
              "properties":{
                "description":{
                  "anyOf":[
                    {
                      "type":"string"
                    },
                    {
                      "type":"null"
                    }
                  ],
                  "examples":[
                    null
                  ],
                  "title":"Description"
                },
                "name":{
                  "title":"Name",
                  "type":"string"
                },
                "parameters":{
                  "anyOf":[
                    {
                      "additionalProperties":true,
                      "type":"object"
                    },
                    {
                      "type":"null"
                    }
                  ],
                  "title":"Parameters"
                }
              },
              "required":[
                "name"
              ],
              "title":"Function",
              "type":"object"
            },
            "type":{
              "default":"function",
              "examples":[
                "function"
              ],
              "title":"Type",
              "type":"string"
            }
          },
          "required":[
            "function"
          ],
          "title":"Tool",
          "type":"object"
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Tools"
  },
  "top_k":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":40,
    "title":"Top K"
  },
  "top_logprobs":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Top Logprobs"
  },
  "top_p":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":1.0,
    "title":"Top P"
  },
  "user":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"User"
  }
}
```

Example request:

```text
POST /v1/chat/completions HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "chat_template_kwargs": {},
    "do_preprocess": true,
    "enable_thinking": true,
    "frequency_penalty": 1.0,
    "ignore_eos": true,
    "include_stop_str_in_output": true,
    "logit_bias": {},
    "logprobs": true,
    "max_completion_tokens": 1,
    "max_tokens": 1,
    "media_io_kwargs": {},
    "messages": "string",
    "min_new_tokens": 1,
    "min_p": 1.0,
    "mm_processor_kwargs": {},
    "model": "string",
    "n": 1,
    "presence_penalty": 1.0,
    "reasoning_effort": "low",
    "repetition_penalty": 1.0,
    "response_format": {
        "json_schema": {
            "description": "string",
            "name": "string",
            "schema": {},
            "strict": true
        },
        "regex_schema": "string",
        "type": "text"
    },
    "return_token_ids": true,
    "seed": 1,
    "session_id": 1,
    "skip_special_tokens": true,
    "spaces_between_special_tokens": true,
    "stop": "string",
    "stream": true,
    "stream_options": {
        "include_usage": true
    },
    "temperature": 1.0,
    "tool_choice": {
        "function": {
            "name": "string"
        },
        "type": "string"
    },
    "tools": [
        {
            "function": {
                "description": "string",
                "name": "string",
                "parameters": {}
            },
            "type": "string"
        }
    ],
    "top_k": 1,
    "top_logprobs": 1,
    "top_p": 1.0,
    "user": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

POST/v1/completions#

Completions V1

Completion API similar to OpenAI’s API.

Go to https://platform.openai.com/docs/api-reference/completions/create
for the API specification.

The request should be a JSON object with the following fields:

model (str): model name. Available from /v1/models.

prompt (str): the input prompt.

suffix (str): The suffix that comes after a completion of inserted text.

max_completion_tokens (int | None): output token nums. Default to None.

max_tokens (int): output token nums. Default to 16.
Deprecated: Use max_completion_tokens instead.

temperature (float): to modulate the next token probability

top_p (float): If set to float < 1, only the smallest set of most
probable tokens with probabilities that add up to top_p or higher
are kept for generation.

n (int): How many chat completion choices to generate for each input
message. Only support one here.

stream: whether to stream the results or not. Default to false.

repetition_penalty (float): The parameter for repetition penalty.
1.0 means no penalty

user (str): A unique identifier representing your end-user.

stop (str | list[str] | None): To stop generating further
tokens. Only accept stop words that’s encoded to one token idex.

Additional arguments supported by LMDeploy:

ignore_eos (bool): indicator for ignoring eos

skip_special_tokens (bool): Whether or not to remove special tokens
in the decoding. Default to be True.

top_k (int): The number of the highest probability vocabulary
tokens to keep for top-k-filtering

Currently we do not support the following features:

logprobs (not supported yet)

presence_penalty (replaced with repetition_penalty)

frequency_penalty (replaced with repetition_penalty)

Request body:

```text
{
  "echo":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Echo"
  },
  "frequency_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.0,
    "title":"Frequency Penalty"
  },
  "ignore_eos":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Ignore Eos"
  },
  "logprobs":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Logprobs"
  },
  "max_completion_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "description":"An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens",
    "examples":[
      null
    ],
    "title":"Max Completion Tokens"
  },
  "max_tokens":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":16,
    "deprecated":true,
    "examples":[
      16
    ],
    "title":"Max Tokens"
  },
  "min_p":{
    "default":0.0,
    "title":"Min P",
    "type":"number"
  },
  "model":{
    "title":"Model",
    "type":"string"
  },
  "n":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":1,
    "title":"N"
  },
  "presence_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.0,
    "title":"Presence Penalty"
  },
  "prompt":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{},
        "type":"array"
      }
    ],
    "title":"Prompt"
  },
  "repetition_penalty":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":1.0,
    "title":"Repetition Penalty"
  },
  "return_token_ids":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Return Token Ids"
  },
  "seed":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "title":"Seed"
  },
  "session_id":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":-1,
    "title":"Session Id"
  },
  "skip_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Skip Special Tokens"
  },
  "spaces_between_special_tokens":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":true,
    "title":"Spaces Between Special Tokens"
  },
  "stop":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "items":{
          "type":"string"
        },
        "type":"array"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ],
    "title":"Stop"
  },
  "stream":{
    "anyOf":[
      {
        "type":"boolean"
      },
      {
        "type":"null"
      }
    ],
    "default":false,
    "title":"Stream"
  },
  "stream_options":{
    "anyOf":[
      {
        "description":"The stream options.",
        "properties":{
          "include_usage":{
            "anyOf":[
              {
                "type":"boolean"
              },
              {
                "type":"null"
              }
            ],
            "default":false,
            "title":"Include Usage"
          }
        },
        "title":"StreamOptions",
        "type":"object"
      },
      {
        "type":"null"
      }
    ],
    "examples":[
      null
    ]
  },
  "suffix":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"Suffix"
  },
  "temperature":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":0.7,
    "title":"Temperature"
  },
  "top_k":{
    "anyOf":[
      {
        "type":"integer"
      },
      {
        "type":"null"
      }
    ],
    "default":40,
    "title":"Top K"
  },
  "top_p":{
    "anyOf":[
      {
        "type":"number"
      },
      {
        "type":"null"
      }
    ],
    "default":1.0,
    "title":"Top P"
  },
  "user":{
    "anyOf":[
      {
        "type":"string"
      },
      {
        "type":"null"
      }
    ],
    "title":"User"
  }
}
```

Example request:

```text
POST /v1/completions HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "echo": true,
    "frequency_penalty": 1.0,
    "ignore_eos": true,
    "logprobs": 1,
    "max_completion_tokens": 1,
    "max_tokens": 1,
    "min_p": 1.0,
    "model": "string",
    "n": 1,
    "presence_penalty": 1.0,
    "prompt": "string",
    "repetition_penalty": 1.0,
    "return_token_ids": true,
    "seed": 1,
    "session_id": 1,
    "skip_special_tokens": true,
    "spaces_between_special_tokens": true,
    "stop": "string",
    "stream": true,
    "stream_options": {
        "include_usage": true
    },
    "suffix": "string",
    "temperature": 1.0,
    "top_k": 1,
    "top_p": 1.0,
    "user": "string"
}
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```

422 Unprocessable Entity –
Validation Error

Example response:

```text
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
    "detail": [
        {
            "ctx": {},
            "input": {},
            "loc": [
                "string",
                1
            ],
            "msg": "string",
            "type": "string"
        }
    ]
}
```

GET/v1/models#

Available Models

Show available models.

Example request:

```text
GET /v1/models HTTP/1.1
Host: example.com
```

Status Codes:

200 OK –
Successful Response

Example response:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{}
```
