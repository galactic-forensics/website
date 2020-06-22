---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "The Solar Nebula"
summary: "The solar nebula, from which our Solar System formed, represents Milky May material after 9 Ga of galactic chemical evolution. Solar System samples, such as meteorites, contain important information to study our neighborhood."
authors: []
profile: false
tags: []
categories: []
date: 2020-05-24T15:34:09-07:00
weight: 30

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

## The composition of the solar nebula

The solar system formed around 4.5 billion years ago, which is around 9 billion years after the formation of the Milky Way itself. This means that the average solar composition that the solar nebula started with represents one datapoint in terms of galactic chemical evolution.

The solar composition can be measured excellently by observing the sun as well as by analyzing primitive meteorites. Except for volatile species, e.g., hydrogen and the noble gases, the composition of these two sample sets agree very well with each other. However, there are some anomalies that can be found in meteorites, which are very indicative of the exact circumstances under which the solar system formed.

## Short-lived radionuclides
Some of the anomalies that can be found in primitive objects from the solar system are enhancement in certain isotopes due to the in situ radioactive decay of short-lived radionuclides (SLRs). Calcium aluminum-rich refractory inclusions (CAIs), which are fluffy looking phases in primitive meteorites, are some of the very first material that condensed in the solar nebula and are the ideal samples to look for such anomalies.

### How to determine the abundance of SLRs in the solar nebula

If for example the short-lived <sup>60</sup>Fe was incorporated into a solid that condensed early on in the solar system we would be able to measure it today as an enhancement of <sup>60</sup>Ni since the original <sup>60</sup>Fe, which has a half-life of 2.6 Ma, would have all decayed to its stable daughter by now. The figure below shows how the presence of SLRs can be detected in a given sample.

![Schematic on Measuring an Isochron](/img/projects/slrs/fe60_isochron.png)

The figure on left shows the scenario at formation. Different minerals condense with different amounts of iron to nickel elemental compositions. The figure in the middle shows what happens with these different phases once they are solidified. The y-axis here always shows the <sup>60</sup>Ni/<sup>58</sup>Ni ratio. The more iron a phase condensed with the more <sup>60</sup>Fe it will have incorporated as well. Thus, once all the <sup>60</sup>Fe has decayed to <sup>60</sup>Ni the phases will end up with different <sup>60</sup>Ni/<sup>58</sup>Ni ratios. The figure on the right shows the scenario today. By measuring different phases for their Fe/Ni elemental ratio (shwown on the x-axis) and their nickel isotopic composition (y-axis), the original value of the <sup>60</sup>Fe/<sup>56</sup>Fe at the time of condensation can be determined by fitting a line to these measurements. In above example this line will have the form:

$$\frac{^{60}\rm{Ni}}{^{58}\rm{Ni}} = \left(\frac{^{60}\rm{Fe}}{^{56}\rm{Fe}}\right)_ 0 \times \frac{^{56}\rm{Fe}}{^{58}\rm{Ni}} + \left(\frac{^{60}\rm{Ni}}{^{58}\rm{Ni}}\right)_ 0$$

Here, the isotope ratios with subscript 0 represent the initial composition of the isotope ratio when the phase condensed. The original <sup>60</sup>Fe/<sup>56</sup>Fe ratio is thus nothing else than the slope of the regression.

Assuming that an SLR was distributed homogeneously in the early solar system allows to also date phases relative to each other. For example, if one phase shows half the initial <sup>60</sup>Fe/<sup>56</sup>Fe than another phase we can say that the phase with less initial <sup>60</sup>Fe condensed one <sup>60</sup>Fe half life (2.6 Ma) after the first one.

### The presence of <sup>26</sup>Al and its effects

One of the most prominent SLRs that has been shown to be present in the solar nebula is <sup>26</sup>Al (half life 717 ka). Many studies have shown that <sup>26</sup>Al was distributed homogeneously in the solar nebula and that its initial abundance when CAIs formed was $$^{26}\rm{Al}/^{27}\rm{Al} = 5\times10^{-5}$$. This has important implications because it allows us to date different phases in the early solar system relative to each other. Furhtermore, when <sup>26</sup>Al decays to <sup>26</sup>Mg it releases 4 MeV of energy. This is a significant amount and has been shown to be able to heat an asteroid parent body of a given size (and thus of a given <sup>26</sup>Al content) significally. In fact, <sup>26</sup>Al has been invoked as being a crucial heat source that started the differentiation of early planetesimals.

The presence of <sup>26</sup>Al in the solar system raises the quesion on where it came from. Since its half-life is only 717 ka it had to be produced just prior to solar system formation. The key to decipher where it came from comes from studying other SLRs that were also present in the solar nebula.

### The curious case of <sup>60</sup>Fe in the solar nebula

One nuclide that can help us solve the question on where the <sup>26</sup>Al in the early solar system came from is <sup>60</sup>Fe. If <sup>60</sup>Fe is also present in the solar nebula it was likely produced and injected along with <sup>26</sup>Al. A large amount of <sup>60</sup>Fe in the early solar nebula, by which we mean a value of $$^{60}\rm{Fe}/^{56}\rm{Fe} > 5\times10^{-7}$$ would make it likely that a supernova that exploded just before the solar system produced and injected the two nucldies. A low value of $$^{60}\rm{Fe}/^{56}\rm{Fe} \sim 10^{-8}$$ would however indicate that no such supernova took place and that the <sup>60</sup>Fe does not need to be produced but is rather the galactic background value. 

This discussion might seem very fabricated, however, for years and years the community has argued over the amount of <sup>60</sup>Fe present in the solar nebula and the mentioned values are not just randomly picked. In situ studies of chondrules, objects that formed in the solar system about 2 Ma after CAIs, by secondary ion mass spectrometry (SIMS) showed high <sup>60</sup>Fe values and thus pointed towards a supernova source. Bulk studies of many meteorites on the other hand consistently measured low <sup>60</sup>Fe values. Until recently, the in situ measurements could not be tested with other techniques than SIMS. 

In a <a href="https://doi.org/10.3847/2041-8213/aabba9" target="_blank">recent publication</a> we re-analyzed one chondrule with [resonance ionization mass spectrometry (RIMS)](/research/04-rims). This sample has previously only been studied with SIMS. RIMS has the advantage over SIMS that all nickel isotopes can be measured without interferences. SIMS however can only anlyze <sup>60</sup>Ni, <sup>61</sup>Ni, and <sup>62</sup>Ni. In order to determine the excess in <sup>60</sup>Ni the measurements needs to be normalized to another isotope (see isochron figure above). Furthermore, <a href="https://en.wikipedia.org/wiki/Isotope_fractionation" target="_blank">mass dependent fractionation</a> also has to be corrected for, thus measuring a third isotope is required. 

![Nickel isotopes in DAP1](/img/projects/slrs/ni_isos_dap1.png)

The above figure shows the new results obtained by RIMS (left, <a href="https://doi.org/10.3847/2041-8213/aabba9" target="_blank">Trappitsch et al., 2018</a>) versus a re-evaluation of the old results by SIMS (right, <a href="https://doi.org/10.1016/j.gca.2017.06.013" target="_blank">Telus et al., 2018</a>). To evaluate the SIMS measurements requires doing the described corrections with the low abundance isotope <sup>61</sup>Ni. This results in extreme correlations of the uncertainties, which, if not adequately accounted for, can seem like excesses in <sup>60</sup>Ni due to in situ decay of <sup>60</sup>Fe. With RIMS however this problem does not exist. The figure on the left clearly shows that the errors are uncorrelated thanks to the ability to measure <sup>58</sup>Ni. 

Our recent re-evaluation has brought up issues with the data processing that has been done in the determination of the initial <sup>60</sup>Fe abundance. It remains to be seen if this is the case for all samples, however, preliminary evaluations of other SIMS measurements show that the same problem occurs in the rest of the dataset. A supernova thus cannot have injected the <sup>26</sup>Al and another source, e.g., <a href="https://doi.org/10.3847/1538-4357/aa992e" target="_blank">a Wolf-Rayet star</a>, is required to explain its high value in the solar nebula.
