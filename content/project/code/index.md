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

Research is fun when it consists of new and unique tasks. For repetitive ones on the other hand, computers are uniquely suited. Furthermore, in order to run [RIMS instruments](/project/rims/) control software is required. We have worked and are currently engaged in multiple code development projects. You can find many of these projects on the <a href="https://github.com/galactic-forensics" target="_blank">lab's GitHub page</a>, <a href="https://github.com/trappitsch" target="_blank">Reto's GitHub page</a>, or the <a href="https://github.com/RIMS-Code" target="_blank">RIMS-Code GitHub page</a>. Below we outline some notable projects.

*Note*: We are strong supporters of free and open source software (<a href="https://en.wikipedia.org/wiki/Free_and_open-source_software" target="_blank">FOSS</a>). Scientific research is generally paid for by the taxpayer. The outcome should thus be freely available for everyone. We strive to publish all software under open source licenses and only use open source software in our daily life.

<a href="https://www.python.org" target="_blank">![Python Logo](/img/projects/code/python_logo.png)</a>

As you will notice, a dominating programming language in our lab is Python. This becomes especially clear when you look at the GitHub pages given above. If you are interested in any of our specific code or you have questions, please feel free to [contact us](/contact/)! Also, contributions to our codes are always welcomed. Please have a look at the developer guides (when available). Feel free to create pull requests for documentation enhancement, small bug fixes, etc. We are looking forward to your ideas and issues.


## iniabu

`iniabu` is a package for python that you can use 
to easily calculate the inital abundances of the solar system 
and return ratios as δ-values or in bracket notation. 
By default the initial abundances from 
<a href="https://doi.org/10.1007/978-3-540-88055-4_34" target="_blank">Lodders et al. (2009)</a> 
are used.
You can install this module by simply calling:

``` console
pip install iniabu
```

The full documentation of `iniabu` can be found [here](https://iniabu.rtfd.io).
Full examples in the form of jupyter notebooks
can be found [here](https://github.com/galactic-forensics/iniabu/tree/master/docs/jupyter_examples).
This package is completely rewritten from its first version.
It is also fully open source,
the code base is available on [our GitHub page](https://github.com/galactic-forensics/iniabu).
On that page are also instructions on how to install the latest development version,
how to install from source,
and how to contribute.

On the GitHub page
there is also a discussion section
where users are encouraged to share examples
and ask questions on usage.
Furthermore,
you can raise an issue
if you find a bug in the software,
would like some specific feature included,
or need help.

## InstrumentKit

The freely available <a href="https://github.com/Galvant/InstrumentKit" target="_blank">InstrumentKit</a> 
has been used to interact with hardware for the LION instrument
at Lawrence Livermore National Laboratory. 
Several classes have been contributed by us 
to this excellent compilation of tools. 
This allows you and anybody else in the world to utilize more tools,
might motivate you to continue down the Python path, 
and contribute your own instruments one day.


## Mahon Fitting

In order to fit a linear regression to measurements with uncertainties in both axes, the routine by <a href="https://www.tandfonline.com/doi/abs/10.1080/00206819709465336" target="_blank">Mahon (1996)</a>, also known as the “New York” regression, should be used. Along with the <a href="https://doi.org/10.3847/2041-8213/aabba9" target="_blank">Trappitsch et al. (2018)</a> publication we published a tool to easily apply the Mahon fitting routine to any dataset. The tool, including a detailed README file, can be found on <a href="https://github.com/LLNL/MahonFitting" target="_blank">the respective GitHub site</a>.

## Resonance Ionization Scheme Drawer

Would you like to make resonance ionization schemes like the one we show [here](/project/rims/) for titanium? Check out our <a href="https://github.com/RIMS-Code/RIMSSchemeDrawer" target="_blank">`RIMS Scheme Drawer`</a> software. This GUI allows you to draw your own resonance ionization schemes with just a few clicks and results in publishable figures.

<a href="https://github.com/RIMS-Code/RIMSSchemeDrawer" target="_blank">![RIMSSchemeDrawer](https://raw.githubusercontent.com/RIMS-Code/RIMSSchemeDrawer/master/examples/screenshot_titanium.png)</a>

## Coordinate Transformation

If you work with samples in various instruments, our coordinate transfer program might be of interest to you. Assuming you have coordinates for your particles, our program allows you easily transfer these coordinates from one system into the other. You can use fiducial marks or simply find some of your sample positions again and start from there. 

<a href="https://github.com/trappitsch/CoordinateTransformation" target="_blank">![Coordinate Transformation](https://raw.githubusercontent.com/trappitsch/CoordinateTransformation/master/docs/screenshot-full.png)</a>

Enjoy, and if you want, the source code is there for you as well!