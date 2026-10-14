# OpenGL Cube (Pygame + PyOpenGL)

A rotating, color-faced 3D cube rendered with legacy (fixed-function) OpenGL, using Pygame for the window and event loop. I wrote it to learn the basics of the OpenGL pipeline: perspective projection, the model-view matrix stack, depth testing, and per-frame redraws.

## What it does

- Defines the cube as vertex, edge and face index tables, then draws faces with `GL_QUADS` and outlines with `GL_LINES`
- Sets up a perspective camera with `gluPerspective` and moves it back with `glTranslatef`
- Rotates the cube around the X and Y axes each frame inside `glPushMatrix`/`glPopMatrix`, so the transforms don't accumulate
- Enables the depth buffer so nearer faces correctly hide farther ones
- Caps the loop at 60 FPS and reports any OpenGL errors after each frame

## Run it

Requires Python 3.10+ and a machine with OpenGL support.

```bash
pip install -r requirements.txt
python main.py
```

Close the window to exit.

## What I'd do next

- Move from immediate mode (`glBegin`/`glEnd`) to vertex buffer objects and shaders (modern OpenGL)
- Add lighting with per-face normals
- Control rotation with the mouse or keyboard

## License

MIT. See [LICENSE](LICENSE).
