# TINY JARVIS

Tiny_Jarvis is a local, portable AI assistant that lives on a Raspberry Pi 5 with a custom-made HAT, stereo analog speakers, and a small OLED screen. It can play songs, set timers and answer most questions in general. Plus, it's voice-controlled!

It allows for infinite creativity as to what it can do. In my case, for instance, I use it to help me with cooking. It chooses a recipe, displays the ingredients and guides me through the recipe out loud. Tiny Jarvis also sets a timer for the oven, or even for the washing machine in college.

During the day, it grabs the 15 main headlines from BBC World and chooses the three that have the most impact. It then reads the corresponding articles, and generates a summary of each one!

Up to you now to add any features you want to.

![image](https://cdn.hackclub.com/01a01e08-cb3f-7aaf-9e4b-f9ef1785e805/IMG_5995.jpeg)

## Table of contents:

 - [Quickstart](#quickstart)
 - [Features](#features)
 - [How it works](#how-it-works)
 - [Hardware](#hardware)

# Quickstart

## Prerequisites

<b>OS recommendation:</b> Raspberry Pi OS Lite (64-bit)

Before doing anything, clone the repo:
```bash
sudo apt update
sudo apt install git
git clone https://github.com/LouisD2008/Tiny_Jarvis.git
```

## Dependencies:

Run the `install.sh` script by running:
```bash
chmod +x install.sh
./install.sh
```
You may of course choose a different AI model if you wish, but this is the current recommended one for a Raspberry Pi 5.\
Feel free as well to choose a different Piper TTS voice!

> Note: this will affect the output time


# Features

 - "Play ..." --> Tiny Jarvis will search and play music from YouTube Music using natural voice commands. (This only works when connected to wi-fi)
 - "Cooking ..." --> Tiny_Jarvis will output a random recipe from a list with over 50 simples recipes, display the ingredients, and read the recipe out loud.
 - "Set a timer of ... minutes" --> Tiny_Jarvis will set a timer for the needed time, and display it in real time on the OLED screen.
 - "Flip a coin..." --> self-explanatory
 - "What's the news?" --> Tiny_Jarvis will choose between 15 daily headlines from BBC World for the 3 most impactful, read the articles and generate three 3-4 sentence summaries.
 - Idle screen: system metrics screen


# How it works

 - User presses a button, gives a command, and releases the button when done speaking.
 - The captured audio is translated into text by [faster-whisper](https://pypi.org/project/faster-whisper/0.3.0/).
 - That text is given as a prompt to a model of your choice using [llama.cpp](https://github.com/abetlen/llama-cpp-python) (optimized for Raspberry pi 5), preferably a low-parameter model like Llama-3.2-3B, balancing speed and quality.
 - The model's ouput is streamed into [Piper TTS](https://github.com/rhasspy/piper), a text-to-speech model, and played through the speakers (stereo sound) thanks to digital-to-analog amplifiers, which allows for good sound quality.
 - OLED screen display a variety of animations to accompany every step of the experience.
 - The other button serves a single purpose: to turn off the Raspberry Pi 5 safely through `sudo poweroff`.


# Hardware

See [JOURNAL.md](JOURNAL.md)

Check out the PCB files in `pcb/`.