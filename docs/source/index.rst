NaMIx User Guide
----------------

Here you can find information about how to install and use PtAC.

Getting Started
----------------
In order to run the library on a windows computer you have to have a recent Python version installed
(we recommend using Python `Anaconda <https://www.anaconda.com/products/individual>`_
or `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, which is a lightweight version of the conda environment).

Please also ensure that a `Java Development Kit <https://java.com/de/>`_ (preferably version 1.8) is installed
and that the folder containing the java.exe file is set in your path environment variable.
If you would prefer to set the JAVA_HOME (or JRE_HOME) variable via the command line:

* Open Command Prompt (make sure you Run as administrator so you're able to add a system environment variable).

* Set the value of the environment variable to your JDK (or JRE) installation path as follows

  .. code-block:: bash

     setx -m JAVA_HOME "C:\Program Files\Java\jdk1.8.0_XX"

* Restart Command Prompt to reload the environment variables then use the following command to check the it's been added correctly.

  .. code-block:: bash

     echo %JAVA_HOME%

**1. open the Anaconda prompt (can be found on windows start menu) and navigate to your home folder**

.. code-block:: bash

   cd C:\Users\YOUR_USERNAME

**2. generate a project folder and navigate to this folder**

.. code-block:: bash

   mkdir namix
   cd namix

**3. now, we can create a python virtual environment and install necessary dependencies
with** `conda <https://docs.conda.io/en/latest/>`_ **and activate the created environment**

.. code-block:: bash

   conda config --prepend channels conda-forge
   conda create -n namix --strict-channel-priority namix

**4. in the next step, activate the created environment**

.. code-block:: bash

   conda activate namix

(namix) should now be displayed in brackets at the starting of the line.

**5. You can install namix by typing**

.. code-block:: bash

   pip install namix

should look like this:

.. code-block:: bash

   (namix) C:\>pip install namix
   Looking in indexes: https://test.pypi.org/simple/
   Collecting namix
   Downloading https://test-files.pythonhosted.org/packages/32/b3/a3b687fb181cc584f4308655a895299494126474ad2cb4470fa67f8e3b3a/namix-0.0.1-py3-none-any.whl (13 kB)
   Installing collected packages: namix
   Successfully installed namix-0.0.1a

namix should be successfully installed, now. To be sure weather it works you might start python


.. code-block:: bash

   python

.. code-block:: bash

   (namix) C:\>python
   Python 3.8.10 | packaged by conda-forge | (default, May 11 2021, 06:25:23) [MSC v.1916 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

and then import the accessibility module of namix

.. code-block:: bash

   (namix) C:\>python
   Python 3.8.10 | packaged by conda-forge | (default, May 11 2021, 06:25:23) [MSC v.1916 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>> import namix.accessibility as accessibility
   >>>

if no error occurs the installation has been successful.

In order to try out the `examples <https://github.com/DLR-VF/NaMIx-examples>`_,
`jupyter notebook <https://jupyter-notebook.readthedocs.io/en/stable/index.html>`_ needs to be installed with the following command:

.. code-block:: bash

   conda install -c conda-forge notebook


Usage
-----
To get started with NaMIx, read the user reference and see sample code and input data in
`examples repository <https://github.com/DLR-VF/NaMIx-examples>`_.

Features
--------
PtAC is built on top of osmnx, geopandas, networkx and
uses `UrMoAC <https://github.com/DLR-VF/UrMoAC>`_ for accessibility computation.

* Download and prepare road networks from OpenStreetMap for accessibility calculation
* Calculate accessibilities from origins to the next destination
* Generate a population point dataset from population raster dataset
* Calculate Sustainable Development Goal 11.2.1 based on starting points with population information


User reference
--------------

.. toctree::
   :maxdepth: 2

   namix



Support
--------

If you have a usage question please contact us via email (serra.yosmaoglu@dlr.de).


License
--------

Copyright © 2023 German Aerospace Center (DLR)

This work is licensed under [Eclipse Public License 2.0 (EPL-2.0)](LICENSE/EPL-2.0.txt)

> **Hint:** We provided the copyright and license information in accordance to the [REUSE Specification 3.0](https://reuse.software/spec/).



Indices
==================

* :ref:`genindex`
* :ref:`modindex`
