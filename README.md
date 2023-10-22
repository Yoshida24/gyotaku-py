# gyotaku-py

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Yoshida24/gyotaku-py)

Lets take "Gyotaku" !

## What does this tool do?

- A tool to save full-size captures of web pages, and HTML snapshots.
- You can write browser macros in Gherkin format that closely resemble natural language.

## Getting Started

### Install on Ubuntu Server
First of all, `update` apt and `pip`

```bash
apt update && apt upgrade -y && apt autoremove -y && apt autoclean -y
pip install --upgrade pip
```

install VSCode recommended extensions. This includes Linter, Formatter, and so on. Recommendation settings is written on `.vscode/extensions.json`.

Then, install dependencies:

```bash
make setup
```

Then edit `.env` file.

```.env
# Your project path, or specific directory.
SNAPSHOTS_PARENT_PATH=/path/to/gyotaku-py
```

Now you can run script:

```bash
make run
```

Success is indicated when [cucumber](https://cucumber.io/) official page captures and HTML snapshots are created under the file specified in `SNAPSHOTS_PARENT_PATH`.
- Sample screenshot: [snapshots/sample/captures](snapshots/sample/captures/2023_10_22_13_21_00.png)
- Sample HTML snapshot: [snapshots/sample/html](snapshots/sample/html/2023_10_22_13_21_00.html)

## Use Cases

### Taking Gyotaku
Get Captures like below:
- Sample screenshot: [snapshots/sample/captures](snapshots/sample/captures/2023_10_22_13_21_00.png)
- Sample HTML snapshot: [snapshots/sample/html](snapshots/sample/html/2023_10_22_13_21_00.html)

Create a browser macro in `src/features/my_gyotaku.feature` in Gherkin format.

```my_gyotaku.feature
Feature: Take Gyotaku of cucumber.io TOP Page

  Scenario: Opening example.com and taking a screenshot after clicking a button
    Given I open "https://cucumber.io/"
    Then I wait for 3 seconds
    Then I click the ".btn[href="/docs/installation/"]"
    Then I wait for 3 seconds
    Then I save a capture to "sample/captures"
    Then I save a HTML snapshot to "sample/html"
    Then end
```

> **Note**.
> Check the available instructions in `src/features/steps/navigater.py`.

You can take "Gyotaku" by executing `behave src/features/my_gyotaku.feature`.
Multiple files can be placed.

### Take Gyotaku periodically.
Set up `crontab -e`.

```bash
* * * * * cd /path/to/gyotaku-py && . .venv/bin/activate && set -a && . ./.env && set +a && behave src/features/scheduled_gyotaku.feature
```

## Usage

depends on:
- Python: 3.11.2
- pip: 22.3.1
- GNU Make: 3.81

included
- Lint and Format
- Task runner

supported platform:
- M1 Macbook Air Ventura 13.4.1
- Ubuntu 22.04.3 on Raspberry Pi 4 Model B Rev 1.2 (2GB)
