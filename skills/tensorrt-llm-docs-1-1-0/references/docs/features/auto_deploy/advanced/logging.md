Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/features/auto_deploy/advanced/logging.md

* Logging Level

# Logging Level[#](#logging-level "Link to this heading")

Use the following env variable to specify the logging level of our built-in logger, ordered by
decreasing verbosity;

```
AUTO_DEPLOY_LOG_LEVEL=DEBUG
AUTO_DEPLOY_LOG_LEVEL=INFO
AUTO_DEPLOY_LOG_LEVEL=WARNING
AUTO_DEPLOY_LOG_LEVEL=ERROR
AUTO_DEPLOY_LOG_LEVEL=INTERNAL_ERROR
```

The default log level is `INFO`.