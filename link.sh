#!/bin/sh
# Link every top-level directory of this repository into a harness's
# skills directory, and remove links into this repository whose source
# directory is gone. Safe to run again after every pull.
#
#   ./link.sh                 # Claude Code: ~/.claude/skills
#   ./link.sh ~/.agents/skills   # another harness's skills directory
#
# A directory without SKILL.md (a shared directory) is linked too; the
# harness ignores it as a skill, and the skills that read it find it by
# relative path. The directories tools/ and .git are never linked.
set -eu
REPO=$(cd "$(dirname "$0")" && pwd)
TARGET=${1:-$HOME/.claude/skills}
mkdir -p "$TARGET"
for dir in "$REPO"/*/; do
  dir=${dir%/}
  name=$(basename "$dir")
  case "$name" in tools|.*) continue ;; esac
  link="$TARGET/$name"
  if [ -L "$link" ]; then
    if [ "$(readlink "$link")" != "$dir" ]; then
      rm "$link"; ln -s "$dir" "$link"; echo "relinked $name"
    fi
  elif [ -e "$link" ]; then
    echo "skipped $name: $link exists and is not a symlink" >&2
  else
    ln -s "$dir" "$link"; echo "linked $name"
  fi
done
for link in "$TARGET"/*; do
  [ -L "$link" ] || continue
  dest=$(readlink "$link")
  case "$dest" in
    "$REPO"/*) [ -e "$dest" ] || { rm "$link"; echo "pruned $(basename "$link")"; } ;;
  esac
done
