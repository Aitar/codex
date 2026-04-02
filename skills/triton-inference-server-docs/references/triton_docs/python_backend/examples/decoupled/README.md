* Decoupled...

# Decoupled Model Examples[#](#decoupled-model-examples "Link to this heading")

In this section we demonstrate an end-to-end examples for developing and
serving [decoupled models](../../README.md#decoupled-mode) in Python backend.

[repeat\_model.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled/repeat_model.py) and [square\_model.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled/square_model.py) demonstrate
how to write a decoupled model where each request can generate 0 to many responses.
These files are heavily commented to describe each function call.
These example models are designed to show the flexibility available to decoupled models
and in no way should be used in production. These examples circumvents
the restriction placed by the
[instance count](../../../user_guide/model_configuration.md#instance-groups)
and allows multiple requests to be in process even for single instance. In
real deployment, the model should not allow the caller thread to return from
`execute` until that instance is ready to handle another set of requests.

## Deploying the Decoupled Models[#](#deploying-the-decoupled-models "Link to this heading")

1. Create the model repository:

```
mkdir -p models/repeat_int32/1
mkdir -p models/square_int32/1

# Copy the Python models
cp examples/decoupled/repeat_model.py models/repeat_int32/1/model.py
cp examples/decoupled/repeat_config.pbtxt models/repeat_int32/config.pbtxt
cp examples/decoupled/square_model.py models/square_int32/1/model.py
cp examples/decoupled/square_config.pbtxt models/square_int32/config.pbtxt
```

2. Start the tritonserver:

```
tritonserver --model-repository `pwd`/models
```

## Running inference on Repeat model:[#](#running-inference-on-repeat-model "Link to this heading")

Send inference requests to repeat model using [repeat\_client.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled/repeat_client.py).

```
python3 examples/decoupled/repeat_client.py
```

You should see an output similar to the output below:

```
stream started...
async_stream_infer
model_name: "repeat_int32"
id: "0"
inputs {
  name: "IN"
  datatype: "INT32"
  shape: 4
}
inputs {
  name: "DELAY"
  datatype: "UINT32"
  shape: 4
}
inputs {
  name: "WAIT"
  datatype: "UINT32"
  shape: 1
}
outputs {
  name: "OUT"
}
outputs {
  name: "IDX"
}
raw_input_contents: "\004\000\000\000\002\000\000\000\000\000\000\000\001\000\000\000"
raw_input_contents: "\001\000\000\000\002\000\000\000\003\000\000\000\004\000\000\000"
raw_input_contents: "\005\000\000\000"

enqueued request 0 to stream...
infer_response {
  model_name: "repeat_int32"
  model_version: "1"
  id: "0"
  outputs {
    name: "IDX"
    datatype: "UINT32"
    shape: 1
  }
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\000\000\000\000"
  raw_output_contents: "\004\000\000\000"
}

infer_response {
  model_name: "repeat_int32"
  model_version: "1"
  id: "0"
  outputs {
    name: "IDX"
    datatype: "UINT32"
    shape: 1
  }
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\001\000\000\000"
  raw_output_contents: "\002\000\000\000"
}

infer_response {
  model_name: "repeat_int32"
  model_version: "1"
  id: "0"
  outputs {
    name: "IDX"
    datatype: "UINT32"
    shape: 1
  }
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\002\000\000\000"
  raw_output_contents: "\000\000\000\000"
}

infer_response {
  model_name: "repeat_int32"
  model_version: "1"
  id: "0"
  outputs {
    name: "IDX"
    datatype: "UINT32"
    shape: 1
  }
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\003\000\000\000"
  raw_output_contents: "\001\000\000\000"
}

PASS: repeat_int32
stream stopped...
```

Look how a single request generated 4 responses.

## Running inference on Square model:[#](#running-inference-on-square-model "Link to this heading")

Send inference requests to square model using [square\_client.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled/square_client.py).

```
python3 examples/decoupled/square_client.py
```

You should see an output similar to the output below:

```
stream started...
async_stream_infer
model_name: "square_int32"
id: "0"
inputs {
  name: "IN"
  datatype: "INT32"
  shape: 1
}
outputs {
  name: "OUT"
}
raw_input_contents: "\004\000\000\000"

enqueued request 0 to stream...
async_stream_infer
model_name: "square_int32"
id: "1"
inputs {
  name: "IN"
  datatype: "INT32"
  shape: 1
}
outputs {
  name: "OUT"
}
raw_input_contents: "\002\000\000\000"

enqueued request 1 to stream...
async_stream_infer
model_name: "square_int32"
id: "2"
inputs {
  name: "IN"
  datatype: "INT32"
  shape: 1
}
outputs {
  name: "OUT"
}
raw_input_contents: "\000\000\000\000"

enqueued request 2 to stream...
async_stream_infer
model_name: "square_int32"
id: "3"
inputs {
  name: "IN"
  datatype: "INT32"
  shape: 1
}
outputs {
  name: "OUT"
}
raw_input_contents: "\001\000\000\000"

enqueued request 3 to stream...
infer_response {
  model_name: "square_int32"
  model_version: "1"
  id: "0"
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\004\000\000\000"
}

infer_response {
  model_name: "square_int32"
  model_version: "1"
  id: "1"
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\002\000\000\000"
}

infer_response {
  model_name: "square_int32"
  model_version: "1"
  id: "0"
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\004\000\000\000"
}

infer_response {
  model_name: "square_int32"
  model_version: "1"
  id: "3"
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\001\000\000\000"
}

infer_response {
  model_name: "square_int32"
  model_version: "1"
  id: "1"
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\002\000\000\000"
}

infer_response {
  model_name: "square_int32"
  model_version: "1"
  id: "0"
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\004\000\000\000"
}

infer_response {
  model_name: "square_int32"
  model_version: "1"
  id: "0"
  outputs {
    name: "OUT"
    datatype: "INT32"
    shape: 1
  }
  raw_output_contents: "\004\000\000\000"
}

PASS: square_int32
stream stopped...
```

Look how responses were delivered out-of-order of requests.
The generated responses can be tracked to their request using
the `id` field.

