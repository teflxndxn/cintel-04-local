# cintel-04-local

## Project Overview

This project is part of Module 4 (CC4.1: Orient and Engage) focused on transitioning from browser-based to local Python development for PyShiny apps.  
The goal is to set up Python, Git, and development tools on my machine to build and run interactive dashboards locally.

## Project Structure

- `app.py`: Main PyShiny app file  
- `requirements.txt`: List of Python packages needed  
- `.gitignore`: Files and folders to ignore in Git  
- `README.md`: This documentation

## Python Installation and Setup

I installed Python 3.12.1 on my macOS machine using the official installer from python.org.  
During installation, I ran the `Install Certificates.command` as instructed.

To ensure my terminal uses the official Python instead of Anaconda, I updated my PATH by adding:

```bash
export PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin:$PATH"
```
After updating the PATH and restarting my terminal, I verified the Python and pip versions with the following commands:
```bash
which python3
python3 --version
python3 -m pip --version
```
Output:
```bash
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
Python 3.12.1
pip 23.2.1 from /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pip (python 3.12)
```
## Local Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/teflxndxn/cintel-04-local.git
   cd cintel-04-local

Create and activate the virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:
python3 -m pip install --upgrade pip setuptools
python3 -m pip install -r requirements.txt

Run the app:
python3 app.py
