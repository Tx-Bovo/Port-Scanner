# Port Scanner

A simple port scanner written in Python, with optional tor.

## Prerequisites

- Python 3.x
- PySocks (for Tor support)

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```
## Usage
```
python stealthscan.py -t <ip> [-a] [--tor-scanner]
-t or --target: Specify the target address.
-a or --all: Scan all ports (default is to scan well-known ports only).
--tor-scanner: Use Tor as a proxy for port scanning (requires PySocks).
```
## Example
```
python stealthscan.py -t 192.168.1.1 -a --tor-scanner
```
## Notes
Make sure to have Tor installed and running locally for Tor proxy support.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

