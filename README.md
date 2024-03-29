beets-tcp / titlecase-proper
----------------------

Adds a template function `%tcp{}` that titlecases
strings better.

Why?
----------------------

The beets builtin template function `%title{}` uses `str.capwords()`.

This causes issues with strings that begin with a character that can't
be titlecased:


> It's Raining Men (instrumental Version).flac


`str.title()` does a better job but causes issues with strings like
"It's" instead:


> It'S Raining Men (Instrumental Version).flac


This plugin takes care of both issues.

Additionally, custom words can be added to the plugin section in
beets/config.yaml that will be returned as-is:

```yaml
tcp:
  asis: [
    'PhD',
    'DJ',
    'TCP',
    'YodA',
  ]
```

which can render:

- **DJ Madfist the Invincible TCP Guru │2024│ Got Myself an PhD in the 313 (Deluxe YodA Edition) [MP3]**


Installation
------------
```bash
$ pip3 install titlecase
```

Replace all `%title{}` functions with the shiny new one:

```bash
perl -i.old -pe 's/%title{(\$[A-Za-z_-]+)}/%tcp{$1}/g' config.yaml
```

Add this script to the beets pluginpath:

```yaml
pluginpath: ['/usr/lib/python3.9/site-packages/beetsplug/',
             '/home/scp1/dev/beets-tcp',
            ]
```

Add the plugin to the plugin list and configure it:

```yaml
plugins: [
  'tcp'
]

tcp:
  asis: ['foo', 'Bar', 'TCP']
```
