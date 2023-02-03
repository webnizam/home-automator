<div id="top"></div>
<div align="center">
  
[![Generic badge](https://img.shields.io/badge/NVIDIA-Jetson-brightgreen.svg)](https://shields.io/)
![](https://img.shields.io/badge/Language-Python-blue)
[![Generic badge](https://img.shields.io/badge/SHELL-Bash-orange.svg)](https://shields.io/)
  
</div>

<h1 align="center">Home Automator</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/webnizam/home-automator?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/webnizam/home-automator?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/webnizam/home-automator?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/webnizam/home-automator?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/webnizam/home-automator?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/webnizam/home-automator?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/webnizam/home-automator?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Home Automator 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="https://github.com/webnizam/home-automator/blob/main/LICENSE.md">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/webnizam" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

The objective of this proof of concept project is to showcase the feasibility of utilizing Jetson Nano and OpenCV in combination with a trained classification model to control lighting in a residential setting. The classification model has been specifically trained to distinguish between open and closed states of the entrance door. The lighting control system is seamlessly integrated with Homebridge for easy operation. The application constantly monitors the entrance door and adjusts the lighting accordingly.

Please note that the model provided with the repository has been trained for a specific environment and for optimal results, it is recommended to train the model for your specific environment.

This project is open source and available for modification to meet individual requirements and preferences.

## :sparkles: Features ##

:heavy_check_mark: Turn on Lights on Opening Door
:heavy_check_mark: Turn off Lights on Closing Door

## :rocket: Technologies ##

The following tools were used in this project:

- [PyTorch](https://pytorch.org/)
- [OpenCV](https://opencv.org/)
- [Python](https://www.python.org/)
- [Homebridge](https://homebridge.io/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed in your Jetson Nano.

Please refer https://github.com/mstatt/jetson-interface_installer for more details on setting up Jetson Nano.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/webnizam/home-automator

# Access
$ cd home-automator

# Copy .env
$ cp .example.env .env

# Edit .env values
$ nano .env

# Build Docker Image
$ run ./build.sh or bash build.sh

# Run the project
$ run ./run.sh or bash run.sh

# The server will initialize in the http://{jetson-ip}:8000
```

## Contact

Project Link: https://github.com/webnizam/home-automator

Nano Certification URL:
https://courses.nvidia.com/certificates/84a55e8ae6304f608f1cb463bf6b9784

Project Video:
https://drive.google.com/file/d/1MuVffLJt0nN_7qyRL796qWcyVm70C634

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/webnizam" target="_blank">Nizamuddin Mohamed</a>

&#xa0;

<a href="#top">Back to top</a>
