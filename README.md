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

## PyShiny Penguins Dashboard Setup & Run Guide

### 1. Create and activate the virtual environment

**Mac/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate

2. Install required packages
Make sure you have a requirements.txt file with all necessary packages. Then run:
pip install -r requirements.txt

3. Run the Shiny app
shiny run --reload --launch-browser penguins/app.py

4. Recommended VS Code Extension for Shiny
Install the Shiny for Python extension for better integration:

Open the Extensions pane in VS Code (Cmd+Shift+X or Ctrl+Shift+X)
Search for Shiny for Python
Click Install
This extension helps you run and debug PyShiny apps directly inside VS Code.

5. Project folder structure
cintel-04-local/
├── .venv/
├── penguins/
│   └── app.py
├── requirements.txt
└── README.md
```
# Module 4: PyShiny App – Penguins Dataset

This project is a PyShiny web application built using the [Palmer Penguins dataset](https://allisonhorst.github.io/palmerpenguins/). It allows users to interactively explore penguin species data using filters and visualizations.

## 📊 Features

- Interactive charts with `Plotly` and `Matplotlib`
- Filters based on penguin species
- Reactive calculations using `@reactive.calc`
- Exported with `shinylive` for easy deployment

## Live App

Click the link below to view the live version of this app (hosted via GitHub Pages):

**[Live App on GitHub Pages]( https://teflxndxn.github.io/cintel-04-local/)**

##  Project Structure
cintel-04-local/
├── app.py # Main PyShiny application file
├── docs/ # Exported static app (for GitHub Pages)
│ ├── index.html
│ └── ...other files
├── .gitignore
├── README.md
└── requirements.txt

## 🛠️ How to Run Locally

1. Clone the repo  
2. Create a virtual environment  
3. Install dependencies  
4. Run the app with Shiny

```bash
git clone https://github.com/teflxndxn/cintel-04-local.git
cd cintel-04-local
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
shiny run --reload --launch-browser app.py


