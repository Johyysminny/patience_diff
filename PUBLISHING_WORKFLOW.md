# Publishing Workflow

The PyPI distribution name is `patience_diff_algo`. Its primary Python import
package is `patience_diff`; `bram_diff` remains available as a compatibility
import.

## Build and verify

1. Update the version in `setup.py`.
2. Run the tests:

   ```bash
   make test
   ```

3. Build and validate the distributions:

   ```bash
   python -m pip install build twine
   python -m build
   twine check dist/*
   ```

4. Publish the built distributions to the configured index. For PyPI, use
   GitHub Actions trusted publishing or enter a PyPI API token when prompted:

   ```bash
   twine upload dist/*
   ```

   Never put API tokens in source files, shell commands, or commit history.

## Verify installation

```bash
python -m pip install --upgrade patience_diff_algo
python -c "import patience_diff; print(patience_diff.__version__)"
```

The distribution name used by `pip` is distinct from the Python import name.
