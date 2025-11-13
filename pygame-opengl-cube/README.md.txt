# Pygame OpenGL Cube

This project is a simple 3D cube visualization built using **Python**, **Pygame**, and **PyOpenGL**.  
I coded it to learn how OpenGL rendering works and how to connect it with Pygame for window management, input, and frame updates.

## Overview

The program draws a colored 3D cube that continuously rotates on both the X and Y axes.  
It uses lists of vertices, edges, and surfaces to define the cube’s shape, and OpenGL functions to render it with basic lighting and depth testing.

## Key Features

- Real-time cube rotation using transformation matrices  
- Distinct colored faces rendered with OpenGL quads  
- Dynamic frame updates with Pygame’s main event loop  
- Depth buffer support for correct 3D layering  
- Clean separation between drawing, updating, and rendering logic  

## How It Works

1. **Initialization:**  
   The script initializes Pygame, creates an OpenGL-enabled window, and sets up a perspective camera.  

2. **Rendering:**  
   Each frame, OpenGL clears the screen, applies rotations, and draws the cube using vertex and color data.  

3. **Animation Loop:**  
   The cube rotates continuously by updating rotation variables every frame. The main loop also listens for the quit event to close the program cleanly.

## Languages Used

- Python  
- Pygame  
- PyOpenGL  

## Run the Program

Install dependencies with pip:
