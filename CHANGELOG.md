# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [1.0.2] - 2026-07-27

### Changed
- Ignore the local `Broadlink RM Codes Gists` symlink in `.gitignore`.

## [1.0.1] - 2026-07-26

### Added
- LICENSE and CHANGELOG.

### Changed
- Moved the per-script docs under a Usage subsection in the README.

## [1.0.0] - 2026-07-26

### Added
- Interactive `learn_ir_codes.py` for learning IR remote button codes one at a time.
- Interactive `learn_rf_codes.py` for learning RF codes, with a frequency prompt.
- Interactive `learn_rf_dim_levels.py` for learning RF dimmer levels, with a dim-level-count prompt.
- Shared `broadlink_helpers.py` for connecting to and learning from a Broadlink RM4 Pro.
