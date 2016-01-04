Using Python for Astronomical Data Analysis
===========================================

| `227th AAS Meeting <http://aas.org/meetings/aas227>`_
| Monday, 4 January 2016
| 9:00am - 12:00pm, 1:30pm - 4:30pm
| Room: St. George 114
| Fee: $35
| Instructors:  Larry Bradley, Nadia Dencheva, Tim Pickering, and Erik Tollerud
| Speaker:  Jason Kalirai
|

This workshop will cover the use of Python tools to analyze
astronomical data, with the focus primarily on Optical, IR and UV data
analysis tools. The primary tools that will be covered are those
available in the Astropy library and affiliated packages. The specific
tools to be covered will be:

* Physical units and quantities
* Basics on accessing data files, both FITS and ascii tables
* Coordinate utilities
* Modeling and Fitting
* Photometric tools
* Interactive visualization and analysis tools:

  - Glue
  - imexam
  - specview

There will be time spent on hands-on exercises. Instructions on
installing the necessary software will be provided before the workshop
and help will be available at the workshop for those that experience
problems with installations.

The prerequisites are a familiarity with astronomical data analysis.
Basic Python experience is highly recommended to be able to
participate in the exercises. Those without Python experience will
still get much useful information about the capabilities for data
analysis in Python. Experience with Python scientific libraries,
particularly numpy and matplotlib, is helpful, but not required.


Installation Requirements
-------------------------

To follow along with the tutorials and to do the exercises, you will
need to have the following packages installed:

* Python 2.6 (>= 2.6.5), 2.7, or >= 3.3
* IPython (>= 4.0) and Jupyter Notebook (>= 1.0)
* Numpy >= 1.6
* Scipy >= 0.15
* Pandas >= 0.17
* xlwt >= 1.0
* matplotlib >= 1.3
* Astropy 1.1
* Photutils 0.2
* scikit-image >= 0.11
* astroquery >= 0.2.6 (not strictly needed, but makes the coordinates tutorial more straightforward)
* Glue
* imexam
* astroquery

You can run the ``check_env.py`` script to check your Python
environment for the required dependencies::

  % python check_env.py

Some quirks you might run into:

* ``glue`` is installed as ``glueviz`` (e.g. ``conda install glueviz``)
* ``skimage`` is ``scikit-image`` (e.g. ``conda install scikit-image``)
* If you're using anaconda or miniconda, you should use the astropy channel for conda to install photutils and astroquery:

``conda install -c http://conda.anaconda.org/astropy photutils astroquery``

Schedule
--------

+------------------+-------------------------------------------------+
|     Time         |   Topic                                         |
+==================+=================================================+
| 8:00 - 9:00 am   | Installation help                               |
+------------------+-------------------------------------------------+
| 8:30 - 9:00 am   | Breakfast                                       |
+------------------+-------------------------------------------------+
| 9:00 - 9:15 am   | Astropy Overview (Erik T; 15 min)               |
+------------------+-------------------------------------------------+
| 9:15 - 10:00 am  | Numpy Intro, Units (Larry; 45 min)              |
+------------------+-------------------------------------------------+
| 10:00 - 10:30 am | Tables, FITS, ASCII tables Part 1 (Tim; 30 min) |
+------------------+-------------------------------------------------+
| 10:30 - 10:45 am | Break (15 min)                                  |
+------------------+-------------------------------------------------+
| 10:45 - 11:15 am | Tables, FITS, ASCII tables Part 2 (Tim; 30 min) |
+------------------+-------------------------------------------------+
| 11:15 am - 12 pm | Coordinates (Erik T; 45 min)                    |
+------------------+-------------------------------------------------+
| 12:00 - 1:30 pm  | Lunch                                           |
+------------------+-------------------------------------------------+
| 1:30 - 1:45 pm   | Cosmology (Erik T; 15 min)                      |
+------------------+-------------------------------------------------+
| 1:45 - 2:40 pm   | Modeling, Fitting, WCS (Nadia; 55 min)          |
+------------------+-------------------------------------------------+
| 2:40 - 3:00 pm   | JWST: Preparing for Cycle 1 (Jason; 20 min)     |
+------------------+-------------------------------------------------+
| 3:00 - 3:15 pm   | Break (15 min)                                  |
+------------------+-------------------------------------------------+
| 3:15 - 4:00 pm   | Photutils (Larry; 45 min)                       |
+------------------+-------------------------------------------------+
| 4:00 - 4:30 pm   | GUI (Glue, imexam, specview) (Tim; 30 min)      |
+------------------+-------------------------------------------------+

AAS Survey
----------
If you participated in the workshop, the AAS asks that you please fill out the survey at http://bit.ly/aas227profdev
