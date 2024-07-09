---
title: "Packaging Python CLIs and GUIs for air-gapped computers"

summary: "A lightning talk about how to package Python applications for air-gapped computers"

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2024-07-10"
# date_end: "2030-06-01T15:00:00Z"
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "2024-07-09"

authors: [reto]
tags: []

# Is this a featured talk? (true/false)
featured: false

#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

links:
# url_pdf: "files/presentations/2020-10-27-NuGrid/iniabu-slides.pdf"
url_slides: "files/presentations/2024-07-10_Python_Packaging/python_packaging.html"

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

Python is an amazing language when it comes to rapidly developing instrument control or data evaluation programs. However, when you want to package your program such that it can run on an air-gapped computer, the situation becomes a bit more tricky. In this very brief talk I give an overview of what tools are available and talk in more detail about [PyApp](https://ofek.dev/pyapp) and [box](https://box.rtfd.io), two tools that might can help with these tasks.
