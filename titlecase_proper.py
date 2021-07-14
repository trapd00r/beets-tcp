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
# Furthermore, word specified in ~/.beets_titlecase

from beets.plugins import BeetsPlugin
from titlecase     import titlecase
import os
import logging
logger = logging.getLogger(__name__)

# wordlist with words that will be returned as-is and NOT titlecased.
# ~/.beets_titlecase
# That means situations like this can be avoided:
# > Dj TCP the Reckless │2021│ So Much Drama in the PHD [CDR, MP3]
#
# And instead we get the proper:
# > DJ TCP the Reckless │2021│ So Much Drama in the PhD [CDR, MP3]
wordlist_asis = os.path.join(os.path.expanduser('~'), '.beets_titlecase')

def create_wordlist_filter_from_file(file_path):
    '''
    Load a list of abbreviations from the file with the provided path,
    reading one abbreviation from each line, and return a callback to
    be passed to the `titlecase` function for preserving their given
    canonical capitalization during title-casing.
    '''
    if file_path is None:
        logger.debug('No abbreviations file path given')
        return lambda word, **kwargs: None
    file_path_str = str(file_path)
    if not os.path.isfile(file_path_str):
        logger.debug('No abbreviations file found at ' + file_path_str)
        return lambda word, **kwargs: None
    with open(file_path_str) as f:
        logger.debug('Reading abbreviations from file ' + file_path_str)
        abbrevs_gen = (line.strip() for line in f.read().splitlines() if line)
        abbrevs = {abbr.upper(): abbr for abbr in abbrevs_gen}
        if logger.isEnabledFor(logging.DEBUG):
            for abbr in abbrevs.values():
                logger.debug('Registered abbreviation: ' + abbr)
        return lambda word, **kwargs: abbrevs.get(word.upper())


class titlecase_proper(BeetsPlugin):
    def __init__(self):
        super(titlecase_proper, self).__init__()
        self.template_funcs['titlecase_proper'] = _titlecase_proper

def _titlecase_proper(text):
  return titlecase(text, callback=create_wordlist_filter_from_file(wordlist_asis))
