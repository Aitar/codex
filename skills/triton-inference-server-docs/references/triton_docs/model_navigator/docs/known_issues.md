* Known...

# Known Issues and Limitations[#](#known-issues-and-limitations "Link to this heading")

* nav.Module moves original torch.nn.Module to the CPU, in case of weight sharing that might result in unexpected behavior
* For data dependent dynamic control flow (multiple computation graphs) nav.Module might copy the weights for each separate graph
* Source model running in Python can cause OOM issue when GPU memory is larger than CPU RAM memory
* Verify command could potentially experience CUDA OOM errors while trying to run inference on two models at the same time.
* Dependencies between modules in optimized pipelines may lead to unexpected behavior and failure in Inplace Optimize
* TensorRT might require manual installation of correct version of `nvidia-cudnn-cu12` package
* ONNXRuntime 1.17.x does not support ONNX IR 10 (onnx ver 1.16.0)
* ONNXRuntime 1.17.x requires cuDNN 8.x
* DistillBERT ONNX dynamo export does not support dynamic shapes