#!/usr/bin/env python3
import argparse
import json
import shlex
import shutil
import subprocess
import sys
from pathlib import Path


def find_iwyu():
    for name in ("include-what-you-use", "iwyu"):
        p = shutil.which(name)
        if p:
            return p
    return None


def load_compile_commands(db_path: Path):
    cc_path = db_path / "compile_commands.json"
    if not cc_path.exists():
        return []
    data = json.loads(cc_path.read_text())
    return data


def find_entry_for_file(entries, file_path: Path):
    file_str = str(file_path)
    for e in entries:
        # entry 'file' is often relative to project root
        if Path(e.get("file", "")).resolve() == file_path.resolve():
            return e
    # fallback: match basename
    for e in entries:
        if Path(e.get("file", "")).name == file_path.name:
            return e
    # If it's a header, try to find a source file that includes it
    if file_path.suffix in (".h", ".hpp"):
        header_name = file_path.name
        for e in entries:
            src = Path(e.get("file", ""))
            try:
                content = src.read_text()
            except Exception:
                continue
            if f'#include "{header_name}"' in content or f'#include <{header_name}>' in content:
                return e
        # fallback: return first entry in same directory
        for e in entries:
            if Path(e.get("file", "")).parent == file_path.parent:
                return e
        # final fallback: return first entry
        if entries:
            return entries[0]
    return None


def build_command(entry, iwyu_bin, target_file: Path):
    if "arguments" in entry:
        args = entry["arguments"].copy()
    else:
        args = shlex.split(entry.get("command", ""))
    if not args:
        return None
    # replace the compiler with iwyu
    args[0] = iwyu_bin
    # ensure the file we analyze is the target_file
    # find any occurrence of the original file in args and replace it
    replaced = False
    for i, a in enumerate(args):
        if a == entry.get("file") or a.endswith(str(target_file.name)):
            args[i] = str(target_file)
            replaced = True
    if not replaced:
        args.append(str(target_file))
    # for headers, ensure correct language
    if target_file.suffix in (".h", ".hpp") and "-x" not in args:
        args.insert(1, "-x")
        args.insert(2, "c++-header")
    return args


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("-p", "--build-dir", default="build/default")
    p.add_argument("files", nargs="*")
    args = p.parse_args(argv)

    iwyu_bin = find_iwyu()
    if not iwyu_bin:
        print("include-what-you-use not found in PATH", file=sys.stderr)
        return 1

    db_path = Path(args.build_dir)
    entries = load_compile_commands(db_path)
    if not entries:
        print(f"No compile_commands.json found in {db_path}", file=sys.stderr)
        return 1

    rc = 0
    for f in args.files:
        target = Path(f)
        entry = find_entry_for_file(entries, target)
        if not entry:
            print(f"No compile command found for {f}", file=sys.stderr)
            rc = 1
            continue
        cmd = build_command(entry, iwyu_bin, target)
        if not cmd:
            print(f"Failed to build command for {f}", file=sys.stderr)
            rc = 1
            continue
        print(f"Running: {' '.join(cmd)}")
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.stdout:
            print(proc.stdout)
        if proc.stderr:
            print(proc.stderr, file=sys.stderr)
        if proc.returncode != 0:
            rc = proc.returncode

    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
