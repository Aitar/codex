* [In-Process Triton Server API](../../../../client_guide/in_process.md)
* [Python](../../../../client_guide/python.md)
* Triton...

# Triton Inference Server Kafka I/O Deployment[#](#triton-inference-server-kafka-i-o-deployment "Link to this heading")

Using the Triton Inference Server In-Process Python API you can
integrate triton server based models into any Python framework
to consume the messages from a Kafka topic and produce the inference results
back to the kafka topic of choice.

This directory contains an example Triton Inference Server
deployment based on Kafka I/O that uses threads for each of server, consumer and producer.

| [Installation](#installation) | [Run Deployment](#starting-the-pipeline) | [Send Requests](#send-requests-to-deployment) |

## Installation[#](#installation "Link to this heading")

In this Kafka I/O pipeline we deploy a pre-processing stage of tokenization based on `transformers` tokenization module and can be extended to any type of models as needed.

### Pre-requisite[#](#pre-requisite "Link to this heading")

1. [Docker](https://docs.docker.com/engine/install/)

### Starting docker container[#](#starting-docker-container "Link to this heading")

Once you have the docker service up and running, launch a container by executing the following command:

```
docker run --rm -it --gpus all -v <path>/<to>/tutorials/Triton_Inference_Server_Python_API/examples/kafka-io/:/opt/tritonserver/kafka-io -w /opt/tritonserver/kafka-io  --entrypoint bash nvcr.io/nvidia/tritonserver:24.06-py3
```

### Clone Repository[#](#clone-repository "Link to this heading")

```
git clone https://github.com/triton-inference-server/tutorials.git
cd tutorials/Triton_Inference_Server_Python_API/examples/kafka-io
```

*Note: Skip this step if you have mounted the git repository from local directory to the docker container*

### Install dependencies[#](#install-dependencies "Link to this heading")

Please note that installation times may vary depending on
your hardware configuration and network connection.

```
pip install -r requirements.txt
```

If triton server is not already installed, install the dependency by using the following command.

```
pip install /opt/tritonserver/python/tritonserver-2.44.0-py3-none-any.whl
```

Next run the provided `start-kafka.sh` script that will perform the following actions:

1. Download kafka and itâs dependencies
2. Start Kafka service by starting Zookeeper and Kafka brokers
3. Create 2 new topics with names `inference-input` as input queue and `inference-output` to store the inference results

```
chmod +x start-kafka.sh
./start-kafka.sh
```

## Starting the pipeline[#](#starting-the-pipeline "Link to this heading")

### Start the inference pipeline[#](#start-the-inference-pipeline "Link to this heading")

Run the provided `start-server.sh` script that will perform the following actions:

1. Export Kafka Producer and Consumer configs, topic names for input and output topics, model name and repositories.
2. Start the server.

```
chmod +x start-server.sh
./start-server.sh
```

When your console outputs something similar to:

```
2024-07-18 21:55:38,254 INFO api.py:609 -- Deployed app 'default' successfully.
```

It means that the server has started successfully. You can press `Ctrl+C` and proceed to the next steps.

*Note: In the above invocation, we are using default of 1 thread for kafka consumer, however, if you need to increase the concurrency, please set the environment variable `KAFKA_CONSUMER_MAX_WORKER_THREADS` to the desired value and restart the server. This should start the server with new concurrency of the consumer to increase the throughput of the deployment*

## Send Requests to Deployment[#](#send-requests-to-deployment "Link to this heading")

In order to send requests to inference pipeline deployed, produce messages into the input kafka topic using the following command.

```
cd kafka_2.13-3.7.0
bin/kafka-console-producer.sh --topic inference-input --bootstrap-server localhost:9092
```

Once, the above command has been executed, you should see a prompt `>` to start ingesting the messages to the input topic.

```
> this is a sample message
>
```

Once you have produced enough messages, you can exit the prompt by pressing `Ctrl+C`.

### Example Output[#](#example-output "Link to this heading")

Once the workflow consumes the ingested messages from the kafka topic, it invokes the triton server and produces the inference output as `json` string to the output kafka topic. Once the message has been ingested, we can start the consumer to see the output messages from the pipeline ingested to the output topic

```
bin/kafka-console-consumer.sh --topic inference-output --from-beginning --bootstrap-server localhost:9092
```

Since, our example has a tokenizer deployed as a custom model in triton, we should see an output inserted into kafka topic as shown below.

```
{"model": {"name": "tokenizer", "version": 1, "state": null, "reason": null}, "request_id": "", "parameters": {}, "outputs": {"input_ids": [[101, 1142, 1110, 2774, 3802, 118, 1207, 130, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "token_type_ids": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "attention_mask": [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}, "error": null, "classification_label": null, "final": true}
```

