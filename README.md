# Port Scanner

A simple port scanner written in Python, with optional tor.

## Prerequisites

- Python 3.x
- PySocks (for Tor support)
- Stem (for start Tor Service)

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```
## Usage
```
python stealthscan.py -t <ip> [-a] [--tor]
-t or --target: Specify the target address.
-a or --all: Scan all ports (default is to scan well-known ports only).
--tor: Use Tor as a proxy for port scanning (requires PySocks, stem).
```
## Example
```
python stealthscan.py -t example.com -a --tor
```
## Notes
Make sure to have Tor installed for Tor proxy support.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

