# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: CleanRoutine
import sys

class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'

    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Special
    BG_ON_BLACK = '\033[48;5;0m'
    FG_ON_BLACK = '\033[38;5;0m'
    BG_ON_WHITE = '\033[48;5;156m'
    FG_ON_WHITE = '\033[38;5;156m'

    # ANSI escape code to disable color
    DISABLE = '\033[0m'

    @staticmethod
    def disable():
        """Disable color support."""
        print(Color.RESET, end='')
        Color.enabled = False

    @staticmethod
    def enable():
        """Enable color support."""
        Color.enabled = True

    @staticmethod
    def is_enabled():
        """Check if color is enabled."""
        return Color.enabled

    @staticmethod
    def print(*args, **kwargs):
        """Print with color support."""
        if Color.enabled:
            print(*args, **kwargs)
        else:
            print(*args, **kwargs)

    @staticmethod
    def print_success(msg):
        """Print success message in green."""
        Color.print(f'{Color.GREEN}{msg}{Color.RESET}', flush=True)

    @staticmethod
    def print_error(msg):
        """Print error message in red."""
        Color.print(f'{Color.RED}{msg}{Color.RESET}', flush=True)

    @staticmethod
    def print_warning(msg):
        """Print warning message in yellow."""
        Color.print(f'{Color.YELLOW}{msg}{Color.RESET}', flush=True)

    @staticmethod
    def print_info(msg):
        """Print info message in blue."""
        Color.print(f'{Color.BLUE}{msg}{Color.RESET}', flush=True)

    @staticmethod
    def print_title(title):
        """Print title in bold cyan."""
        Color.print(f'{Color.BOLD}{Color.CYAN}{title}{Color.RESET}', flush=True)

    @staticmethod
    def print_header(header):
        """Print header in bold green."""
        Color.print(f'{Color.BOLD}{Color.GREEN}{header}{Color.RESET}', flush=True)

    @staticmethod
    def print_subheader(subheader):
        """Print subheader in bold cyan."""
        Color.print(f'{Color.BOLD}{Color.CYAN}{subheader}{Color.RESET}', flush=True)

    @staticmethod
    def print_zone(zone_name):
        """Print zone name in bold green."""
        Color.print(f'{Color.BOLD}{Color.GREEN}{zone_name}{Color.RESET}', flush=True)

    @staticmethod
    def print_item(item_name, status):
        """Print item with status."""
        status_color = Color.GREEN if status else Color.RED
        Color.print(f'  {status_color}{item_name}{Color.RESET}', flush=True)

    @staticmethod
    def print_stat(stat_name, value):
        """Print stat name and value."""
        Color.print(f'  {stat_name}: {value}', flush=True)

    @staticmethod
    def print_separator():
        """Print separator line."""
        Color.print(f'{Color.DIM}{"─" * 60}{Color.RESET}', flush=True)

    @staticmethod
    def print_summary(data):
        """Print summary of data."""
        Color.print(f'{Color.BOLD}{Color.CYAN}Summary{Color.RESET}', flush=True)
        Color.print(f'{Color.DIM}{"─" * 40}{Color.RESET}', flush=True)
        for key, value in data.items():
            Color.print(f'  {key}: {value}', flush=True)
        Color.print(f'{Color.DIM}{"─" * 40}{Color.RESET}', flush=True)
