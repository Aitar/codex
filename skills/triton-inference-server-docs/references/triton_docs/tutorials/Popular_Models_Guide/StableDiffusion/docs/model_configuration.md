* Stable...

# Stable Diffusion Model Configuration Options[#](#stable-diffusion-model-configuration-options "Link to this heading")

The example python based backend
[`/backend/diffusion/model.py`](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion/backend/diffusion/model.py) supports
the following configuration parameters to customize the model being served.

## Full Configuration Examples[#](#full-configuration-examples "Link to this heading")

* [Stable Diffusion v1.5](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion/diffusion-models/stable_diffusion_1_5/config.pbtxt)
* [Stable Diffusion XL](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion/diffusion-models/stable_diffusion_xl/config.pbtxt)

## Batch Size and Dynamic Batching[#](#batch-size-and-dynamic-batching "Link to this heading")

You can select the batch size and dynamic batching queue delay. With
batch size 1 dynamic batching is disabled.

> [!Note]
> Changing the batch size requires rebuilding the TensorRT Engines

```
max_batch_size: 1

dynamic_batching {
 max_queue_delay_microseconds: 100000
}
```

## Engine Building Parameters[#](#engine-building-parameters "Link to this heading")

The following configuration parameters affect the engine build.

Please see the [TensorRT demo](https://github.com/NVIDIA/TensorRT/tree/release/9.2/demo/Diffusion)
for more information.

```
{
  key: "onnx_opset"
  value: {
    string_value: "18"
  }
},
{
  key: "image_height"
  value: {
    string_value: "512"
  }
},
{
  key: "image_width"
  value: {
    string_value: "512"
  }
},
{
  key: "version"
  value: {
    string_value: "1.5"
  }
}
```

## Forcing Engine Build[#](#forcing-engine-build "Link to this heading")

Setting the following parameter to a non empty value will force an
engine rebuild.

```
{
  key: "force_engine_build"
  value: {
    string_value: ""
  }
}
```

## Runtime Settings[#](#runtime-settings "Link to this heading")

The following configuration parameters affect the runtime behavior of the model.
Please see the [TensorRT demo](https://github.com/NVIDIA/TensorRT/tree/release/9.2/demo/Diffusion)
for more information.

Setting a non null integer value for `seed` will result in
deterministic results.

```
{
  key: "steps"
  value: {
    string_value: "50"
  }
},
{
  key: "scheduler"
  value: {
    string_value: ""
  }
},
{
  key: "guidance_scale"
  value: {
    string_value: "7.5"
  }
},
{
  key: "seed"
  value: {
    string_value: ""
  }
}
```

