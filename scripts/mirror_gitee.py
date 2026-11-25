"""Mirror a published board package into a Gitee checkout."""
import argparse
import hashlib
import json
import re
from pathlib import Path

GITEE_REPO = "https://gitee.com/pingshui11/arduino-esp32-boards"
INDEX = "package_waveshare_index.json"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version")
    parser.add_argument("archive", type=Path)
    parser.add_argument("mirror", type=Path)
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", args.version):
        parser.error("expected MAJOR.MINOR.PATCH")

    source = json.loads((Path(__file__).resolve().parents[1] / INDEX).read_text(encoding="utf-8"))
    package = source["packages"][0]
    release = next((item for item in package["platforms"] if item["version"] == args.version), None)
    if release is None:
        parser.error("release version is missing from the GitHub index")

    filename = f"waveshare-esp32-{args.version}.zip"
    archive = args.archive.read_bytes()
    checksum = "SHA-256:" + hashlib.sha256(archive).hexdigest().upper()
    if release["archiveFileName"] != filename or release["checksum"].upper() != checksum.upper():
        parser.error("archive does not match the GitHub index")
    if int(release["size"]) != len(archive):
        parser.error("archive size does not match the GitHub index")

    mirror_index = args.mirror / INDEX
    existing = json.loads(mirror_index.read_text(encoding="utf-8"))["packages"][0]
    retained = [
        item for item in existing["platforms"]
        if item["version"] != args.version and item["url"].startswith(f"{GITEE_REPO}/raw/main/archives/")
    ]
    directory = args.mirror / "archives"
    directory.mkdir(exist_ok=True)
    (directory / filename).write_bytes(archive)
    package["websiteURL"] = GITEE_REPO
    package["help"]["online"] = f"{GITEE_REPO}/issues"
    release["url"] = f"{GITEE_REPO}/raw/main/archives/{filename}"
    package["platforms"] = sorted(
        [release, *retained],
        key=lambda item: tuple(map(int, item["version"].split("."))),
        reverse=True,
    )
    mirror_index.write_text(json.dumps(source, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
