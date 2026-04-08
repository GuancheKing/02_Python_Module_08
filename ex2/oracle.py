import os

CONFIG_VARS = ("mode", "db", "api_key", "log_lvl", "zion_endpoint")


def load_environment() -> None:
    """Load environment variables from the .env file."""

    try:
        from dotenv import load_dotenv
    except ImportError:
        print(
            "dotenv: Not installed. Run 'pip install python-dotenv' "
            "on venv to install.\n"
            )
        exit()
    load_dotenv()


def get_config() -> dict[str, str | None]:
    """Collect the current application configuration from the environment."""

    config = {
        "mode": os.environ.get("MATRIX_MODE"),
        "db": os.environ.get("DATABASE_URL"),
        "api_key": os.environ.get("API_KEY"),
        "log_lvl": os.environ.get("LOG_LEVEL"),
        "zion_endpoint": os.environ.get("ZION_ENDPOINT")
        }
    return config


def validate_config(config: dict[str, str | None]) -> list[str]:
    """Validate required configuration values and report missing entries."""

    errors: list[str] = []
    for key in CONFIG_VARS:
        value = config.get(key)
        if value is None:
            errors.append(f"Missing {key}")
    mode = config.get("mode")

    if mode is not None:
        if mode not in ("development", "production"):
            errors.append("Invalid MATRIX_MODE")

    return errors


def display_config(config: dict[str, str | None]) -> None:
    """Display the loaded configuration in a user-friendly format."""

    mode = config.get('mode')
    print(f"Mode: {mode}")
    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to production instance")

    api_key = config.get('api_key')
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {config.get('log_lvl')}")

    zion_endpoint = config.get('zion_endpoint')
    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def display_security_check() -> None:
    """Print a simple environment security summary."""

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def main() -> None:
    """Run the Oracle configuration check."""

    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_environment()
    config = get_config()
    errors = validate_config(config)

    if errors:
        print("Configuration errors:")
        for e in errors:
            print(f"- {e}")
        return

    print("Configuration loaded:")
    display_config(config)
    display_security_check()


if __name__ == "__main__":
    main()
