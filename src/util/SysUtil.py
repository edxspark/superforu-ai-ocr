from pathlib import Path


def get_project_path_root():
    return Path(__file__).resolve().parent.parent.parent

if __name__ == '__main__':
    print(get_project_path_root())
