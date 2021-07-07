beets-titlecase_proper
----------------------

Adds a template function `%titlecase_proper{}` that titlecases
strings better.

The beets builtin template function `%title{}` uses `str.capwords()`.
This causes issues with strings that begin with a character that can't
be titlecased:

`
It's Raining Men (instrumental Version).flac
`

`str.title()` does a better job but causes issues with strings like
"It's" instead:

`
It'S Raining Men (Instrumental Version).flac
`

This plugin takes care of both issues.

Installation
------------

`$ pip3 install titlecase`

Replace all `%title{}` functions with the shiny new one:

`
perl -i.old -pe 's/%title{(\$[A-Za-z_-]+)}/%titlecase_proper{$1}/g' config.yaml
`

Add this script to the beets pluginpath:


`
pluginpath: ['/usr/lib/python3.9/site-packages/beetsplug/',
             '/home/scp1/dev/beets-titlecase_proper',
            ]
`

Add the plugin to the plugin list:

`
plugins: [
  'titlecase_proper'
]
`
