* [API Reference](../client_guide/api_reference.md)
* [Extensions](../client_guide/kserve_extension.md)
* Schedule...

# Schedule Policy Extension[#](#schedule-policy-extension "Link to this heading")

This document describes Tritonâs schedule policy extension. The
schedule-policy extension allows an inference request to provide
parameters that influence how Triton handles and schedules the
request. Because this extension is supported, Triton reports
âschedule\_policyâ in the extensions field of its Server Metadata.
Note the policies are specific to [dynamic
batcher](../user_guide/model_configuration.md#dynamic-batcher)
and only experimental support to [sequence
batcher](../user_guide/model_configuration.md#sequence-batcher)
with the [direct](../user_guide/architecture.md#direct)
scheduling strategy.

## Dynamic Batcher[#](#dynamic-batcher "Link to this heading")

The schedule-policy extension uses request parameters to indicate the
policy. The parameters and their type are:

* âpriorityâ : int64 value indicating the priority of the
  request. Priority value zero indicates that the default priority
  level should be used (i.e. same behavior as not specifying the
  priority parameter). Lower value priorities indicate higher priority
  levels. Thus the highest priority level is indicated by setting the
  parameter to 1, the next highest is 2, etc.
* âtimeoutâ : int64 value indicating the timeout value for the
  request, in microseconds. If the request cannot be completed within
  the time Triton will take a model-specific action such as
  terminating the request.

Both parameters are optional and, if not specified, Triton will handle
the request using the default priority and timeout values appropriate
for the model.

## Sequence Batcher with Direct Scheduling Strategy[#](#sequence-batcher-with-direct-scheduling-strategy "Link to this heading")

**Note that the schedule policy for sequence batcher is at experimental stage
and it is subject to change.**

The schedule-policy extension uses request parameters to indicate the
policy. The parameters and their type are:

* âtimeoutâ : int64 value indicating the timeout value for the
  request, in microseconds. If the request cannot be completed within
  the time Triton will terminate the request, as well as the corresponding
  sequence and received requests of the sequence. The timeout will only be
  applied to requests of the sequences that havenât been allocated a batch slot
  for execution, the requests of the sequences that have been allocated batch
  slots will not be affected by the timeout setting.

The parameter is optional and, if not specified, Triton will handle
the request and corresponding sequence based on the model configuration.

