from __future__ import division
import difflib, re, cgi
import unicodedata as ucd
import HTMLParser
from aqt.qt import *
from anki.utils import stripHTML, isMac, json
from anki.hooks import addHook, runHook
from anki.sound import playFromText, clearAudioQueue, play
from aqt.utils import mungeQA, getBase, openLink, tooltip
from aqt.sound import getAudio
import aqt
from aqt.reviewer import Reviewer

def myShowAnswerButton(self):
    self._bottomReady = True
    if not self.typeCorrect:
        self.bottom.web.setFocus()
    middle = '''
<span class=stattxt>%s</span><br>
<button title="%s" id=ansbut style=width:260px; onclick='py.link(\"ans\");'>%s</button>''' % (
    self._remaining(), _("Shortcut key: %s") % _("Space"), _("Show Answer"))
    # wrap it in a table so it has the same top margin as the ease buttons
    middle = "<table cellpadding=0><tr><td class=stat2 align=center>%s</td></tr></table>" % middle
    if self.card.shouldShowTimer():
        maxTime = self.card.timeLimit() / 1000
    else:
        maxTime = 0
    self.bottom.web.eval("showQuestion(%s,%d);" % (
        json.dumps(middle), maxTime))
 
Reviewer._showAnswerButton = myShowAnswerButton