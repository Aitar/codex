* Schedulers

# Schedulers[#](#schedulers "Link to this heading")

Triton supports batch inferencing by allowing individual inference
requests to specify a batch of inputs. The inferencing for a batch of
inputs is performed at the same time which is especially important for
GPUs since it can greatly increase inferencing throughput. In many use
cases the individual inference requests are not batched, therefore,
they do not benefit from the throughput benefits of batching.

The inference server contains multiple scheduling and batching
algorithms that support many different model types and use-cases. More
information about model types and schedulers can be found in [Models
And Schedulers](architecture.md#models-and-schedulers).

## Default Scheduler[#](#default-scheduler "Link to this heading")

The default scheduler is used for a model if none of the
*scheduling\_choice* properties are specified in the model
configuration. The default scheduler simply distributes inference
requests to all [model instances](model_configuration.md#instance-groups) configured for the
model.

## Ensemble Scheduler[#](#ensemble-scheduler "Link to this heading")

The ensemble scheduler must be used for [ensemble
models](architecture.md#ensemble-models) and cannot be used for any
other type of model.

The ensemble scheduler is enabled and configured independently for
each model using the *ModelEnsembleScheduling* property in the model
configuration. The settings describe the models that are included in
the ensemble and the flow of tensor values between the models. See
[Ensemble Models](architecture.md#ensemble-models) for more
information and examples.

