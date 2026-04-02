* Rate Limiter

# Rate Limiter[#](#rate-limiter "Link to this heading")

Rate limiter manages the rate at which requests are scheduled on
model instances by Triton. The rate limiter operates across all
models loaded in Triton to allow *cross-model prioritization*.

In absence of rate limiting (ârate-limit=off), Triton schedules
execution of a request (or set of requests when using dynamic
batching) as soon as a model instance is available. This behavior
is typically best suited for performance. However, there can be
cases where running all the models simultaneously places excessive
load on the server. For instance, model execution on some
frameworks dynamically allocate memory. Running all such models
simultaneously may lead to system going out-of-memory.

Rate limiter allows to postpone the inference execution on some
model instances such that not all of them runs simultaneously.
The model priorities are used to decide which model instance
to schedule next.

## Using Rate Limiter[#](#using-rate-limiter "Link to this heading")

To enable rate limiting users must set `--rate-limit` option when
launching tritonserver. For more information, consult usage of
the option emitted by `tritonserver --help`.

The rate limiter is controlled by the rate limiter configuration given
for each model instance, as described in [rate limiter
configuration](model_configuration.md#rate-limiter-configuration).
The rate limiter configuration includes
[resources](model_configuration.md#resources) and
[priority](model_configuration.md#priority) for the model instances
defined by the instance group.

### Resources[#](#resources "Link to this heading")

Resources are identified by a unique name and a count indicating
the number of copies of the resource. By default, model instance
uses no rate-limiter resources. By listing a resource/count the
model instance indicates that it requires that many resources to
be available on the model instance device before it can be allowed
to execute. When under execution the specified many resources are
allocated to the model instance only to be released when the
execution is over. The available number of resource copies
are, by default, the max across all model instances that list that
resource. For example, assume three loaded model instances A, B
and C each specifying the following resource requirements for
a single device:

```
A: [R1: 4, R2: 4]
B: [R2: 5, R3: 10, R4: 5]
C: [R1: 1, R3: 7, R4: 2]
```

By default, based on those model instance requirements, the server
will create the following resources with the indicated copies:

```
R1: 4
R2: 5
R3: 10
R4: 5
```

These values ensure that all model instances can be successfully
scheduled. The default for a resource can be overridden by giving
it explicitly on command-line using `--rate-limit-resource` option.
`tritonserver --help` will provide with more detailed usage
instructions.

By default, the available resource copies are per-device and resource
requirements for a model instance are enforced against corresponding
resources associated with the device where the model instance runs.
The `--rate-limit-resource` allows users to provide different resource
copies to different devices. Rate limiter can also handle global
resources. Instead of creating resource copies per-device, a global
resource will have a single copy all across the system.

Rate limiter depends upon the model configuration to determine
whether the resource is global or not. See
[resources](model_configuration.md#resources) for more details on
how to specify them in model configuration.

For tritonserver, running on a two device machine, invoked with
`--rate-limit-resource=R1:10 --rate-limit-resource=R2:5:0 --rate-limit-resource=R2:8:1 --rate-limit-resource=R3:2`
, available resource copies are:

```
GLOBAL   => [R3: 2]
DEVICE 0 => [R1: 10, R2: 5]
DEVICE 1 => [R1: 10, R2: 8]
```

where R3 appears as a global resource in one of the loaded model.

### Priority[#](#priority "Link to this heading")

In a resource constrained system, there will be a contention for
the resources among model instances to execute their inference
requests. Priority setting helps determining which model instance
to select for next execution. See [priority](model_configuration.md#priority)
for more information.

