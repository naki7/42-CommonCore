import importlib


def print_not_installed(not_installed_modules: list, modules: list) -> None:
    for module_name in not_installed_modules:
        print(f"{module_name}", end=" ")
    print("has not been installed.",
          "To ensure proper functionality use:\n")
    print("For pip run:\n   > pip install -r requirements.txt")
    print("\nMake sure that the requirements.txt file contains:")
    print(f"{modules}\nMake sure to add:\n{not_installed_modules}")

    print("\n\nFor poetry run:\n   > poetry install --no-root")
    print("\nMake sure that the pyproject.toml file contains:")
    print("[tool.poetry]\nname = 'ex1'\n",
          "version = '1.0.0'\n\n[tool.poetry.dependencies]\n",
          "python = '^3.10'\npandas = '2.1.0'\n",
          "numpy = '1.25.0'\nrequests = '2.31.0'\n",
          "matplotlib = '3.7.2'", sep="")
    print(f"\nMake sure to double check:\n{not_installed_modules}\n")


def check_install() -> list:
    modules: list = ["pandas", "numpy", "requests", "matplotlib"]
    modules_text: dict = {
        "pandas": "Data manipulation", "numpy": "Numerical computation",
        "requests": "Network access", "matplotlib": "Visualization"
        }
    installed_modules: list = []
    not_installed_modules: list = []
    print("Checking dependencies:\n")
    for module_name in modules:
        try:
            installed_modules.append(importlib.import_module(module_name))
        except ImportError:
            not_installed_modules.append(module_name)
    if len(not_installed_modules) > 0:
        print_not_installed(not_installed_modules, modules)

    i: int = 0
    for module in modules:
        if not_installed_modules.count(module) == 1:
            print(f"[KO] {module} - Install required")
        else:
            print(f"[OK] {module}",
                  f"({installed_modules[i].__version__})",
                  f" - {modules_text[module]} ready", sep="")
            i += 1

    return installed_modules


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    installed_modules: list = check_install()
    if len(installed_modules) < 4:
        print("\nAnalysis not possible!")
        return
    for module in installed_modules:
        if module.__name__ == "numpy":
            nump = module
        elif module.__name__ == "pandas":
            pand = module
        elif module.__name__ == "matplotlib":
            matplot = importlib.import_module("matplotlib.pyplot")
    if not all([pand, nump, matplot]):
        print("\nAnalysis not possible!")
        return

    print("\nAnalyzing Matrix data...")
    time = nump.arange(0, 1000)
    values = nump.cumsum(time)

    print("Processing 1000 data points...")
    frame: dict = {
        "time": time,
        "values": values
    }

    print("Generating visualization...")
    png_name: str = "matrix_analysis.png"
    matplot.plot(frame["values"], frame["time"])
    matplot.title("Matrix Cummulative Graph")
    matplot.xlabel("time but if time was added to its previous time")
    matplot.ylabel("time")
    matplot.savefig(png_name)

    print("\nAnalysis complete!")
    print(f"Results saved to: {png_name}")


if __name__ == "__main__":
    main()
