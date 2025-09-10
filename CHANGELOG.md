# Changelog

All notable changes to this project will be documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
the project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-09-10
### Added
- Initial production-ready release of **Plasma Toolkit**.
- Modular Python package with:
  - Paschen law, Meek–Raether streamer, and A/B back-calculation.
  - γ-bands and Ncrit bands.
  - I/O utilities for CSVs and Townsend parameters.
  - Plotting utilities for Paschen/Streamer overlays.
- Command-line interface (`scripts/plasma_cli.py`) for automatic figure generation.
- Data templates for Air, Argon, Helium, Nitrogen, CO₂.
- Golden regression dataset for numerical validation.
- Sanity + regression tests (pytest).
- Documentation:
  - Sphinx (HTML + PDF).
  - nbsphinx integration for Jupyter Notebooks.
- Examples:
  - Paschen curve for Air (γ sweep).
  - Multigas overlays.
  - Air Paschen vs Streamer (Ncrit band).
  - Dataset overlay with experimental CSVs.
- GitHub Actions workflows:
  - CI (pytest).
  - Lint (ruff, black, mypy).
  - Docs (HTML + PDF build, GitHub Pages deploy).
  - Publish to PyPI/TestPyPI.
- Developer tools:
  - `pyproject.toml` with ruff/black/mypy configs.
  - Pre-commit hooks.
- License: MIT.
- README with badges (CI, Lint, Docs, PyPI, Downloads, License).

[1.0.0]: https://github.com/Tsoympet/plasma-toolkit/releases/tag/v1.0.0
