import unittest
from unittest.mock import patch,Mock
import chromium_entry as a
class Tests(unittest.TestCase):
 def test_missing(self):
  with patch.object(a,'browser',return_value=None):self.assertIn('not installed',a.launch())
 def test_headless(self):
  with patch.object(a,'browser',return_value='/usr/bin/chromium'),patch.object(a.subprocess,'run') as r:self.assertIn('Desktop display required',a.launch({},1000));r.assert_not_called()
 def test_root(self):
  with patch.object(a,'browser',return_value='/usr/bin/chromium'),patch.object(a.subprocess,'run') as r:self.assertIn('not root',a.launch({'DISPLAY':':0'},0));r.assert_not_called()
 def test_launch(self):
  with patch.object(a,'browser',return_value='/usr/bin/chromium'),patch.object(a.subprocess,'run',return_value=Mock(returncode=0)) as r:self.assertEqual('Browser closed.',a.launch({'DISPLAY':':0'},1000));self.assertEqual(r.call_args.args[0],['/usr/bin/chromium','--start-fullscreen','--new-window','about:blank'])
 def test_failure(self):
  with patch.object(a,'browser',return_value='/usr/bin/chromium'),patch.object(a.subprocess,'run',return_value=Mock(returncode=7)):self.assertIn('code 7',a.launch({'WAYLAND_DISPLAY':'wayland-0'},1000))
