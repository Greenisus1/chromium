# Chromium 1.0.0

Pi App Store entry for the actual distribution Chromium browser, not a terminal web renderer. The fullscreen terminal launcher shows installation/display status. L or Enter opens Chromium with --start-fullscreen in a desktop session; Q exits the launcher. F11 in Chromium toggles fullscreen. Minimum launcher70x20, inputs pause below that size.

Install checks Python3+curses and installs the Debian chromium package with apt-get when missing. A desktop is required to browse: plain headless SSH cannot show the browser. Use unicode-block-browser for terminal browsing. Run as your desktop user, not root. The launcher never adds --no-sandbox or turns off browser security. A Store started as root can install it but must not launch Chromium as root.

    bash app-store.sh install
    bash app-store.sh run
    python3 -m unittest -v

Five mocked launch tests cover missing browser, no display, root refusal, fullscreen arguments and failure exit. Actual fullscreen terminal status, resize and clean restoration checked on Linux. Actual graphical Chromium launch and package install not exercised here; Raspberry Pi/non-Linux untested. No bundled browser binaries, logos or branded assets; MIT applies to this launcher only.

Invocation reference: https://manpages.debian.org/bookworm/chromium/chromium.1.en.html
Fullscreen switch reference: https://chromium.googlesource.com/chromium/src/+/673a452fa0cad726f06264fb8de9a8073ddcef7e/content/public/common/content_switches.cc
