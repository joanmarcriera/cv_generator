# CV Generator

This repository contains a simple Python script for creating a curriculum vitae (CV) from a JSON file. The script generates a `.docx` document using the [python-docx](https://python-docx.readthedocs.io/) library. The JSON file holds all the personal information, professional summary, skills and work history that will appear in the final CV.

## Current Workflow

1. Edit `cv_content.json` with your personal details.
2. Run `python cv_generator.py -o Joan_Marc_Riera_CV.docx` to create your CV.

The script sets up page margins and basic styles, then writes the contents of `cv_content.json` to the document. Only the fields present in the JSON file are used.

## Getting Started

It is recommended to work inside a virtual environment so dependencies do not
pollute your system installation. Create and activate one with:

```bash
python -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install python-docx docxtpl pytest
```

## Running tests

Unit tests use `pytest`. Install dependencies and run tests with:

```bash
pip install python-docx docxtpl pytest
pytest
```
## Usage

After populating `cv_content.json` with your CV details, generate a CV with:

```bash
python cv_generator.py -i cv_content.json -o My_CV.docx
```

You can also specify a DOCX template using `-t TEMPLATE.docx`.

## Suggested Improvements

The goal of the project is to quickly tailor CVs and cover letters for specific companies. The script now provides a basic command line interface but could be further extended with features such as:

* **Templating** – Allow multiple docx templates or sections to be assembled depending on the target company. This enables focused CVs with relevant skills and experience highlighted.
* **Cover Letter Generation** – Add support for a cover letter template. The script could read a different JSON file or template fields to populate with company‑specific details (job title, contact person, etc.).
* **Command Line Arguments** – Accept arguments for the output file name, selected template, or a path to a custom JSON file. This avoids hard‑coding values within the script.
* **Configuration File or CLI** – Provide a simple configuration file or command line interface that prompts the user for key details. This would make it easier for non‑developers to create targeted CVs and letters.

These changes would help transform the script from a single hard‑coded workflow into a small tool for generating CVs and cover letters tailored to different roles.


