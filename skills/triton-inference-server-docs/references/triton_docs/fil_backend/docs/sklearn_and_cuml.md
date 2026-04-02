* Scikit-Learn...

# Scikit-Learn and cuML Support[#](#scikit-learn-and-cuml-support "Link to this heading")

**NOTE:** Due to a change in Scikit-Learn 1.2.0, forest models from version
1.2.0 and later are not currently supported. Support will be added in an
upcoming release of Triton.

## Model Serialization[#](#model-serialization "Link to this heading")

While LightGBM and XGBoost have their own serialization formats that are
directly supported by the Triton FIL backend, tree models trained with
[Scikit-Learn](https://scikit-learn.org/stable/modules/model_persistence.md)
or [cuML](https://docs.rapids.ai/api/cuml/stable/pickling_cuml_models.md) are
generally serialized using Pythonâs
[pickle](https://docs.python.org/3/library/pickle.md) module. In order to
avoid a round-trip through Python in Triton, the FIL backend instead requires
that these pickled models first be converted to Treeliteâs binary checkpoint
format. Note that this also allows you to make use of *any* Treelite-supported
model framework in Triton simply by exporting to the binary checkpoint format.

The FIL backend repo includes scripts for easy conversion from
pickle-serialized cuML or Scikit-Learn models to Treelite checkpoints. You can
download the relevant script for Scikit-Learn
[here](https://raw.githubusercontent.com/triton-inference-server/fil_backend/main/scripts/convert_sklearn.py)
and for cuML
[here](https://raw.githubusercontent.com/triton-inference-server/fil_backend/main/scripts/convert_cuml.py).

## Prerequisites[#](#prerequisites "Link to this heading")

To use the Scikit-Learn conversion script, you must run it from within a Python
environment containing both
[Scikit-Learn](https://scikit-learn.org/stable/install.md) and
[Treelite](https://treelite.readthedocs.io/en/latest/install.md). To use the
cuML conversion script, you must run it from within a Python environment
containing [cuML](https://rapids.ai/start.md).

For convenience, a conda environment config file
[is provided](https://raw.githubusercontent.com/triton-inference-server/fil_backend/main/scripts/environment.yml)
which will install all three of these prerequisites:

```
conda env create -f scripts/environment.yml
conda activate triton_scripts
```

## Converting to Treelite checkpoints[#](#converting-to-treelite-checkpoints "Link to this heading")

**NOTE:** The following steps are **not** necessary for LightGBM or XGBoost
models. The FIL backend supports the native serialization formats for these
frameworks directly.

If you already have a Scikit-Learn or cuML RF model saved as a pickle file
(`model.pkl`), place it in a directory structure as follows:

```
model_repository/
`-- fil
    |-- 1
    |   `-- model.pkl
    `-- config.pbtxt
```

Then perform the conversion by running either:

```
./convert_sklearn.py model_repository/fil/1/model.pkl
```

for Scikit-Learn models or

```
./convert_cuml.py model_repository/fil/1/model.pkl
```

for cuML models. This will generate a `checkpoint.tl` file in the model
repository in the necessary location. You can then proceed as with any other
model type, setting the `model_type` parameter in `config.pbtxt` to
`"treelite_checkpoint"`.

Note that Treelite did not guarantee compatibility between minor release
versions for its binary checkpoint model until version 3.0.0 and does not
guarantee compatibility between major releases, so it is recommended that you
keep the original pickle file. If you later make use of a newer version of
Treelite, you can simple re-run the conversion on this pickle file.

