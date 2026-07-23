# DataConverter

`DataConverter` is a small Python command-line tool for converting autonomous vehicle test data between `JSON`, `YAML`, and `CSV`.

The current implementation reads input files from [`input/`](/home/adelelakour/DataConverter/input), validates the test records, and writes the converted result to [`output/`](/home/adelelakour/DataConverter/output).

## Current Features

- Read `JSON`, `YAML`, and `CSV`
- Write `JSON`, `YAML`, and `CSV`
- Validate record schema before writing output
- Validate basic field types
- Restrict `status` to `Passed` or `Failed`

## Project Structure

```text
DataConverter/
├── converter.py      # CLI entry point
├── parsers.py        # Input readers
├── writers.py        # Output writers
├── validator.py      # Schema and type validation
├── transformer.py    # Early transformation helper
├── input/            # Sample source files
└── output/           # Generated files
```

## Requirements

- Python 3
- `PyYAML`

Install the YAML dependency with:

```bash
pip install pyyaml
```

## Usage

Run the converter from the repository root:

```bash
python3 converter.py <input-file> <output-file>
```

Example:

```bash
python3 converter.py data.json converted.yaml
python3 converter.py data.csv converted.json
python3 converter.py data.yaml converted.csv
```

The program expects:

- the source file to exist under [`input/`](/home/adelelakour/DataConverter/input)
- the destination file name to be written under [`output/`](/home/adelelakour/DataConverter/output)

For example, `python3 converter.py data.json converted.yaml` reads `input/data.json` and writes `output/converted.yaml`.

## Expected Data Shape

For `JSON` and `YAML`, the tool expects a top-level object like:

```json
{
  "project": "Autonomous Vehicle Validation",
  "version": "1.0",
  "generated_at": "2026-07-23T14:30:00Z",
  "tests": [
    {
      "id": 1001,
      "name": "Emergency Braking",
      "category": "Safety",
      "status": "Passed",
      "priority": "Critical",
      "duration": 2.8,
      "vehicle": "Car-A",
      "environment": "Simulation",
      "temperature": 24,
      "executed_by": "CI",
      "timestamp": "2026-07-22T09:15:00Z"
    }
  ]
}
```

For `CSV`, each row represents one test record using these columns:

```text
id,name,category,status,priority,duration,vehicle,environment,temperature,executed_by,timestamp
```

When reading CSV, the current implementation fills metadata with:

- `project: "Unknown"`
- `version: "Unknown"`
- `generated_at: null`

## Validation Rules

Each test must include these fields:

- `id`
- `name`
- `category`
- `status`
- `priority`
- `duration`
- `vehicle`
- `environment`
- `temperature`
- `executed_by`
- `timestamp`

Current validation checks:

- `id` must be an integer and non-negative
- `duration` must be numeric and non-negative
- `temperature` must be numeric
- most remaining fields must be strings
- `status` must be either `Passed` or `Failed`

If validation fails, the program prints an error message and stops without writing the converted file.

## Notes And Limitations

- Input and output directories are hardcoded in `converter.py`
- There is no argument parsing or help output yet
- Unsupported file extensions are not handled explicitly
- `statistics.py` and `utils.py` are present but currently empty
- `transformer.py` exists but is not wired into the CLI flow
- The `tests/` directory exists, but there are no test files yet

## Next Improvements

- Add automated tests
- Add a `requirements.txt` or `pyproject.toml`
- Improve CLI argument validation and usage help
- Support custom input and output paths
- Add transformation and filtering options
