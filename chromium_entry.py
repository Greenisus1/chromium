"""Terminal launcher for the actual distro Chromium browser, not a terminal renderer."""
import curses,os,shutil,subprocess
from ui import put,run

def browser():return shutil.which('chromium') or shutil.which('chromium-browser')
def launch(env=None,uid=None):
 env=os.environ if env is None else env;uid=os.geteuid() if uid is None else uid
 if not browser():return 'Chromium is not installed. Run the Store install action first.'
 if not (env.get('DISPLAY') or env.get('WAYLAND_DISPLAY')):return 'Desktop display required. Plain SSH cannot show Chromium. Use unicode-block-browser for terminal browsing.'
 if uid==0:return 'Run this app as your desktop user, not root. Chromium sandbox is never disabled.'
 try:code=subprocess.run([browser(),'--start-fullscreen','--new-window','about:blank']).returncode
 except OSError as exc:return 'Could not launch Chromium: '+str(exc)
 return 'Browser closed.' if code==0 else 'Chromium exited with code '+str(code)+'.'
def loop(s):
 msg=''
 while True:
  h,w=s.getmaxyx();s.erase();put(s,1,2,'C H R O M I U M',curses.A_BOLD)
  lines=['Actual Chromium browser from your Linux distribution.', 'This fullscreen terminal launcher is not a terminal web browser.', '', 'Installed: '+(browser() or 'not found'), 'Desktop: '+('available' if os.getenv('DISPLAY') or os.getenv('WAYLAND_DISPLAY') else 'not available'), '', 'L / Enter launches a fullscreen desktop window.', 'Q quits. F11 in Chromium toggles fullscreen.', 'Needs a desktop user, not root. No --no-sandbox workaround.', '',msg]
  if h<20 or w<70:put(s,3,2,'Resize to70x20. Q exits.')
  else:
   for i,line in enumerate(lines):put(s,3+i,2,line)
  put(s,h-2,2,'Desktop browser, not a headless SSH renderer.')
  s.refresh();k=s.getch()
  if k in (ord('q'),ord('Q')):return
  if h<20 or w<70:continue
  if k in (10,13,ord('l'),ord('L')):
   curses.def_prog_mode();curses.endwin()
   try:msg=launch()
   finally:curses.reset_prog_mode();s.clearok(True)
if __name__=='__main__':raise SystemExit(run(loop))
