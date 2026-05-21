#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Install personal-memory-workflow into a Codex-compatible skills directory.

Usage:
  install.sh [--target-root PATH] [--copy] [--force]

Defaults:
  --target-root "$HOME/.codex/skills"
  symlink install, so local repo updates are picked up automatically.

Options:
  --copy        Copy files instead of creating a symlink.
  --force       Replace an existing target path.
USAGE
}

target_root="${MEMORY_SKILLS_DIR:-${HOME}/.codex/skills}"
mode="symlink"
force="0"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target-root)
      target_root="${2:?missing value for --target-root}"
      shift 2
      ;;
    --copy)
      mode="copy"
      shift
      ;;
    --force)
      force="1"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target="${target_root}/personal-memory-workflow"

mkdir -p "${target_root}"

if [[ -e "${target}" || -L "${target}" ]]; then
  if [[ -L "${target}" && "$(readlink "${target}")" == "${skill_dir}" ]]; then
    echo "[OK] already installed: ${target} -> ${skill_dir}"
    exit 0
  fi
  if [[ "${force}" != "1" ]]; then
    echo "[ERROR] target already exists: ${target}" >&2
    echo "Re-run with --force to replace it." >&2
    exit 3
  fi
  rm -rf "${target}"
fi

if [[ "${mode}" == "copy" ]]; then
  mkdir -p "${target}"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "${skill_dir}/" "${target}/"
  else
    cp -R "${skill_dir}/." "${target}/"
  fi
  echo "[OK] copied skill to ${target}"
else
  ln -s "${skill_dir}" "${target}"
  echo "[OK] symlinked skill: ${target} -> ${skill_dir}"
fi

