## Author: Magnus Woldrich, japh@irc.libera.chat
##   Date: 2021-07-07 10:07:37
## > https://github.com/beetbox/beets/discussions/3998
## > https://www.japh.se/2021/07/14/a_better_titlecase_function_for_beets.html
##
## adds a template function %tcp{} that titlecases
## strings better.
##
## The beets builtin template function %title{} uses str.capwords(). This
## causes issues with strings that begin with a character that can't be
## titlecased:
##
## It's Raining Men (instrumental Version).flac
##
## str.title() does a better job but causes issues with strings like
## "It's" instead:
##
## It'S Raining Men (Instrumental Version).flac
##
## This plugin takes care of both issues.

from beets         import config
from beets.plugins import BeetsPlugin
from titlecase     import titlecase
import os

# error handling, in case there's no config section for
# tcp, we should just titlecase as normal
words_to_use_asis = None
try:
  words_to_use_asis = config['tcp']['asis'].get()
except:
  words_to_use_asis = None

class tcp(BeetsPlugin):
    def __init__(self):
      super(tcp, self).__init__()
      self.template_funcs['tcp'] = _tcp


def custom_casing(word, **kwargs):
    for w in words_to_use_asis:
      # compare words uppercased, since the casing can be whatever in
      # the config.
        if word.upper() == w.upper():
            return w


def _tcp(text):
    if words_to_use_asis is not None:
        real_words = titlecase(text, callback=custom_casing)
    else:
        real_words = titlecase(text)

    return ''.join(real_words)
