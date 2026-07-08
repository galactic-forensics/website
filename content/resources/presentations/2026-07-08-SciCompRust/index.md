---
title: "Oxidizing cryogenic sample storage in ultra-high vacuum"

summary: Presentation at Scientific Computing in Rust Workshop 2026

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2026-07-08"
# date_end: "2030-06-01T15:00:00Z"
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "2026-07-08"

authors: [reto]
tags: []

# Is this a featured talk? (true/false)
featured: false

#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

links:
url_pdf: "files/presentations/2026-07-08_SciCompRust/trappitsch_sci_comp_rust_2026_slides.pdf"

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
# projects:
# - internal-project

# Enable math on this page?
math: true
---
To store frozen research sample after sample preparation and prior to analysis, a storage chamber that keeps them at 120 K temperature and in ultra-high vacuum (~1e-9 mbar) is required. In this talk I will discuss the development and integration of the control electronics, firmware, and host software with user-interface that now controls our home-built cryostorage solution.

Controlling the chamber requires (a) control of certain parts via digital I/O lines, (b) communication with several existing instruments via established protocols (e.g., via RS-232), (c) reading, updating, and displaying the current status of the chamber and attached instruments, and (d) interfacing with the user. Electronics for task (a) was designed in-house and uses a RaspberryPi Pico2 board as the controlling MCU. Firmware for this MCU was written in Rust using embassy. This firmware communicates with our Rust-based host software (which takes care of tasks (c) and (d)) using postcard and postcard-rpc. Finally, we also developed Rust crates to communicate with various instruments via RS-232, RS-485, and OPCUA. The host software and touch-driven user interface runs on a Seeedstudio ReTerminal DM, a RaspberryPi compute module 4 based Linux computer with a 10" touch screen. The user interface was developed using Slint.

In summary: Our brand-new cryostorage chamber is already Rusty all over.
