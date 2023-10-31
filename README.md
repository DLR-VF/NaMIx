# NaMIx

[![DOI](https://img.shields.io/badge/doi-10.5281%2Fzenodo.8328622-blue)](https://doi.org/10.5281/zenodo.8328622)

NaMIx ("Sustainable mobility index to assess the location-related mobility potential", in German: 
"Nachhaltige-Mobilität-Index zur Bewertung des standortbezogenen Mobilitätspotentials") 
is a project that aims to develop an index for sustainable mobility at locations and 
for neighborhoods that incorporates existing data and indices and maps different spatial levels. You can find out more about the project here: https://verkehrsforschung.dlr.de/de/projekte/namix.

Most of the needed data can be retrieved from [OpenStreetMap](https://www.openstreetmap.org) (OSM). 
Public transport stops can be obtained from [OpenStreetMap (OSM)](https://wiki.openstreetmap.org/wiki/Public_transport) 
or [General Transit Feed Specification (GTFS)](https://gtfs.org/).

Please note that due to restrictions regarding the distribution of some of the used datatypes, we had to limit the functionality in comparison to what has been shown during the final project presentation. Given the current version, the locations of buildings are retrieved from [OSM](https://www.openstreetmap.org) instead of using the BKG address dataset. In addition, schools are retrieved from [OSM](https://www.openstreetmap.org) as well and instead of using access by foot to elementary schools and access by bike to secondary schools NaMIx version 0.2.0 computes the access to all schools obtained from [OSM](https://www.openstreetmap.org) by walk and by bike.

## Installation

The current version is "NaMIx-0.2.0". It computes ten indicators almost (see above) as presented at the final project presentation.

Please note that current NaMIx is realised as a Jupyter Notebook and that it is currently available in German only.

To run the computation, please do the following
* Download a version of NaMIx
: You may __download a copy or fork the code__ at [NaMIx&apos; github page](https://github.com/DLR-VF/NaMIx).
: Besides, you may __download the current release__ here:
  * [NaMIx-0.2.0.zip](https://github.com/DLR-VF/NaMIx/archive/refs/tags/0.2.0.zip)
  * [NaMIx-0.2.0.tar.gz](https://github.com/DLR-VF/NaMIx/archive/refs/tags/0.2.0.tar.gz)
* Depack the obtained file into a folder of your choice (named **&lt;NaMIx&gt;** from now on)
* Open the command line in this folder
* Optionally create a virtual python environment (recommended)
  * run ```python -m venv venv_namix```
  * run ```venv_namix\Scripts\activate.bat```
* Run ```pip install -r requirements.txt``` to install all necessary dependencies
* Download the 0.6.0 version of UrMoAC from [UrMoAC-0.6.0.zip](https://github.com/DLR-VF/UrMoAC/releases/download/v0.6.0/UrMoAC-0.6.0.zip). Extract the contents into **&lt;NaMIx&gt;**/demo/tools so that the jar file is located directly within this folder.
* Download GTFS data (e.g. from [MVG](https://www.mvg.de/services/fahrgastservice/fahrplandaten.html)). Extract the contents so that can be found in **&lt;NaMIx&gt;**/demo/input/GTFS.
* Start the jupyter notebook
  * You should have a command line open in **&lt;NaMIx&gt;**
  * Run ```python -m jupyter notebook```
  * open "namix_demo.ipynb" in the notebook

The notebook processes the input data, computes the individual indicators and the joined NaMIx indicator, and stores the result in a geopackage file named "**&lt;NaMIx&gt;**/demo/namix.gpkg".

## Authors

NaMIx was developed and implemented by [Serra Yosmaoglu](https://github.com/serrayos), Benjamin Heldt, [Daniel Krajzewicz](https://github.com/dkrajzew), and [Simon Nieland](https://github.com/SimonNieland).

## ChangeLog

**NaMIx 0.2.0** (31.10.2023)
* initial version

## License

**NaMIx** is licensed under the [Eclipse Public License 2.0]([LICENSE.md](https://github.com/DLR-VF/NaMIx/blob/main/LICENSE)).

**When using it, please cite it via the DOI: [![DOI](https://img.shields.io/badge/doi-10.5281%2Fzenodo.8328622-blue)](https://doi.org/10.5281/zenodo.8328622) (v0.2.0)**

## Support

If you have a usage question, please contact us via email (serra.yosmaoglu@dlr.de).

## Disclaimer
* We are not responsible for the contents of the pages we link to.
* The software is provided "AS IS".
* We cannot guarantee that the software works as you expect.

## References

* Boeing, G. (2017). OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks.
  Computers, Environment and Urban Systems 65, 126-139. doi:10.1016/j.compenvurbsys.2017.05.004
* Krajzewicz, D., Heinrichs, D. & Cyganski, R. (2017). Intermodal Contour Accessibility Measures Computation Using the 'UrMo Accessibility Computer'.
  International Journal On Advances in Systems and Measurements, 10 (3&4), Seiten 111-123. IARIA.
* Heldt, B., Yosmaoglu, S. (2023). Neues Planungswerkzeug für Quartiere: Der Nachhaltige-Mobilität-Index. Emmett. https://emmett.io/article/der-nachhaltige-mobilitaet-index.
  

