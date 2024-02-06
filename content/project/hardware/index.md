---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Hardware Development"
summary: "For cutting edge research applications, the perfect hardware must sometimes be built by yourself."
authors: []
profile: false
tags: []
categories: []
date: 2024-02-06
weight: 80

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

We develop our own hardware, mainly for [RIMS](/project/RIMS) applications. However, some of these might be useful for other laser- and mass spectrometry laboratories! Have a look. All of our hardware is released open-source with well documented building instructions, firmware, and python interfaces.

## Digital Outputs: `DigOutBox`

We developped a digital output box (called `DigOutBox`). Our intended use was to control laser shutters with a remote control (while working on the laser), but also from the computer. The box simply applies low (0 V) or high (5 V) voltage to the outputs, which can be fed into the TTL input channel of a laser shutter or any other device.

Since the project was developed for lasers, several safety features are built into the hardware:

- **Software lockout**: The remote control can be configured such that the user can easily lock-out any interaction from the computer
- **Interlock**: Optionally, an interlock line can be connected, which, when triggered, will close all shutters and keep them closed until untriggered.

The first version of the box can be seen here:

![Image of the DigOutBox with remote control](/img/projects/hwdev/gfl002_setup.jpg)

The box also comes with a python module to communicate from your own program, and with a GUI for computer control - assuming the software lockout is not triggered!

If you are interested, have a look at the <a href="https://github.com/galactic-forensics/DigOutBox" target="_blank">GitHub repository</a> and our <a href="https://digoutbox.readthedocs.io/" target="_blank">detailed documentation</a> of the project.

