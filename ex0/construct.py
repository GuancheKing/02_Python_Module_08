import sys
import os
import site


def detect_virtual_env() -> bool:
    """Return True if a virtual environment is currently active."""

    virtual_env = os.environ.get("VIRTUAL_ENV")
    if virtual_env:
        return True
    return False


def print_inside_env() -> None:
    """Print details about the active virtual environment."""

    path = os.environ.get("VIRTUAL_ENV")
    assert path is not None
    name = os.path.basename(path)
    package_paths = site.getsitepackages()

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {name}")
    print(f"Environment Path: {path}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting "
          "the global system.")
    print(f"\nPackage installation path:\n{package_paths[0]}")


def print_outside_env() -> None:
    """Display a warning when no virtual environment is active."""

    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print("\nThen run this program again.")


def main() -> None:
    """Run the construct checker."""

    if detect_virtual_env():
        print_inside_env()
    else:
        print_outside_env()


if __name__ == "__main__":
    main()
