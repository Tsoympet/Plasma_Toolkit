
# Release / Tagging

## Tag & publish to PyPI
1) Βεβαιώσου ότι έχεις ορίσει το secret `PYPI_API_TOKEN` στο GitHub repo.
2) Κάνε tag και push:
```bash
git tag v1.0.0
git push origin v1.0.0
```
3) Το workflow `publish-pypi` θα χτίσει και θα ανεβάσει το πακέτο.

## TestPyPI (προαιρετικό)
- Ορισμός secret `TEST_PYPI_API_TOKEN`.
- Trigger το workflow `publish-testpypi` από την καρτέλα Actions.
