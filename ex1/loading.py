import importlib
from importlib.metadata import version


PACKAGE_DESCRIPTIONS = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computation",
            "matplotlib": "Visualization",
            "requests": "Network access"
            }

def package_exists(dependency: str) -> bool:

    spec = importlib.util.find_spec(dependency)
    return spec is not None


def get_package_version(dependency: str) -> str:

    return version(dependency)


def format_package_status(dependency: str) -> str:

    if package_exists(dependency):
        v = get_package_version(dependency)
        description: str | None = PACKAGE_DESCRIPTIONS.get(dependency)
        return f"[OK] {dependency} ({v}) - {description} ready"
    else:
        return (f"[ERROR] {dependency} - not installed")


def print_install_instructions() -> None:

    print("\nInstall with pip: 'pip install -r requirements.txt'")
    print("\nInstall with Poetry: 'poetry install'")


def check_dependencies() -> bool:

    packages: list[str] = ['numpy', 'pandas', 'matplotlib', "requests"]


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")


if __name__ == "__main__":
    main()
