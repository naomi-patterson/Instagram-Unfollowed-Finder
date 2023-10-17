# Instagram Unfollowed Finder

## Overview
This repository has code, an executable, and instructions to extract a list of users who don't follow you back on Instagram.

## Get Started

First you'll need to request your data from Instagram. Follow the steps below:

<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_1.jpeg?raw=true" width="200">
<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_2.jpeg?raw=true" width="200">
<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_3.jpeg?raw=true" width="200">
<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_4.jpeg?raw=true" width="200">
<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_5.jpeg?raw=true" width="200">
<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_6.jpeg?raw=true" width="200">
<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_7.jpeg?raw=true" width="200">
<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_8.jpeg?raw=true" width="200">
<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_9.jpeg?raw=true" width="200">

After these steps, you'll need to wait for the download to be ready. This can take minutes, hours, or days. When ready, you'll receive an email notification, and will need to login on a computer to download the data. After downloading the data, extract it with an unzipping program to any folder on your computer, without changing the default name of `instagram-YOURUSERNAME`.

## Quickest Method

To get going as simply as possible, download the `unfollowed.exe` file and place it in the directory `instagram-YOURUSERNAME/followers_and_following`. 

<img src="https://github.com/naomi-patterson/Instagram-Unfollowed-Finder/blob/master/images/image_10.jpeg?raw=true" width="500">

Running the executable there will generate the list `not_followed_back.txt`, which contains the usernames of users who don't follow you back. From here, you can unfollow them manually on your account with that list, as you see fit.

If you're uncomfortable running a random .exe from the internet, I've also included instructions to run the python file and create your own executable below.

## Run Without The Executable

First ensure that Python is installed on your system. In any terminal, type `python` and press enter. If python is installed, this will activate an executing environment, which can be left by entering `exit()`. If Python is not installed, there will be an error, and you will need to install the programming language. Check online for instructions on how to do so.

With a working installation of Python, move `unfollowed.py` into the directory `instagram-YOURUSERNAME/followers_and_following`. The program can then be ran by entering `python unfollowed.py` in a terminal within that same working directory.

If you would like to create your own executable, run `pip install pyinstaller` followed by `pyinstaller -F unfollowed.py` in that same directory. This will generate `unfollowed.exe` in the folder `dist`, which gets created in the working directory.
