# TESS Workshop Tutorials

## [TESScut and ExoMAST: Working with TESS Time Series Data](tesscut_exomast/TESScut_ExoMAST_Tutorial.ipynb)

Learn about MAST's programmatic tools for accessing TESS time series data while exploring weird looking light curves.  This tutorial will show users how to follow up on unusual TCE results using the MAST API in Python to access and view TESS time series and FFI data.

Topics to be covered include:
- Using the MAST API to get data validation time series
- Plotting TESS light curves in Python
- Using the MAST API to make an FFI cutout
- Creating a movie of TPF frames in Python

[Extra exercises](tesscut_exomast/TESScut_ExoMAST_exercises.ipynb)


## [starry: Fast light curve modeling for TESS](starry/)

Learn how to use [starry](https://rodluger.github.io/starry) to model TESS light curves and infer the surface properties of variable stars. We'll discuss how to use `starry` to model rotational light curves and occultation light curves of stars (and planets) with arbitrary surface features (such as spots, clouds, or even continents). Since the algorithm in `starry` is analytic, the modeling is extremely fast, and you'll be a stellar cartographer in no time!

The two tutorials we'll cover are
- [An introduction to `starry`](starry/Introduction.ipynb)
- [Mapping stellar surfaces with `starry`](starry/StarspotMapping.ipynb)

## [eleanor: Simple light curve extraction from TESS FFIs](eleanor/eleanor_tess_workshop.ipynb)

Learn how to use [eleanor](http://adina.feinste.in/eleanor/) to extract light curves for sources in the TESS Full-Frame Images (FFIs). We'll discuss the basics of what is in an eleanor light curve product, the best practices with the data, and how to customize your own light curves. By the end, you'll have all the tools to start finding your own new planet candidates, eclipsing binaries, recovering supernovae, etc. etc.!

Everything you need to know about eleanor will be covered in the [tutorial notebook](eleanor/eleanor_tess_workshop.ipynb)

## [exoplanet: Gradient-based inference to exoplanet data analysis](exoplanet/)

Learn how to use [PyMC3](https://docs.pymc.io) and [exoplanet](https://exoplanet.dfm.io/en/stable) to model TESS light curves. exoplanet provides the tools needed to use gradient-based inference methods for modeling exoplanets and stellar variability in photometric and radial velocity time series. These methods (like the [No-U-Turn Sampler](https://arxiv.org/abs/1111.4246)) are much more efficient than tools like [emcee](https://emcee.readthedocs.io) for modeling problems with large numbers of parameters, for example multi-planet systems.

The two tutorials are:
1. [Fitting a line to data with PyMC3](exoplanet/01_line.ipynb) where we fit a mass-radius relation for small planets, and
2. [Fitting a transit model to TESS data](exoplanet/02_transit.ipynb) where we fit the FFI light curve of Pi Mensae to model the recently discovered transiting planet in that system.


## [lightkurve: A friendly package for TESS time series analysis in Python](lightkurve/workshop/)

Learn how to use the [Lightkurve](https://docs.lightkurve.org) package to create, detrend, and analyze custom light curves from Kepler and TESS pixel data:
- Tutorial: [Workshop.ipynb](lightkurve/workshop/Workshop.ipynb)
- Exercise 1: Extracting light curves using different masks ([Exercise_1.ipynb](lightkurve/workshop/Exercise_1.ipynb) | [Exercise_1-Solutions.ipynb](lightkurve/workshop/Exercise_1-Solutions.ipynb))
- Exercise 2: Building a light curve from two different sectors ([Exercise_2.ipynb](lightkurve/workshop/Exercise_2.ipynb) | [Exercise_2-Solutions.ipynb](lightkurve/workshop/Exercise_2-Solutions.ipynb))


## [bls: Finding planet candidates using the Box Least Squares (BLS) algorithm](bls/bls-tutorial.ipynb)

This tutorial demonstrates usage patterns for the brand new `astropy.stats.bls` module to identify transiting planet candidates using the Box Least Squares (BLS) algorithm.
If you are already familiar with AstroPy and BLS, you may prefer to head straight to the [AstroPy BLS documentation](http://docs.astropy.org/en/latest/stats/bls.html).
If Python or BLS are new to you, this tutorial will provide you with step-by-step instructions on how to get started.

- Tutorial: [bls-tutorial.ipynb](bls/bls-tutorial.ipynb)
- Exercises: [bls-tutorial.ipynb#Exercises](bls/bls-tutorial.ipynb#Exercises)


# Additional Example Notebooks

## [Retrieve Data from Amazon S3 Cloud](aws_cloud_retrieval/aws_cloud_data_retrieval.ipynb)
