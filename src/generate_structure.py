import os
import subprocess
import requests

def create_directory_structure(base_path, directory_structure):
    """
    Create directories and files based on the given directory structure.
    
    Args:
        base_path (str): The base path where the directory structure will be created.
        directory_structure (dict): Dictionary representing the directory structure.
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
                # Create an empty file
                open(file_path, 'w').close()
        else:
            # If content is an empty string, create an empty file
            open(path, 'w').close()

def generate_directory_tree(directory, prefix=''):
    """
    Generate and print the directory tree recursively.
    
    Args:
        directory (str): Root directory path.
        prefix (str): Prefix for the directory tree lines.
    """
    print(prefix + '+-- ' + os.path.basename(directory) + '/')
    new_prefix = prefix + '    '
    # Walk the directory recursively and print each file/folder
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * level
        for d in dirs:
            print('{}+-- {}/'.format(indent, d))
        for f in files:
            print('{}+-- {}'.format(indent, f))
        # Remove break to print full directory tree
        # break

def initialize_git_repo_and_push_to_github(local_path, repo_name, github_token):
    """
    Initialize a git repository and push it to GitHub.
    
    Args:
        local_path (str): The local directory path.
        repo_name (str): The name of the GitHub repository.
        github_token (str): The GitHub token for authentication.
    """
    try:
        os.chdir(local_path)
        
        # Initialize git repository on branch 'main'
        subprocess.run(['git', 'init', '-b', 'main'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)
        
        # Create a GitHub repository using the GitHub API
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
        repo_url = response.json().get('clone_url')
        if not repo_url:
            raise ValueError("Failed to create GitHub repository. Response: " + str(response.json()))
        
        # Add remote and push to GitHub using branch 'main'
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
    except Exception as e:
        print(f"Error during Git initialization or push: {e}")

def main():
    # Define the directory structure as a flat structure (files at repo root)
    directory_structure = {
        'src': ['generate_structure.py'],
        'README.md': '',
        '.gitignore': '',
        'requirements.txt': ''
    }

    base_path = input("Enter the path where you want to create the directory: ").strip()
    repo_name = input("Enter the desired name of the repository: ").strip()
    full_path = os.path.join(base_path, repo_name)
    
    try:
        # Create the directory structure at the specified location.
        create_directory_structure(full_path, directory_structure)
    except Exception as e:
        print(f"Error creating directory structure: {e}")
        return
    
    try:
        # Generate and print the directory tree.
        generate_directory_tree(full_path)
    except Exception as e:
        print(f"Error generating directory tree: {e}")
        return
    
    # Get GitHub token from the user.
    github_token = input("Enter your GitHub token: ").strip()
    
    try:
        # Initialize the git repository and push it to GitHub.
        initialize_git_repo_and_push_to_github(full_path, repo_name, github_token)
    except Exception as e:
        print(f"Error initializing git repo or pushing to GitHub: {e}")

if __name__ == '__main__':
    main()
