---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Galactic Chemical Evolution"
summary: "The Big Bang only formed Hydrogen, Helium, and traces of Lithium. The evolution of elements since then is termed galactic chemical evolution."
authors: []
profile: false
tags: []
categories: []
date: 2020-05-24T15:34:09-07:00
weight: 20

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

## From the Big Bang to today

Galactic chemical evolution (GCE) is the field that studies how elements evolved in the universe. The big bang only produced hydrogen, helium, and a little bit of lithium. Aside from beryllium and boron, all other elements formed in stars in a process called nucleosynthesis. Depending on their initial masses stars undergo very different developments. A massive star can explode as a supernova at the end of its life while a low-mass star does not have enough energy stored up in order to explode so violently. Different elements and isotopes are associated with the production in different stellar environments. Galactic chemical evolution describes how this evolution of the elements took place since the beginning of the universe and is thus often described as galactic archeology. Below artistic impression (by Jenny Mottar, NASA) beautifully summarizes GCE in one image: from the big bang to complex molecules and the earth everything originates as stardust.

![GCE by Jenny Mottar](/img/projects/gce/gce_mottar.jpg)

## Metallicity 
The periodic chart of the elements as chemists use it can be hard to
remember, however, it is fairly easy for astronomers. In the
astronomical sense, the universe consists of hydrogen, helium, and metals (yes,
in the astronomical sense you breathe metals). The amount of metals in a star
with respect to hydrogen is called the metallicity. Mass fractions of hydrogen
to helium to metals are usually written in astronomy with the letters *X*, *Y*,
and *Z*, respectively. The mass fractions of hydrogen, helium, and metals in the
sun for example are: *X*<sub>sun</sub> = 0.7381, *Y*<sub>sun</sub> = 0.2485, and
*Z*<sub>sun</sub> = 0.0134. Knowing this number for the sun, any star's
metallicity can be expressed in terms of the solar metallicty. Metallicity can
however also be expressed as a chemical abundance ratio. Here, the abundance of
iron is often measured in a star and used as a proxy for the total metallicity.
This abundance ratio is typically written as:

$$ [\rm{Fe}/\rm{H}] = \log_{10} \left( \frac{N_{\rm{Fe}}}{N_{\rm{H}}} \right)_{\rm{star}} - \log_{10} \left( \frac{N_{\rm{Fe}}}{N _{\rm{H}}} \right)_{\rm{sun}}$$

Since the big bang did not produce metals a first order GCE model can assume that the metallicity of an object is correlated to its age, i.e., an older object started out with a lower metallicty. This is assumption is correct up to a certain degree, however, breaks down when looking at the details of GCE.


## Observables

### Astronomical observations

Traditionally GCE is studied in detail by astronomical observations, specifically spectroscopy. This allows the determination of the elemental composition of stars and, in for certain elements, their isotopic composition. A variety of different stars can be observed, which allows us to study the distribution of elements within the galaxy. Furthermore, different stars have different ages. The elemental starting comopsition of a given star will be observable throughout most of its life, thus astronomical observations also allow us to look at GCE in time. 

### Stardust grain measurements

Stardust grains also allow us to study GCE. While the elemental composition of these grains is primarily dominated by the chemistry of the condensing stellar outflow and is thus not representative of the parent star's composition, stardust grains are excellent tracers for the isotopic comopsition of stars. 

#### Silicon isotopes in mainstream grains and the puzzling conclusion

The figure below shows the silicon isotopic composition of all mainstream SiC stardust grains from low-mass stars taken from the <a href="https://presolar.physics.wustl.edu/presolar-grain-database/" target="_blank">presolar grain database</a>. Plotted are all measurement that have isotope ratio measurements with lower than 10‰ uncertainties. 

![SiC Stardust Silicon Isotopes](/img/projects/gce/sic_si_isos.png)

The axes labels are in delta units and describe the deviation of the sample from a standard (here the solar average) in per thousands:

$$ \delta ^{i}\rm{Si}_{28} = \left[\frac{\left(\frac{^{i}\rm{Si}}{^{28}\rm{Si}}\right) _{\rm{sample}}}{\left(\frac{^{i}\rm{Si}}{^{28}\rm{Si}}\right) _{\rm{standard}}} - 1\right] \times 1000 $$

The dashed line at the origin of the plot represents the solar isotopic composotion of silicon. 

From GCE calculations we expect that <sup>28</sup>Si forms early on and that the isotopes <sup>29</sup>Si and <sup>30</sup>Si form later on from <sup>28</sup>Si. Silicon-28 is thus also called a primary isotope, while <sup>29,30</sup>Si are secondary isotopes. We know however that presolar grains are older than the solar system, thus the material from which their stars formed came together before the solar system formed. A low-mass star, such as each parent star of a grain shown in the figure above, does not effectively produce <sup>29</sup>Si and only produces a little bit (a few tens of ‰) of <sup>30</sup>Si. Silicon isotopes are thus excellent proxies to study GCE. 

What is going on then in the figure above? A lot of the grains are clearly enriched in <sup>29</sup>Si and <sup>30</sup>Si compared to the solar system. In the age-metallicity correlated GCE picture these grains thus seem younger than the solar system. The silicon isotopic composition of presolar grains thus clearly requires that GCE takes place more heterogeneously. 

#### Other GCE proxies tell the same story

In a <a href="https://doi.org/10.1016/j.gca.2017.05.031" target="_blank">recent study</a> we tested if the same holds true for the isotopic composition of iron and nickel. The best isotopes to use as GCE proxies here are <sup>54</sup>Fe and <sup>60</sup>Ni. The figure below shows our results:

![Iron and Nickel Results in Presolar SiC Grains](/img/projects/gce/gce_fe_ni_trappitsch18_380px.png)

The dashed, purple line shows the GCE model by <a href="https://doi.org/10.1111/j.1365-2966.2011.18621.x" target="_blank">Kobayashi et al. (2011)</a> in comparison with our measurements. This linear GCE model ends at solar composition and for older objects shows a decrease in <sup>54</sup>Fe and an enhancement in <sup>60</sup>Ni. Many of the measured stardust grains look more evolved than the solar system itself, which agrees with the silicion isotopic measurements and also requries GCE to take place heterogeneously.

Measurements of stardust grains along with astronomical observations yield important constraints for our understanding of GCE. Astronomical observations are often limited to determine the elemental abundance. Stardust grains on the other hand don't allow us to determine their exact parent star, however, enable an excellent understanding of the isotopic evolution of GCE. The two techniques are thus highly complementary for studying GCE.