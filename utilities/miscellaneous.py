# This is a collection of miscellaneous functions that are used in the main script.
import re


def sanitize_filename(policy_name: str) -> str:
    # Replace all non-alphanumeric characters with an underscore
    sanitized_name = re.sub(r"[^\w\s-]", "_", policy_name)
    # Replace multiple consecutive underscores, spaces, or hyphens with a single underscore
    sanitized_name = re.sub(r"[\s_-]+", "_", sanitized_name)
    # Remove leading or trailing underscores
    sanitized_name = sanitized_name.strip("_")
    return sanitized_name
