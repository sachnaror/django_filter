import curses
import os
import re


def list_files(directory):
    """List all Python files in the directory and its subdirectories."""
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                files_list.append(os.path.join(root, file))
    return files_list


def remove_comments_and_docstrings(file_path):
    """Remove comments and docstrings from the given Python file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    new_lines = []
    in_string = False
    for line in lines:
        if '"""' in line:
            in_string = not in_string
        if not in_string:
            line = re.sub(r'^\s*#.*', '', line)
        new_lines.append(line)
    with open(file_path, 'w') as file:
        file.writelines(new_lines)


def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    max_rows, max_cols = stdscr.getmaxyx()

    files = list_files(os.getcwd())
    selected_row = 0
    file_page = files[selected_row:selected_row +
                      max_rows-3]  # Adjust for window size

    while True:
        stdscr.clear()
        stdscr.addstr(
            "Use arrow keys to navigate and press Enter to select a file.\n")
        for idx, filename in enumerate(file_page):
            if idx >= max_rows - 2:  # Prevent writing outside the window
                break
            display_filename = f"{'> ' if idx == selected_row else '  '}{
                filename[:max_cols-3]}..." if len(filename) > max_cols-3 else filename
            stdscr.addstr(display_filename + "\n")
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and selected_row > 0:
            selected_row -= 1
            if selected_row < len(file_page) // 2 and selected_row > 0:
                file_page = files[selected_row:selected_row+max_rows-3]
        elif key == curses.KEY_DOWN and selected_row < len(files) - 1:
            selected_row += 1
            if selected_row >= len(file_page) // 2:
                file_page = files[selected_row:selected_row+max_rows-3]
        elif key == curses.KEY_ENTER or key in [10, 13]:
            remove_comments_and_docstrings(files[selected_row])
            break

    stdscr.addstr(f"Comments and docstrings removed from {
                  files[selected_row]}\n")
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
