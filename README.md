# Directory Structure Generator

![Directory Structure Generator](https://i.imgur.com/K2UXKKj.png)

## Overview

The Directory Structure Generator is a Python script designed to automate the creation of a predefined directory structure for new projects and seamlessly initialize them as GitHub repositories. This tool aims to simplify the initial setup process for developers by eliminating manual directory creation and repository initialization steps.

## Features

Effortless Directory Setup: Define and create nested directories and files instantly.

Automated Git Initialization: Quickly initialize Git repositories for seamless version control.

One-Click GitHub Integration: Push your project structure to GitHub with ease for immediate collaboration.

## Usage

To use the python script, follow these steps:

1. Clone the repository or download the script.
2. Install the required Python packages.
3. Run the script and follow the prompts.

## Installation

### Prerequisites

Python 3.x: Ensure Python 3.x is installed on your system.
Git: Make sure Git is installed and configured on your machine.
GitHub Account: Sign up for a GitHub account if you haven't already.

### Step-by-Step Guide

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/NekoTensor/directory-structure-generator.git
    cd directory-structure-generator
    ```

2. **Install the Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Script:**

    ```bash
    python src/generate_structure.py
    ```

4. **Follow the Prompts:**

    - Enter the path where you want to create the directory.
    - Enter the GitHub repository name.
    - Enter your GitHub token.

## Obtaining a GitHub Token


To push your repository to GitHub, you'll need a GitHub token. Here are the steps to generate and use it:

1. **Navigate to your GitHub account settings, then click on Developer settings.**

2. **Click on the "Personal access tokens" menu, then select "Generate new token".**

   ![Generate New Token](https://i.imgur.com/Uxsz1Lx.jpeg)


3. **Select `repo` as the scope. This token will grant access for all specified actions within your repositories.**

   ![Select Scope](https://i.imgur.com/Le0UXWx.jpeg)


4. **Click "Generate Token". GitHub will display the personal access token only once. Copy the token and store it securely.**

   ![Generate and Copy Token](https://i.imgur.com/xrym95i.jpeg)



This token is essential for authentication in the script to automate repository creation and updates on GitHub.


## Example Directory Structure

You can define your desired directory structure in the script. For example:

```python
directory_structure = {
    'your_project_name': {
        'src': ['main.py'],
        'data': {
            'input': [],
            'output': []
        },
        'docs': {
            'README.md': '',
            'documentation.pdf': ''
        },
        'README.md': '',
        '.gitignore': ''
    }
}
## Collaboration

Contributions are welcome! Here's how you can contribute to this project:

1. **Fork** the repository on GitHub.
2. **Clone** the forked repository to your local machine
   ```bash
   git clone https://github.com/your-username/directory-structure-generator.git
   cd directory-structure-generator
