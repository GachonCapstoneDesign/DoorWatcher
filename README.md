<p align="center">
<h2 align="center"> Capstone Design - DoorWatcher Project - <a href="https://github.com/GachonCapstoneDesign/DoorWatcher/wiki/Project-outline">Wiki</a> · <a href="https://travis-ci.org/sergiokopplin/indigo"><img src="https://camo.githubusercontent.com/5393485b732749b3499264168fa8af60166071e8/68747470733a2f2f7472617669732d63692e6f72672f73657267696f6b6f70706c696e2f696e6469676f2e7376673f6272616e63683d67682d7061676573" alt="Build Status" data-canonical-src="https://travis-ci.org/sergiokopplin/indigo.svg?branch=gh-pages" style="max-width:100%;"></a></h2>
</p>

<p align="center">Welcome to DoorWatcher's project</p>

***

<p align="center">
<b><a href="README.md#what-has-inside">What has inside</a></b>
|
<b><a href="README.md#setup">Setup</a></b>
|
<b><a href="README.md#settings">Settings</a></b>
|
<b><a href="README.md#how-to">How to</a></b>
</p>

<p align="center">
<img src="https://raw.githubusercontent.com/GachonCapstoneDesign/DoorWatcher/master/assets/images/title.png" />
</p>

## What has inside
- [Project outline](https://github.com/GachonCapstoneDesign/DoorWatcher/wiki/Project-outline)
- [How to install](https://github.com/GachonCapstoneDesign/DoorWatcher/wiki/1.-Raspberry-pi-OS-Install)
- [Install the project environment](https://github.com/GachonCapstoneDesign/DoorWatcher/wiki/2.-Installing-the-Library)
- DoorWatcher [Module.1](https://github.com/GachonCapstoneDesign/DoorWatcher/wiki/Module1.-DoorWatcher) [Module.2](https://github.com/GachonCapstoneDesign/DoorWatcher/wiki/Module2.-Streaming) [Module.3](https://github.com/GachonCapstoneDesign/DoorWatcher/wiki/Module3.-Unsuspected-person-detection) 

## Setup

0. :star: to the project. :metal:
2. Fork the project [Indigo](https://github.com/sergiokopplin/indigo/fork)
3. Edit `_config.yml` with your data (check <a href="README.md#settings">settings</a> section)
4. Write some posts :bowtie:

If you want to test locally on your machine, do the following steps also:

1. Install [Jekyll](http://jekyllrb.com), [NodeJS](https://nodejs.org/) and [Bundler](http://bundler.io/).
2. Clone the forked repo on your machine
3. Enter the cloned folder via terminal and run `bundle install`
4. Then run `bundle exec jekyll serve --config _config.yml,_config-dev.yml`
5. Open it in your browser: `http://localhost:4000`
6. Test your app with `bundle exec htmlproofer ./_site`

## Settings

You must fill some informations on `_config.yml` to customize your site.

```
name: John Doe
bio: 'A Man who travels the world eating noodles'
picture: 'assets/images/profile.jpg'
...

and lot of other options, like width, projects, pages, read-time, tags, related posts, animations, multiple-authors, etc.
```

## How To?

Check the [FAQ](./FAQ.md) if you have any doubt or problem.

---

[MIT](http://kopplin.mit-license.org/) License © Gathon VIV
