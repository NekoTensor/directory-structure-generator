import os
import subprocess
import requests

def create_directory_structure(base_path, directory_structure):
    """
    Create directories and files based on the given directory structure.
    
    Args:
    - base_path (str): The base path where the directory structure will be created.
    - directory_structure (dict): Dictionary representing the directory structure.
    """
    for name, content in directory_structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_directory_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                file_path = os.path.join(path, file)
                open(file_path, 'w').close()
        else:
            open(path, 'w').close()

def generate_directory_tree(directory, prefix=''):
    """
    Generate and print the directory tree recursively.
    
    Args:
    - directory (str): Root directory path.
    - prefix (str): Prefix for the directory tree lines.
    """
    print(prefix + '+-- ' + os.path.basename(directory) + '/')
    prefix += '|   '
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        subindent = ' ' * 4 * (level + 1)
        for d in dirs:
            print('{}|-- {}/'.format(indent, d))
        for f in files:
            print('{}|-- {}'.format(indent, f))
        break  # prevent further recursion for the current directory

def initialize_git_repo_and_push_to_github(local_path, repo_name, github_token):
    """
    Initialize a git repository and push it to GitHub.
    
    Args:
    - local_path (str): The local directory path.
    - repo_name (str): The name of the GitHub repository.
    - github_token (str): The GitHub token for authentication.
    """
    os.chdir(local_path)
    
    # Initialize git repository
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])
    
    # Creates a Github Repository
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'name': repo_name,
        'private': False
    }
    response = requests.post('https://api.github.com/user/repos', json=data, headers=headers)
    response.raise_for_status()
    repo_url = response.json()['clone_url']
    
    # Push to GitHub
    subprocess.run(['git', 'remote', 'add', 'origin', repo_url])
    subprocess.run(['git', 'push', '-u', 'origin', 'master'])

def main():
    # Below is just an example for the structure of the directory. Enter your desired directory structure.
    directory_structure = {
    'directory-structure-generator': {
        'src': ['generate_structure.py'],
        'README.md': '',
        '.gitignore': '',
        'requirements.txt': ''
    }
}

    
    # Prompts the user to enter the path, repo name
    base_path = input("Enter the path where you want to create the directory: ")
    full_path = os.path.join(base_path, 'Enter the desired name of the repository')
    
    # Create directories and files
    create_directory_structure(full_path, directory_structure)
    
    # Generate and print the directory tree
    generate_directory_tree(full_path)
    
    # Ask the user for GitHub credentials
    repo_name = input("Enter the GitHub repository name: ")
    github_token = input("Enter your GitHub token: ")   #The process of getting github token will be in the readme section..
    
    # Initializes git repo and pushes to GitHub
    initialize_git_repo_and_push_to_github(full_path, repo_name, github_token)

if __name__ == '__main__':
    main()
