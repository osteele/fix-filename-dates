# Fix Filename Dates

## Description

The `fix-filename-dates` utility is designed to rename files with dates in a
variety of formats to a standardized ISO date format. It is a command-line tool
developed in Python, designed to be somewhat flexible in identifying and
transforming date strings. Perfect for managing a cluttered directory of
documents, photos, or any other types of files with date information at various
locations in their names.

For example, it will rename a file with the name `Phone Bill Apr 30, 2023.pdf`
to `2023-04-30 Phone Bill.pdf`.

## Features

- Flexible date parsing that supports an extensible range of date formats
- Command-line options for dry runs and help documentation
- Built using Python, with easy installation and setup via Poetry

## Installation

Before you can use `fix-filename-dates`, you'll need to have Python and Poetry
installed. Once those prerequisites are met, you can install the tool with the
following steps:

1. Clone the repository or download the source code
2. Navigate to the project directory and run:

```bash
poetry install
```

This will install all necessary dependencies and make the `fix-filename-dates`
command available for use.

## Usage

You can rename files using the following syntax:

```bash
fix-filename-dates [OPTIONS] FILES...
```

### Options

- `--dry-run, -n`: Show what files would be renamed, without actually renaming
  them.
- `--help, -h`: Show the help message and exit.

### Examples

Run a dry run to see which files will be renamed:

```bash
fix-filename-dates --dry-run /path/to/dir
```

Actually rename the files:

```bash
fix-filename-dates /path/to/dir
```

## LICENSE

MIT License
