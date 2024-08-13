import subprocess
import sys
import os

def check_tkinter():
    try:
        import tkinter  # For Python 3
        return True
    except ImportError:
        return False

def install_tkinter():
    try:
        # Install Tkinter using the system package manager
        subprocess.check_call(['sudo', 'apt-get', 'update'])
        subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'python3-tk'])
        print("Tkinter installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing Tkinter: {e}")

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f"Package '{package_name}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing package '{package_name}': {e}")

def check_and_install_requirements(requirements_file):
    with open(requirements_file, 'r') as file:
        for line in file:
            package = line.strip()
            if package and not package.startswith('#'):
                try:
                    __import__(package.split('==')[0])  # Check if the package is already installed
                    print(f"{package} is already installed")
                except ImportError:
                    print(f"Package '{package}' is not installed.")
                    install_package(package)

def checkninstall():
    # Check and install Tkinter
    if sys.platform.startswith('linux'):
        if not check_tkinter():
            print("Tkinter is not installed.")
            install_tkinter()
        else:
            print("Tkinter is already installed.")
    
    # Check and install packages from requirements.txt
    requirements_file = 'requirements.txt'
    if os.path.isfile(requirements_file):
        print("Checking and installing packages from requirements.txt...")
        check_and_install_requirements(requirements_file)
    else:
        print(f"{requirements_file} not found.")

if __name__ == "__main__":
    checkninstall()
