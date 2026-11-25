"""Build a Boards Manager archive and generate release and test indexes."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    version = args.version
    if not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", version):
        parser.error("version must have the form MAJOR.MINOR.PATCH")

    index_path = ROOT / "package_waveshare_index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    package = index["packages"][0]
    if any(platform["version"] == version for platform in package["platforms"]):
        parser.error(f"{version} is already in the public index")

    source = ROOT / "platform"
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"waveshare-esp32-{version}.zip"
    boards = (source / "boards.txt").read_text(encoding="utf-8")
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                name = f"platform/{path.relative_to(source).as_posix()}"
                if path.name == "platform.txt":
                    config = path.read_text(encoding="utf-8")
                    config = re.sub(r"^version=.*$", f"version={version}", config, flags=re.M)
                    bundle.writestr(name, config)
                else:
                    bundle.write(path, name)

    metadata = {
        "name": "Waveshare ESP32 Boards",
        "architecture": "esp32",
        "version": version,
        "category": "Contributed",
        "url": f"{package['websiteURL']}/releases/download/v{version}/{archive.name}",
        "archiveFileName": archive.name,
        "checksum": "SHA-256:" + hashlib.sha256(archive.read_bytes()).hexdigest().upper(),
        "size": str(archive.stat().st_size),
        "boards": [{"name": name} for name in re.findall(r"^[\w-]+\.name=(.+)$", boards, re.M)],
        "toolsDependencies": [],
    }
    package["platforms"].insert(0, metadata)
    (output / index_path.name).write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")

    metadata["url"] = f"http://127.0.0.1:8765/{archive.name}"
    package["platforms"] = [metadata]
    (output / "package_waveshare_test_index.json").write_text(
        json.dumps(index, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
