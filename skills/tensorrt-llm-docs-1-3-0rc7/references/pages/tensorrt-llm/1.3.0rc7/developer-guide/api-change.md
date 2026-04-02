# LLM API Change Guide — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/developer-guide/api-change.html

LLM API Change Guide#

This guide explains how to modify and manage APIs in TensorRT LLM, focusing on the high-level LLM API.

Overview#

TensorRT LLM provides multiple API levels:

LLM API - The highest-level API (e.g., the `LLM` class)

PyExecutor API - The mid-level API (e.g., the `PyExecutor` class)

This guide focuses on the LLM API, which is the primary interface for most users.

API Types and Stability Guarantees#

TensorRT LLM classifies APIs into two categories:

1. Committed APIs#

Stable and guaranteed to remain consistent across releases

No breaking changes without major version updates

Schema stored in: `tests/unittest/api_stability/references_committed/`

2. Non-committed APIs#

Under active development and may change between releases

Marked with a `status` field in the docstring:

`prototype` - Early experimental stage

`beta` - More stable but still subject to change

`deprecated` - Scheduled for removal

Schema stored in: `tests/unittest/api_stability/references/`

See API status documentation for complete details

API Schema Management#

All API schemas are:

Stored as YAML files in the codebase

Protected by unit tests in `tests/unittest/api_stability/`

Automatically validated to ensure consistency

API Change Principles#

1. Knob Naming#

Use Semantic Clarity

Argument names should describe what the argument represents, not how it is used internally.

✅ Good: `max_new_tokens` (clear meaning)

❌ Bad: `num` (ambiguous)

Reflect Argument Type and Granularity

For boolean knobs, prefix with verbs like `enable_` and so on.

Examples: `enable_cache`, `enable_flash_attention`

For numerical threshold knobs, suffix with `_limit`, `_size`, `_count`, `_len_` or `_ratio`

Examples: `max_seq_len`, `prefill_batch_size`

Avoid Redundant Prefixes

Example (in `MoeConfig`):

✅ Good: `backend`

❌ Bad: `moe_backend` (redundant since it’s already in `MoeConfig`)

Use Specific Names for Narrow Scenarios

When adding knobs for specific use cases, make the name convey the restriction clearly via a prefix. It’s acceptable to rename later when the knob becomes more generic or is moved into a dedicated config.

Example (argument to the LLM class):

✅ Good: `rope_scaling_factor` → clearly indicates it’s for RoPE

❌ Bad: `scaling_factor` → too generic and prone to misuse

2. Hierarchical Configuration#

Organize complex or hierarchical arguments into dedicated configuration dataclasses with intuitive and consistent naming.

Guidelines

Use the `XxxConfig` suffix consistently

Examples: `ModelConfig`, `ParallelConfig`, `MoeConfig`

Reflect conceptual hierarchy

The dataclass name should represent a coherent functional unit, not an arbitrary grouping

Avoid over-nesting

Use only one level of configuration hierarchy whenever possible (e.g., `LlmArgs→ParallelConfig`) to balance readability and modularity

3. Prefer `LlmArgs` Over Environment Variables#

`LlmArgs` is the central place for all configuration knobs. It integrates with our infrastructure to ensure:

API Stability

Protects committed (stable) APIs

GitHub reviewer committee oversees API stability

API Status Registration

Uncommitted (unstable) APIs must be marked as `"prototype"` or `"beta"`

API statuses are displayed in the documentation

API Documentation

Each knob uses a `Field` with a description

Automatically rendered in public documentation

Managing knobs in `LlmArgs` remains scalable and maintainable thanks to our existing infrastructure and review processes.

Drawbacks of Environment Variables:

Dispersed across the codebase

Lack documentation and discoverability

Pose challenges for testing and validation

Guidelines for Adding Knobs:

✅ Add clear, descriptive documentation for each field

✅ It’s fine to add temporary knobs and refine them later

⚠️ Always mark temporary knobs as `"prototype"` if not stable yet

✅ Refactor prototype knobs as they mature, promote them to “beta” or “stable”.

Modifying LLM Constructor Arguments#

The LLM class accepts numerous configuration parameters for models, runtime, and other components. These are managed through a Pydantic dataclass called `LlmArgs`.

Architecture#

The LLM’s `__init__` method parameters map directly to `LlmArgs` fields

`LlmArgs` is an alias for `TorchLlmArgs` (defined in `tensorrt_llm/llmapi/llm_args.py`)

All arguments are validated and type-checked through Pydantic

Adding a New Argument#

Follow these steps to add a new constructor argument:

1. Add the field to `TorchLlmArgs`#

```text
garbage_collection_gen0_threshold: int = Field(
    default=20000,
    description=(
        "Threshold for Python garbage collection of generation 0 objects. "
        "Lower values trigger more frequent garbage collection."
    ),
    status="beta"  # Required for non-committed arguments
)
```

Field requirements:

Type annotation: Required for all fields

Default value: Recommended unless the field is mandatory

Description: Clear explanation of the parameter’s purpose

Status: Required for non-committed arguments (`prototype`, `beta`, etc.)

2. Update the API schema#

Add the field to the appropriate schema file:

Non-committed arguments: `tests/unittest/api_stability/references/llm.yaml`

```text
garbage_collection_gen0_threshold:
  type: int
  default: 20000
  status: beta  # Must match the status in code
```

Committed arguments: `tests/unittest/api_stability/references_committed/llm.yaml`

```text
garbage_collection_gen0_threshold:
  type: int
  default: 20000
  # No status field for committed arguments
```

3. Run validation tests#

```text
python -m pytest tests/unittest/api_stability/test_llm_api.py
```

Modifying LLM Class Methods#

Public methods in the LLM class constitute the API surface. All changes must be properly documented and tracked.

Implementation Details#

The actual implementation is in the `_TorchLLM` class (llm.py)

Public methods (not starting with `_`) are automatically exposed as APIs

Adding a New Method#

Follow these steps to add a new API method:

1. Implement the method in `_TorchLLM`#

For non-committed APIs, use the `@set_api_status` decorator:

```text
@set_api_status("beta")
def generate_with_streaming(
    self,
    prompts: List[str],
    **kwargs
) -> Iterator[GenerationOutput]:
    """Generate text with streaming output.

    Args:
        prompts: Input prompts for generation
        **kwargs: Additional generation parameters

    Returns:
        Iterator of generation outputs
    """
    # Implementation here
    pass
```

For committed APIs, no decorator is needed:

```text
def generate(self, prompts: List[str], **kwargs) -> GenerationOutput:
    """Generate text from prompts."""
    # Implementation here
    pass
```

2. Update the API schema#

Add the method to the appropriate `llm.yaml` file:

Non-committed API (`tests/unittest/api_stability/references/llm.yaml`):

```text
generate_with_streaming:
  status: beta  # Must match @set_api_status
  parameters:
    - name: prompts
      type: List[str]
    - name: kwargs
      type: dict
  returns: Iterator[GenerationOutput]
```

Committed API (`tests/unittest/api_stability/references_committed/llm.yaml`):

```text
generate:
  parameters:
    - name: prompts
      type: List[str]
    - name: kwargs
      type: dict
  returns: GenerationOutput
```

Modifying Existing Methods#

When modifying existing methods:

Non-breaking changes (adding optional parameters):

Update the method signature

Update the schema file

No status change needed

Breaking changes (changing required parameters, return types):

Only allowed for non-committed APIs

Consider deprecation path for beta APIs

Update documentation with migration guide

Best Practices#

Documentation: Always include comprehensive docstrings

Type hints: Use proper type annotations for all parameters and returns

Testing: Add unit tests for new methods

Examples: Provide usage examples in the docstring

Validation: Run API stability tests before submitting changes

Running Tests#

Validate your changes:

```text
# Run API stability tests
python -m pytest tests/unittest/api_stability/

# Run specific test for LLM API
python -m pytest tests/unittest/api_stability/test_llm_api.py -v
```

Common Workflows#

Promoting an API from Beta to Committed#

Remove the `@set_api_status("beta")` decorator from the method

Move the schema entry from `tests/unittest/api_stability/references/` to `tests/unittest/api_stability/references_committed/`

Remove the `status` field from the schema

Update any documentation referring to the API’s beta status

Deprecating an API#

Add `@set_api_status("deprecated")` to the method

Update the schema with `status:deprecated`

Add deprecation warning in the method:

```text
import warnings
warnings.warn(
    "This method is deprecated and will be removed in v2.0. "
    "Use new_method() instead.",
    DeprecationWarning,
    stacklevel=2
)
```

Document the migration path
