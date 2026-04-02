* Preprocessin...

# Preprocessing Using Python Backend Example[#](#preprocessing-using-python-backend-example "Link to this heading")

This example shows how to preprocess your inputs using Python backend before it is passed to the TensorRT model for inference. This ensemble model includes an image preprocessing model (preprocess) and a TensorRT model (resnet50\_trt) to do inference.

**1. Converting PyTorch Model to ONNX format:**

Run onnx\_exporter.py to convert ResNet50 PyTorch model to ONNX format. Width and height dims are fixed at 224 but dynamic axes arguments for dynamic batching are used. Commands from the 2. and 3. subsections shall be executed within this Docker container.

```
docker run -it --gpus=all -v $(pwd):/workspace nvcr.io/nvidia/pytorch:xx.yy-py3 bash
pip install numpy pillow torchvision
python onnx_exporter.py --save model.onnx
```

**2. Create the model repository:**

```
mkdir -p model_repository/ensemble_python_resnet50/1
mkdir -p model_repository/preprocess/1
mkdir -p model_repository/resnet50_trt/1

# Copy the Python model
cp model.py model_repository/preprocess/1
```

**3. Build a TensorRT engine for the ONNX model**

Set the arguments for enabling fp16 precision âfp16. To enable dynamic shapes use âminShapes, âoptShapes, and maxShapes with âexplicitBatch:

```
trtexec --onnx=model.onnx --saveEngine=./model_repository/resnet50_trt/1/model.plan --explicitBatch --minShapes=input:1x3x224x224 --optShapes=input:1x3x224x224 --maxShapes=input:256x3x224x224 --fp16
```

**4. Run the command below to start the server container:**

Under python\_backend/examples/preprocessing, run this command to start the server docker container:

```
docker run --gpus=all -it --rm -p8000:8000 -p8001:8001 -p8002:8002 -v$(pwd):/workspace/ -v/$(pwd)/model_repository:/models nvcr.io/nvidia/tritonserver:xx.yy-py3 bash
pip install numpy pillow torchvision
tritonserver --model-repository=/models
```

**5. Start the client to test:**

Under python\_backend/examples/preprocessing, run the commands below to start the client Docker container:

```
wget https://raw.githubusercontent.com/triton-inference-server/server/main/qa/images/mug.jpg -O "mug.jpg"
docker run --rm --net=host -v $(pwd):/workspace/ nvcr.io/nvidia/tritonserver:xx.yy-py3-sdk python client.py --image mug.jpg
The result of classification is:COFFEE MUG
```

Here, since we input an image of âmugâ and the inference result is âCOFFEE MUGâ which is correct.