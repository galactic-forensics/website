[![Deploy](https://github.com/galactic-forensics/website/actions/workflows/deploy.yml/badge.svg)](https://github.com/galactic-forensics/website/actions/workflows/deploy.yml)

# Galactic Forensics Laboratory Website

This is the readme file for sustaining the galactic forensics laboratory website. The readme file for the Hugo Academic theme can be found [here](README_Academic.md).

## Manging this website

A detailed readme,
that also applies to this website,
can be found [here](https://github.com/livingpatterns/livingpatterns-website/blob/master/README.md)

**Note**: The website is built with Hugo v0.72.0.
The binaries for this release can be found [here](https://github.com/gohugoio/hugo/releases/tag/v0.72.0).
An installation guide can be found 
[here](https://gohugo.io/getting-started/installing/).


## Clone the website to a new computer

```bash
git clone https://github.com/galactic-forensics/website.git
cd website
git submodule update --init --recursive
```

Alternativley, clone via SSH.

## Building the website

After pushing to the `main` branch,
github actions automatically build the website
and push the files to the `gh-pages` branch.
