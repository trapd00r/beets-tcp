beets-titlecase_proper
----------------------

Adds a template function `%titlecase_proper{}` that titlecases
strings better.

The beets builtin template function `%title{}` uses `str.capwords()`.
This causes issues with strings that begin with a character that can't
be titlecased:


> It's Raining Men (instrumental Version).flac


`str.title()` does a better job but causes issues with strings like
"It's" instead:


> It'S Raining Men (Instrumental Version).flac


This plugin takes care of both issues.

Additionally, words can be added to **~/.beets\_titlecase** that will be
returned as-is:


```bash
{% highlight bash %}
$ cd "Dj TCP the Reckless │2021│ So Much Drama in the PHD [CDR, MP3]"
$ for w in TCP DJ PhD; do echo $w; done >> ~/.beets_titlecase
$ beet import .
$ beet ls -a 'so much drama' -f \$path
DJ TCP the Reckless │2021│ So Much Drama in the PhD [CDR, MP3]
```


Installation
------------
```bash
$ pip3 install titlecase
```

Replace all `%title{}` functions with the shiny new one:

```bash
perl -i.old -pe 's/%title{(\$[A-Za-z_-]+)}/%titlecase_proper{$1}/g' config.yaml
```

Add this script to the beets pluginpath:

```yaml
pluginpath: ['/usr/lib/python3.9/site-packages/beetsplug/',
             '/home/scp1/dev/beets-titlecase_proper',
            ]
```

Add the plugin to the plugin list:

```yaml
plugins: [
  'titlecase_proper'
]
```

TODO
----
Replace the text file in ~/ with inline configuration in config.yaml:
https://beets.readthedocs.io/en/stable/dev/plugins.html#read-configuration-options
