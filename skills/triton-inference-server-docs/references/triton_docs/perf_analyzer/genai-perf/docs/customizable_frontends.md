* Support a...

# Support a New API With Customizable Frontends[#](#support-a-new-api-with-customizable-frontends "Link to this heading")

This guide explains how you can add support for benchmarking a new API.
The main requirement is that the endpoint uses request and response
formats that are compatible with the OpenAI frontend.

The primary logic involves adding a new converter to the genai-perf repository
under `genai_perf/inputs/converters/`. Converters allow the system to handle
different request formats. Please follow these steps below to add a converter
for your custom API.

## Create the Converter Class[#](#create-the-converter-class "Link to this heading")

Create a new file in the `genai_perf/inputs/converters/` directory, such as
`new_converter.py`.

Define the converter class in this file. Your class should inherit from
BaseConverter, which is located in
`genai_perf/inputs/converters/base_converter.py`. You can reference existing
converters for more code examples.

```
from genai_perf.inputs.converters.base_converter import BaseConverter
from genai_perf.inputs.input_constants import OutputFormat
from genai_perf.exceptions import GenAIPerfException
from typing import Any, Dict

class NewConverter(BaseConverter):
    def check_config(self) -> None:
        # If applicable, any configuration checks go here
        # Else, omit this function

    def convert(
        self, generic_dataset: GenericDataset
    ) -> Dict[Any, Any]:
        request_body: Dict[str, Any] = {"data": []}

        for file_data in generic_dataset.files_data.values():
            for index, row in enumerate(file_data.rows):
                # Select a model name via the specified model selection
                # strategy
                model_name = self._select_model_name(config, index)

                # Populate the request body
                payload = {
                    "model": model_name,
                    "input": row.texts,
                }

                request_body["data"].append(
                    self._finalize_payload(payload, config, row)
                )

        return request_body
```

## Update `__init__.py`[#](#update-init-py "Link to this heading")

In `genai_perf/inputs/converters/__init__.py`, import your new converter class:

```
from .new_converter import NewConverter
```

Then, add the new converter class to the `__all__` list to make it available
for use:

```
__all__ = [
    # Existing converters
    "NewConverter",
]
```

## Create the New Output Format[#](#create-the-new-output-format "Link to this heading")

In `genai_perf/inputs/input_constants`, go to the enum OutputFormat.
Add the name of your new endpoint, so that the endpoint name is detected
by the parser.

```
class OutputFormat(Enum):
    # Existing output formats
    NEW_ENDPOINT = auto()
```

## Map the Output Format to the Converter[#](#map-the-output-format-to-the-converter "Link to this heading")

Open `genai_perf/inputs/converters/output_format_converter_factory.py.`
Add a mapping for your new converter in the converters dictionary, linking
the appropriate OutputFormat value to your converter class:

```
converters = {
    # Existing mappings
    OutputFormat.NEW_FORMAT: NewConverter,
}
```

## Map an Endpoint Type to the Output Format[#](#map-an-endpoint-type-to-the-output-format "Link to this heading")

Open `genai_perf/parser.py`.
Add an mapping for your new endpoint type in the `_endpoint_type_map`.

For example, see the code below.

```
_endpoint_type_map = {
    # Existing mappings
    "NEW-ENDPOINT": EndpointConfig("v1/endpoint", "openai", ic.OutputFormat.NEW_ENDPOINT),
}
```

## Update the Metrics Parser[#](#update-the-metrics-parser "Link to this heading")

GenAI-Perf needs to know which metrics format your API uses. Go to
`genai_perf/main.py`. If your endpoint is not an LLM endpoint, add it to the
list of endpoint types that use a ProfileDataParser.

If you find that GenAI-Perf does not correctly read your response format, it
may be necessary to create a new profile data parser. If so, go to
`genai_perf/profile_data_parser/image_retrieval_profile_data_parser.py` as an
example for how to create a new data parser. Add a parser in the same
directory, then add an if/else branch to the calculate\_metrics function to
use the custom parser for that endpoint type.

## Test the Converter[#](#test-the-converter "Link to this heading")

After implementing your converter, you can run it against your server to
ensure it works:

```
genai-perf profile -m TEST_MODEL --endpoint-type NEW-ENDPOINT
```

You can also write unit tests to ensure it works as expected.
To do so, create a test file in the tests directory.
You can reference existing converter tests named `test_**_converter.py`.
To run the test, run `pytest tests/test_new_converter.py`, replacing the
file name with the name of the file you created.

