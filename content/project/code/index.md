---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Code Development"
summary: "Data evaluation, instrument control, and simulations these days all require code development skills and experience."
authors: []
profile: false
tags: []
categories: []
date: 2020-05-24T15:34:09-07:00
weight: 60

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

Research should preferentially consist of new and unique tasks. Computers on the other hand are ideally suited for repetitive tasks. Furthermore, in order to run [RIMS instruments](/project/rims/) control software is required. We have worked and are currently engaged in multiple code development projects. You can find many of these projects on the <a href="https://github.com/galactic-forensics" target="_blank">lab's GitHub page</a>, <a href="https://github.com/trappitsch" target="_blank">Reto's GitHub page</a>, or the <a href="https://github.com/RIMS-Code" target="_blank">GitHub page</a>. Below we outline some notable projects.

*Note*: We are strong supporters free and open source software (<a href="https://en.wikipedia.org/wiki/Free_and_open-source_software" target="_blank">FOSS</a>). Scientific research is generally paid for by the tax payer. The outcome should thus be freely available for everyone. We thus strive to publish all software under open source licenses and only use open source software in our daily life.

<a href="https://www.python.org" target="_blank">![Python Logo](/img/projects/code/python_logo.png)</a>

As you will notice, Reto's programming language of choice is Python. All code is made available on GitHub. Some project are better documented than others. If you are interested in anything specific and have questions, please [contact us](/contact/). Also, contributions to our codes are always highly welcomed. Please have a look at the developer guides (when available). Feel free to create pull requests for documentation enhancement, small bug fixes, etc. We are looking forward to your ideas and issues.


## iniabu

Iniabu is a package for python that you can use to easily calculate the inital abundances of the solar system and return ratios as δ-values or in bracket notation. By default the initial abundances from <a href="https://doi.org/10.1007/978-3-540-88055-4_34" target="_blank">Lodders et al. (2009)</a> are called. You can install this module by simply calling:

    pip install iniabu

Help on how to use it can either be found in the <a href="https://github.com/LLNL/iniabu" target="_blank">readme file on github</a> or by accessing the docstring, e.g., from within ipython by calling:

    import iniabu                                                           
    ini = iniabu.IniAbu()                                                   
    ini?

Give the package a spin but note that we have a completely rewritten package in the makings <a href="https://github.com/galactic-forensics/iniabu" target="_blank">here</a>. This new version will be released as v1.0.0 and will break backwards compatibility. You have been warned :)

## InstrumentKit

The freely available <a href="https://github.com/Galvant/InstrumentKit" target="_blank">InstrumentKit</a> has been used to interact with hardware for the LION instrument. Several classes have been contributed to this excellent compilation of tools, such that they can be used by other groups as well.


## Mahon Fitting

In order to fit a linear regression we use the routine by <a href="https://www.tandfonline.com/doi/abs/10.1080/00206819709465336" target="_blank">Mahon (1996)</a>, also known as the "New York" regression, should be used. Along with the <a href="https://doi.org/10.3847/2041-8213/aabba9" target="_blank">Trappitsch et al. (2018)</a> publication we published a tool to easily apply the Mahon fitting routine to any dataset. The tool, including a detailed readme file, can be found on <a href="https://github.com/LLNL/MahonFitting" target="_blank">the respective github site</a>.

## Resonance Ionization Scheme Drawer

Would you like to make resonance ionization schemes like the one we show [here](/project/rims/) for titanium? Check out our <a href="https://github.com/trappitsch/RIMSSchemeDrawer" target="_blank">`RIMS Scheme Drawer`</a> software. This GUI allows you to draw many resonance ionization schemes with just a few clicks and results in publishable figures.

<a href="https://github.com/trappitsch/RIMSSchemeDrawer" target="_blank">![RIMSSchemeDrawer](https://raw.githubusercontent.com/trappitsch/RIMSSchemeDrawer/master/examples/screenshot_titanium.png)</a>

## Coordinate Transformation

If you work with samples in various instruments, our coordinate transfer program might be of interest to you. Assuming you have coordinates for your particles, our program allows you easily transfer these coordinates from one system into the other. You can use fiducial marks or simply find some of your sample positions again and start from there. 

<a href="https://github.com/trappitsch/CoordinateTransformation" target="_blank">![Coordinate Transformation](https://raw.githubusercontent.com/trappitsch/CoordinateTransformation/master/docs/screenshot-full.png)</a>