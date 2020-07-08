---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Resonance Ionization Mass Spectrometry"
summary: "Analyzing micrometer-sized stardust grains for their trace-element isotopic compositions requires special instruments, such as resonance ionization mass spectrometers."
authors: []
profile: false
tags: []
categories: []
date: 2020-05-24T15:34:09-07:00
weight: 40

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

## The measurement challenge

Most of the large stardust grains are still only a few micrometers in size. Determining the trace element isotopic composition thus requries a very sensitive technique. In addition, the ideal technique should be able to determine between different isobars, i.e., be able to analyze isotopes of different elements that have the same mass, e.g., <sup>58</sup>Fe and <sup>58</sup>Ni, simultaneously. 

## Resonance ionization mass spectrometry

Resonance ionization mass spectrometry (RIMS) is an ideal technique to analyze such particles. The following animation shows schematics on how RIMS works.

![RIMS Animation](/img/projects/rims/rims_animation.gif)

   1. Overview of a RIMS instrument. On the left is the target / sample that should be analyzed. Then ion optics will guide the  ions in the time-of-flight mass spectrometer. In this part, ions are initially given the same energy and are then separated by mass over charge by the total flight time they take from the extractor to the detector. The blue box represents the resonance ionization lasers.
   2. Material from a sample (target) is removed by either using an ion beam or a desorption laser.
   3. After removing sample material a mixture of mostly neutral atoms and secondary ions (usually less than 1%) will be present above the samples.
   4. Since the secondary ions are generally noise in RIMS, they are ejected from the sampling area by applying a high voltage to the extraction optics. These secondary ions are given so much energy that they will fly into the back of the reflector and be neturalized there. They thus cannot reach the detector.
   5. Above the sample a cloud of neutral atoms is left behind.
   6. Resonance lasers ionize all isotopes of the elements of interest selectively creating photoions.
   7. By applying the correct voltages to the instrument the created photoions are extracted into the mass spectrometers and analyzed.

### Resonance ionization with Ti:Sapphire lasers

The advantage of RIMS is the ionization of neutral atoms by tunable, resonant lasers. First of all this process is highly effective since almost all of the atoms that come off in the removal event are neutrals. Further, resonance ionization means that multiple lasers are tuned to stepwise and resonantly excite an atom until it is singly ionized. The figure below for example shows an example for the ionization of titanium. 

![Ti Ionization Scheme](/img/projects/rims/ti_ionization_scheme.png)

This ionization scheme is taken from <a href="https://doi.org/10.1039/C8JA00269J" target="_blank">Trappitsch et al. (2018)</a>. Shown are mutliple transitions for titanium, all of which are highly selective and effective for only this specific element, here titanium. Thus, other elements with potentially overlapping isobars are not ionized.

### Mass spectra

The figure below shows a mass spectrum recorded by RIMS for the quasi-simultaneous analysis of iron and nickel. 

![RIMS Mass Spectrum for Iron and Nickel](/img/projects/rims/feni_ms_sep.png)

While iron and nickel have an overlapping isobar at mass 58, the ionization of nickel was delayed by several hundred nanoseconds with respect to the ionization of nickel. In the time-of-flight mass analyzer this separation resulted in a separation of these two identical masses allowing the simultaneous detection of <sup>58</sup>Fe and <sup>58</sup>Ni. RIMS thus, compared to other techniques, allows us to analyze elements with inherent isobaric overlaps simultaneously for all isotopes.


## Instruments

Currently only two RIMS instruments are being used for cosmochemistry worldwide, both of which I have worked on. These instruments are the <a href="https://geosci.uchicago.edu/research/planetary-sciences-and-cosmochemistry/" target="_blank">CHILI (Chicago Instrument for Laser Ionization) instrument at the University of Chicago</a> and the <a href="https://str.llnl.gov/january-2017/isselhardt" target="_blank">Livermore LION (Laser Ionization of Neutrals) instrument at Lawrence Livermore National Laboratory</a>.

![LION at LLNL](/img/projects/rims/lion400px.jpg) 

The image above shows the LION instrument. The mass spectrometer can be seen on the right side, however, the reflectron (in this setup the top of the instrument) is outside the field of view. The center and left part shows the six tunable Ti:Sapphire lasers which allow the simultaneous ionization of various different elements.
