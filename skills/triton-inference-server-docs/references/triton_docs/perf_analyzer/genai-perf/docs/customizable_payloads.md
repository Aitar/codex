* Use Custom...

# Use Custom Payload Formats[#](#use-custom-payload-formats "Link to this heading")

With GenAI-Perf, you can customize how input data is formatted into payloads
using templates. This allows you to define how payloads are
structured when sent to an inference server.

This feature is only available for Triton.

These provide less customizability than a
[customizable frontend](customizable_frontends.md), which is used when more
endpoint-specific logic is necessary. Templates are used when
the only change necessary is specifying a custom payload schema.

## Table of Contents[#](#table-of-contents "Link to this heading")

* [Use a Named Template (Predefined)](#predefined)
* [Use a Custom Template (Fully Customizable)](#custom)

## Use a Named Template [#](#use-a-named-template "Link to this heading")

GenAI-Perf provides common built-in templates to simplify request formatting.
You can find these in `NAMED_TEMPLATES` in the class
[template\_converter](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/genai_perf/inputs/converters/template_converter.py).

One such template is `nv-embedqa`, which structures requests for
embedding-based models.

### Example: Use the nv-embedqa Named Template[#](#example-use-the-nv-embedqa-named-template "Link to this heading")

Run the following command:

```
genai-perf profile \
  --model MY_MODEL \
  --endpoint-type template \
  --num-payloads 2 \
  --extra-inputs payload_template:nv-embedqa
```

#### Result[#](#result "Link to this heading")

GenAI-Perf will use the nv-embedqa template to format the input data.

After conversion, the `inputs.json` file would look similar to this:

```
{
    "data": [
        {"text": ["example1"]},
        {"text": ["example2"]}
    ]
}
```

## Use a Custom Template [#](#use-a-custom-template "Link to this heading")

Sometimes, you may have a custom payload format.
Custom templates allow you to benchmark using GenAI-Perf.

Here is an example template:

```
    {% for item in texts %}
        {"custom_key": [{{ item|tojson }}]}{% if not loop.last %},{% endif %}
    {% endfor %}
```

This tells GenAI-Perf to format input texts like:

```
[
    {"custom_key": ["example1"]},
    {"custom_key": ["example2"]}
]
```

If you the above template is saved in `custom_template.jinja`,
you can run the command:

```
genai-perf profile \
  --model MY_MODEL \
  --endpoint-type template \
  --num-payloads 2 \
  --extra-inputs payload_template:custom_template.jinja
```

