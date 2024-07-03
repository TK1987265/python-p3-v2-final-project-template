# Wrestling Management System

## Overview
This CLI application manages a database of wrestling teams and wrestlers. Users can add wrestlers, manage teams, and view all entries.

## Setup
Clone this repository and navigate to the project directory. Run `pipenv install` followed by `pipenv shell` to activate the virtual environment.

## Usage
Execute the application with `python lib/cli.py`. Follow the interactive menu to manage wrestlers and teams.

## Details
### cli.py
Serves as the entry point of the application, handling user interaction and routing actions to appropriate functions.

### helpers.py
Contains functions that execute specific tasks like adding or listing wrestlers and teams, providing modular functionality for the CLI.

### models/team.py
Defines the `Team` and `Wrestler` models, establishes the database schema, and manages the database session.
