* [Performance Analyzer](../../perf_benchmark/perf_analyzer.md)
* Input Data

# Input Data[#](#input-data "Link to this heading")

Use the [`--help`](cli.md#help) option to see complete documentation for all
input data options. By default Perf Analyzer sends random data to all the inputs
of your model. You can select a different input data mode with the
[`--input-data`](cli.md#input-data-zero-random-path) option:

* *random*: (default) Send random data for each input. Note: Perf Analyzer only
  generates random data once per input and reuses that for all inferences
* *zero*: Send zeros for each input.
* directory path: A path to a directory containing a binary file for each input,
  named the same as the input (and optionally a binary file for each output for
  validation, named the same as the output). Each binary file must contain the
  data required for that input/output for a batch-1 request. Each file should
  contain the raw binary representation of the input/output in row-major order.
* file path: A path to a JSON file containing data to be used with every
  inference request. See the âReal Input Dataâ section for further details.
  [`--input-data`](cli.md#input-data-zero-random-path) can be provided multiple
  times with different file paths to specific multiple JSON files.

For tensors with `STRING`/`BYTES` datatype, the
[`--string-length`](cli.md#string-length-n) and
[`--string-data`](cli.md#string-data-string) options may be used in some cases
(see [`--help`](cli.md#help) for full documentation).

For models that support batching you can use the [`-b`](cli.md#b-n) option to
indicate the batch size of the requests that Perf Analyzer should send. For
models with variable-sized inputs you must provide the
[`--shape`](cli.md#shape-string) argument so that Perf Analyzer knows what
shape tensors to use. For example, for a model that has an input called
`IMAGE` that has shape `[3, N, M]`, where `N` and `M` are variable-size
dimensions, to tell Perf Analyzer to send batch size 4 requests of shape
`[3, 224, 224]`:

```
$ perf_analyzer -m mymodel -b 4 --shape IMAGE:3,224,224
```

## Real Input Data[#](#real-input-data "Link to this heading")

The performance of some models is highly dependent on the data used. For such
cases you can provide data to be used with every inference request made by Perf
Analyzer in a JSON file. Perf Analyzer will use the provided data in a
round-robin order when sending inference requests. For sequence models, if a
sequence length is specified via
[`--sequence-length`](cli.md#sequence-length-n), Perf Analyzer will also loop
through the provided data in a round-robin order up to the specified sequence
length (with a percentage variation customizable via
[`--sequence-length-variation`](cli.md#sequence-length-variation-n)).
Otherwise, the sequence length will be the number of inputs specified in
user-provided input data.

Each entry in the `"data"` array must specify all input tensors with the exact
size expected by the model for a single batch. The following example describes
data for a model with inputs named, `INPUT0` and `INPUT1`, shape `[4, 4]` and
data type `INT32`:

```
{
  "data":
    [
      {
        "INPUT0": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "INPUT1": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      },
      {
        "INPUT0": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "INPUT1": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      },
      {
        "INPUT0": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "INPUT1": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      },
      {
        "INPUT0": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "INPUT1": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      }
    ]
}
```

Note that the `[4, 4]` tensor has been flattened in a row-major format for the
inputs. In addition to specifying explicit tensors, you can also provide Base64
encoded binary data for the tensors. Each data object must list its data in a
row-major order. Binary data must be in little-endian byte order. The following
example highlights how this can be achieved:

```
{
  "data":
    [
      {
        "INPUT0": {"b64": "YmFzZTY0IGRlY29kZXI="},
        "INPUT1": {"b64": "YmFzZTY0IGRlY29kZXI="}
      },
      {
        "INPUT0": {"b64": "YmFzZTY0IGRlY29kZXI="},
        "INPUT1": {"b64": "YmFzZTY0IGRlY29kZXI="}
      },
      {
        "INPUT0": {"b64": "YmFzZTY0IGRlY29kZXI="},
        "INPUT1": {"b64": "YmFzZTY0IGRlY29kZXI="}
      }
    ]
}
```

In case of sequence models, multiple data streams can be specified in the JSON
file. Each sequence will get a data stream of its own and Perf Analyzer will
ensure the data from each stream is played back to the same correlation ID. The
below example highlights how to specify data for multiple streams for a sequence
model with a single input named `INPUT`, shape `[1]` and data type `STRING`:

```
{
  "data":
    [
      [
        {
          "INPUT": ["1"]
        },
        {
          "INPUT": ["2"]
        },
        {
          "INPUT": ["3"]
        },
        {
          "INPUT": ["4"]
        }
      ],
      [
        {
          "INPUT": ["1"]
        },
        {
          "INPUT": ["1"]
        },
        {
          "INPUT": ["1"]
        }
      ],
      [
        {
          "INPUT": ["1"]
        },
        {
          "INPUT": ["1"]
        }
      ]
    ]
}
```

The above example describes three data streams with lengths 4, 3 and 2
respectively. Perf Analyzer will hence produce sequences of length 4, 3 and 2 in
this case.

You can also provide an optional `"shape"` field to the tensors. This is
especially useful while profiling the models with variable-sized tensors as
input. Additionally note that when providing the `"shape"` field, tensor
contents must be provided separately in a âcontentâ field in row-major order.
The specified shape values will override default input shapes provided as a
command line option (see [`--shape`](cli.md#shape-string)) for variable-sized
inputs. In the absence of a `"shape"` field, the provided defaults will be used.
There is no need to specify shape as a command line option if all the input data
provide shape values for variable tensors. Below is an example JSON file for a
model with a single input `INPUT`, shape `[-1, -1]` and data type `INT32`:

```
{
  "data":
    [
      {
        "INPUT":
          {
              "content": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              "shape": [2,8]
          }
      },
      {
        "INPUT":
          {
              "content": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              "shape": [8,2]
          }
      },
      {
        "INPUT":
          {
              "content": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          }
      },
      {
        "INPUT":
          {
              "content": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              "shape": [4,4]
          }
      }
    ]
}
```

The following is the example to provide contents as base64 string with explicit
shapes:

```
{
  "data":
    [
      {
        "INPUT":
          {
            "content": {"b64": "/9j/4AAQSkZ(...)"},
            "shape": [7964]
          }
      },
      {
        "INPUT":
          {
            "content": {"b64": "/9j/4AAQSkZ(...)"},
            "shape": [7964]
          }
      }
    ]
}
```

Note that for `STRING` type, an element is represented by a 4-byte unsigned
integer giving the length followed by the actual bytes. The byte array to be
encoded using base64 must include the 4-byte unsigned integers.

### OpenAI Chat[#](#openai-chat "Link to this heading")

Perf Analyzer can also be used to profile OpenAI API-compatible servers. Users
must provide an input data JSON via
[`--input-data`](cli.md#input-data-zero-random-path) containing the HTTP request
bodies of the requests to be sent to the OpenAI API-compatible server. See the
example below:

```
{
  "data": [
    {
      "payload": [
        {
          "model": "facebook/opt-125m",
          "messages": [{ "role": "user",
                         "content": "Who wrote the play Romeo and Juliet?" }],
          "max_tokens": 32
        }
      ]
    },
    {
      "payload": [
        {
          "model": "facebook/opt-125m",
          "messages": [{ "role": "user", "content": "What is 1+1?" }],
          "max_tokens": 32
        }
      ]
    }
  ]
}
```

#### OpenAI Multi-Turn Chat[#](#openai-multi-turn-chat "Link to this heading")

Perf Analyzer can also be used to benchmark multi-turn chat models on an
OpenAI API-compatible server. This is currently done via the
[`--session-concurrency`](cli.md) option. Users must provide an input data JSON
via [`--input-data`](cli.md#input-data-zero-random-path) containing the HTTP
request bodies of the requests to be sent with a delay associated with each
request for how long to wait between the requestâs response returns and when the
next request in the multi-turn chat is sent. The last request of a particular
session/multi-turn chat does not need a delay value since there is no next turn.
See the example below:

```
{
  "data": [
    {
      "payload": [
        {
          "model": "facebook/opt-125m",
          "messages": [{ "role": "user",
                         "content": "Who wrote the play Romeo and Juliet?" }],
          "max_tokens": 32
        }
      ],
      "session_id": ["16d63027-f8d8-4a2d-83ac-0cde28f5a431"],
      "delay": [3000]
    },
    {
      "payload": [
        {
          "model": "facebook/opt-125m",
          "messages": [{ "role": "user",
                         "content": "What is it about?" }],
          "max_tokens": 32
        }
      ],
      "session_id": ["16d63027-f8d8-4a2d-83ac-0cde28f5a431"]
    },
    {
      "payload": [
        {
          "model": "facebook/opt-125m",
          "messages": [{ "role": "user",
                         "content": "What is 2+2?" }],
          "max_tokens": 32
        }
      ],
      "delay": [2000],
      "session_id": ["d1ed35c3-2a3a-444e-8e0a-6f0714202cb1"],
    },
    {
      "payload": [
        {
          "model": "facebook/opt-125m",
          "messages": [{ "role": "user",
                         "content": "What the square root of that?" }],
          "max_tokens": 32
        }
      ],
      "session_id": ["d1ed35c3-2a3a-444e-8e0a-6f0714202cb1"]
    }
  ]
}
```

### Output Validation[#](#output-validation "Link to this heading")

When real input data is provided, it is optional to request Perf Analyzer to
validate the inference output for the input data.

Validation output can be specified in the `"validation_data"` field have the
same format as the `"data"` field for real input. Note that the entries in
`"validation_data"` must align with `"data"` for proper mapping. The following
example describes validation data for a model with inputs named `INPUT0` and
`INPUT1`, outputs named `OUTPUT0` and `OUTPUT1`, all tensors have shape `[4, 4]`
and data type `INT32`:

```
{
  "data":
    [
      {
        "INPUT0": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "INPUT1": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      }
    ],
  "validation_data":
    [
      {
        "OUTPUT0": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "OUTPUT1": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
      }
    ]
}
```

Besides the above example, the validation outputs can be specified in the same
variations described in the real input data section.

# Shared Memory[#](#shared-memory "Link to this heading")

By default Perf Analyzer sends input tensor data and receives output tensor data
over the network. You can instead instruct Perf Analyzer to use system shared
memory or CUDA shared memory to communicate tensor data. By using these options
you can model the performance that you can achieve by using shared memory in
your application. Use
[`--shared-memory=system`](cli.md#shared-memory-none-system-cuda) to use system
(CPU) shared memory or
[`--shared-memory=cuda`](cli.md#shared-memory-none-system-cuda) to use CUDA
shared memory.

## Dynamic gRPC[#](#dynamic-grpc "Link to this heading")

When using the dynamic gRPC service kind,
you can configure multiple input data via the `message_generator` field
that can be used to generate a pool of input data (e.g. Protobuf messages) for the gRPC service.
The Protobuf messages generated from each command specified in the `message_generator` field
can be used to send individual inference requests to the gRPC service,
and Perf Analyzer will cycle through each input data in a round-robin manner
when sending inference requests,
which is similar to its default behavior when the `message_generator` field is not specified.

For example, given the following input JSON:

```
{
  "data": [
    {
      "message_generator": "python3 example.py --arg1 value1 --arg2 value2"
    },
    {
      "message_generator": "python3 example.py --arg1 value3 --arg2 value4"
    }
  ]
}
```

In this configuration, Perf Analyzer will read the Protobuf messages from each of the two commands specified in the `message_generator` field,
and create a pool of two separate input data that can be used to send inference requests.
Each input data can be customized, as in the example above,
and contain any user-specified Protobuf messages
(as long as they conform to the gRPC serviceâs expected definition).

### JSON Schema[#](#json-schema "Link to this heading")

Hereâs the JSON schema for the input JSON file when using the dynamic gRPC service kind:

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Dynamic gRPC input JSON Schema",
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "message_generator": {
            "type": "string"
          }
        },
        "required": [
          "message_generator"
        ]
      }
    }
  },
  "required": [
    "data"
  ]
}
```

