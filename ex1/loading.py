import importlib
from typing import Any
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
        description: str = PACKAGE_DESCRIPTIONS.get(dependency, "Package")
        return f"[OK] {dependency} ({v}) - {description} ready"
    else:
        return (f"[ERROR] {dependency} - not installed")


def print_install_instructions() -> None:

    print("\nInstall with pip: 'pip install -r requirements.txt'")
    print("Install with Poetry: 'poetry install'")


def check_dependencies() -> bool:

    packages: list[str] = ['numpy', 'pandas', 'matplotlib', "requests"]
    missing: list[str] = []
    for package in packages:
        print(format_package_status(package))
        if not package_exists(package):
            missing.append(package)
    if missing:
        print_install_instructions()
        return False
    return True


def generate_matrix_data() -> tuple[Any, Any]:
    import numpy as np

    time = np.linspace(1200, 1800, 100)
    energy = np.sin(time * 0.01) + np.random.rand(100)
    return time, energy


def build_dataframe(time: Any, energy: Any) -> Any:
    import pandas as pd

    df = pd.DataFrame({
        "time": time,
        "energy": energy
    })
    return df


def generate_visualization(df: Any) -> None:
    import matplotlib.pyplot as plt

    plt.plot(df["time"], df["energy"])
    plt.title("Matrix Energy Analysis")
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.savefig("matrix_analysis.png")


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    if not check_dependencies():
        return
    print("\nAnalyzing Matrix data...")
    time, energy = generate_matrix_data()
    print("Processing 1000 data points...")
    df = build_dataframe(time, energy)
    print("Generating visualization...")
    generate_visualization(df)
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")



if __name__ == "__main__":
    main()
