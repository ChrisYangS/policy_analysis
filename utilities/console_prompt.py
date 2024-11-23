import logging


def print_message_and_progressing_bar(msg: str, progress: float):
    # This function is used to print a message and a progressing bar based on the progress against 100

    # Print the progressing bar
    print(
        f"\r[{'#' * int(progress/2)}{' ' * int(100/2 - int(progress/2))}] {int(progress)}%    {msg}",
        end="\n",
    )
    logging.info(
        f"\r[{'#' * int(progress/2)}{' ' * int(100/2 - int(progress/2))}] {int(progress)}%    {msg}",
    )
