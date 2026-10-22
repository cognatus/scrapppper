# scrapppper

**An open-source Python toolkit for structured web content extraction, with reusable extractors, configurable parsing rules, and developer-friendly exports.**

## Project Overview

scrapppper is a Python web extraction project originally created to retrieve structured information from Instructables pages using Selenium.

The existing implementation automates browser navigation, extracts page content, and converts the results into structured JSON records.

I plan to evolve the project into a reusable Python library and command-line toolkit for developers who need configurable web content extraction.

The objective is to provide a lightweight, extensible foundation for tasks such as content migration, website structure validation, authorized data extraction, and test-data preparation.

## Target Users

- Backend developers building extraction and automation workflows
- Developers migrating content between systems
- QA engineers testing website structure
- Open-source contributors building reusable parsing tools

## Tech Stack

### Current Implementation

- Python
- Selenium WebDriver
- Headless Google Chrome
- ChromeDriver
- JSON data export

### Planned Extensions

- Modular extraction adapters
- Configurable CSS selector rules
- Command-line interface
- JSON and CSV exports
- Automated testing with synthetic HTML fixtures

## Existing Implementation

The repository contains scripts that:

- Read input URLs from JSON files
- Navigate target web pages with Selenium
- Extract titles, categories, and descriptions
- Extract individual steps and associated images
- Transform extracted information into JSON structures
- Store intermediate and final extraction results

The original implementation is specific to Instructables and depends on its historical HTML structure.

The repository also contains JSON outputs and execution logs from the original experiments.

## Project Structure

- `gettodo.py` — Browser automation and content extraction
- `scrap.py` — Additional extraction logic
- `chromedriver_linux64/` — Original browser driver files
- `*.json` — Historical inputs and extraction results
- `*.log` — Original execution logs

## Local Development

The original implementation requires Python, Selenium, Google Chrome, and a compatible ChromeDriver.

1. Clone the repository.
2. Create a virtual environment using `python -m venv .venv`.
3. Activate the environment.
4. Install Selenium using `pip install selenium`.
5. Configure a compatible ChromeDriver.
6. Review the original input files and script configuration.
7. Run `python gettodo.py`.

The scripts use legacy Selenium APIs and hard-coded paths. Updating the runtime and configuration is part of the planned modernization.

## Planned Development Roadmap

### Phase 1 — Modernization and Refactoring

- [ ] Upgrade Selenium and browser driver management.
- [ ] Replace hard-coded paths and processing offsets.
- [ ] Separate browser navigation, extraction, transformation, and exporting.
- [ ] Introduce structured logging.
- [ ] Improve exception handling and retry behavior.

### Phase 2 — Reusable Extraction Engine

- [ ] Implement a modular extractor interface.
- [ ] Add configurable CSS selector rules.
- [ ] Introduce extraction schemas and field validation.
- [ ] Support local HTML files and synthetic test fixtures.
- [ ] Add configurable extraction limits and rate controls.

### Phase 3 — Developer Tooling

- [ ] Build a command-line interface for extraction jobs.
- [ ] Add JSON and CSV export options.
- [ ] Implement batch processing.
- [ ] Introduce resumable execution.
- [ ] Add execution summaries and error reports.

### Phase 4 — Open-Source Readiness

- [ ] Implement unit tests for parsing and transformation logic.
- [ ] Add integration tests using synthetic HTML fixtures.
- [ ] Configure automated testing and CI.
- [ ] Document installation, configuration, and custom extractors.
- [ ] Publish examples covering common developer workflows.

## Current Status and Future Direction

scrapppper is an independently developed web extraction prototype that I plan to modernize and maintain as an open-source developer toolkit.

My primary goal is to transform the original site-specific scripts into a configurable Python library and CLI that developers can extend for different structured content extraction workflows.

The initial development stage will focus on isolating the extraction logic, introducing reusable components, and modernizing browser automation.

Further work will include configurable parsing rules, custom extractor interfaces, multiple export formats, resumable batch processing, and automated testing.

The original Instructables implementation will serve as the starting point for a more modular architecture.

The project provides substantial opportunities for Python development, software architecture improvements, CLI design, refactoring, and testing.

Development and testing will prioritize synthetic HTML fixtures. Existing third-party extraction outputs will be reviewed before redistribution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
