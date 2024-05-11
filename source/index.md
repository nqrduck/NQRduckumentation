# Welcome to the NQRduckumentation!

![NQRduck Logo](_static/Logo_full.png)

This program is intended as an educational tool for magnetic resonance experiments (NMR, NQR, ...). Its focus lies on modular behaviour depending on what nqrduck modules are installed. 

::::{grid} 2
:::{grid-item-card}  {fas}`wrench;pst-color-primary` Installation
The NQRduck can be easily installed via pip. Additional modules can be installed via an included install wizard.
:::
:::{grid-item-card} {fas}`book;pst-color-primary`  Tutorials
There exists a range of different modules for the NQRduck software. The tutorials range from simulation to magnetic resonance experiments.
:::
:::{grid-item-card} {fab}`python;pst-color-primary`  Python 
The NQRduck comes with a user friendly PyQt6 based user interface. 
:::
:::{grid-item-card} {fas}`tape;pst-color-primary`  API Reference
API Documentation of the program can be found [here](tutorials/index.md)
:::
::::

The core of the program is the nqrduck. It provides a central interface for communication between the different modules. The nqrduck core loads all the installed modules in your python environment.

The focus for spectrometers currently lies on LimeSDR based spectrometers (LimeSDR USB, LimeSDR Mini 2.0).

```{toctree}
:maxdepth: 1
:caption: Contents:

tutorials/index
api_reference/index
```
   
## NQRduck core


