<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Home Automator" />

  &#xa0;

  <!-- <a href="https://homeautomator.netlify.app">Demo</a> -->
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
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/webnizam" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

The purpose of this proof of concept project is to demonstrate the capability of controlling lights in a home environment using Jetson Nano and OpenCV with the aid of a trained classification model. The model has been trained to recognize the open and closed states of the entrance door. The lighting control system is integrated with Homebridge, which has already been set up. The application continuously monitors the entrance door and based on its open or closed state, it will toggle the lights accordingly.

This project is open source and free to modify to meet individual requirements.

## :sparkles: Features ##

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

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

# Build Docker Image
$ run ./build.sh

# Run the project
$ run ./run.sh

# The server will initialize in the <http://locahost:8000>
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/webnizam" target="_blank">Nizamuddin Mohamed</a>

&#xa0;

<a href="#top">Back to top</a>
