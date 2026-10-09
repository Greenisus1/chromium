#!/bin/bash
# pi-app-store: 1
set -eu
cd -- "$(dirname -- "$0")"
case "${1:-}" in
 install)
  python3 -c 'import curses;from pathlib import Path;[compile(p.read_bytes(),str(p),"exec") for p in Path(".").glob("*.py")]'
  if ! command -v chromium >/dev/null && ! command -v chromium-browser >/dev/null;then
   command -v apt-get >/dev/null || { echo 'Install Chromium with your distribution package manager.';exit 1; }
   if [ "$(id -u)" = 0 ];then apt-get update;apt-get install -y chromium;else sudo apt-get update;sudo apt-get install -y chromium;fi
  fi
  command -v chromium >/dev/null || command -v chromium-browser >/dev/null
  ;;
 run) exec python3 chromium_entry.py ;;
 *) echo 'Use: bash app-store.sh install|run';exit 1 ;;
esac
