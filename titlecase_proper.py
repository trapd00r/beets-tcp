# Author: Magnus Woldrich, japh@irc.libera.chat
#   Date: 2021-07-07 10:07:37
# > https://github.com/beetbox/beets/discussions/3998
#
# adds a template function %titlecase_proper{} that titlecases
# strings better.
#
# The beets builtin template function %title{} uses str.capwords(). This
# causes issues with strings that begin with a character that can't be
# titlecased:
#
# It's Raining Men (instrumental Version).flac
#
# str.title() does a better job but causes issues with strings like
# "It's" instead:
#
# It'S Raining Men (Instrumental Version).flac
#
# This plugin takes care of both issues.

from beets.plugins import BeetsPlugin
from titlecase import titlecase

class titlecase_proper(BeetsPlugin):
    def __init__(self):
        super(titlecase_proper, self).__init__()
        self.template_funcs['titlecase_proper'] = _titlecase_proper

def _titlecase_proper(text):
  return titlecase(text)
#   import re
#   return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
#                    lambda mo: mo.group(0).capitalize(),
#                     text)
