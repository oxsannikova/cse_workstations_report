# Cisco Secure Endpoint Workstation Report using Python

This script will return the list of all computers from Cisco Secure Endpoint console, with a series of choices:
* Sort: alphabetically or by last time seen
* Filter: Group
* More Filter: Time range : Last seen, starting from 2 hours.
* Fields shown: Computer Name, Orbital Status, Last Seen, with the ability to add more fields.

# Installation

Clone the repo
```bash
git clone https://github.com/oxsannikova/cse_workstations_report.git
```
Go to your project folder
```bash
cd cisco-sdwan-python
```

Set up a Python venv. First make sure that you have Python 3 installed on your machine. We will then be using venv to create an isolated environment with only the necessary packages.

Install virtualenv via pip
```bash
pip install virtualenv
```

Create the venv
```bash
python3 -m venv venv
```

Activate your venv
```bash
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Edit `environment.py` to provide Cisco Secure Endpoint API Client ID and API Key.

## Usage

Usage examples:

```bash
python3 cse_report.py --help
```

```bash
python3 cse_report.py --group='Linux Audit' --sort='abc'
```

Supported arguments:

| Argument | Description |
|----------|-------------|
| --get_groups |  Print out group names to use in --group argument |
| --group |  Display all computers belonging to the group. Usage: --group='GROUP NAME' |
| --sort | Sort alphabetically or by last time seen. Usage: --sort='abc' or  --sort='last_seen' |
