from pathlib import Path
import shutil


REPO_ROOT = Path(__file__).resolve().parents[1]
TARGET_DIR = REPO_ROOT / "data" / "cleaned"

SOURCE_CANDIDATES = [
    REPO_ROOT.parents[1] / "Presentation" / "Cleaned",
    Path("F:/RA/Presentation/Cleaned"),
]

FILES = [
    "94.csv",
    "95.csv",
    "96.csv",
    "97.csv",
    "98.csv",
    "99.csv",
    "400.csv",
    "401.csv",
    "402.csv",
    "403.csv",
    "CPI.xlsx",
]


def main() -> None:
    source_dir = next((path for path in SOURCE_CANDIDATES if path.exists()), None)
    if source_dir is None:
        candidates = "\n".join(str(path) for path in SOURCE_CANDIDATES)
        raise FileNotFoundError(f"No local source data folder found. Checked:\n{candidates}")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    copied = []
    missing = []
    for file_name in FILES:
        source = source_dir / file_name
        target = TARGET_DIR / file_name
        if source.exists():
            shutil.copy2(source, target)
            copied.append(file_name)
        else:
            missing.append(file_name)

    print(f"Source: {source_dir}")
    print(f"Target: {TARGET_DIR}")
    print(f"Copied {len(copied)} files.")
    if missing:
        print("Missing files:")
        for file_name in missing:
            print(f"  - {file_name}")


if __name__ == "__main__":
    main()
