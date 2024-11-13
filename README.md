Virtual Whiteboard

A Virtual Whiteboard created using Python and Pygame that allows users to draw, erase, and interact with a digital canvas. This project serves as a simple tool for drawing and note-taking, ideal for brainstorming sessions, interactive learning, and collaborative activities.

Features:

Freehand Drawing: Draw freely on the whiteboard using a digital pen.
Erase Function: Erase parts of the drawing as needed.
Clear Canvas: Reset the whiteboard to start fresh.
Color Selection: Choose from various colors to make drawings more expressive.
Brush Size Adjustment: Change the brush size for finer or broader strokes.
Undo/Redo (Optional): Add an undo/redo function for improved usability.

Installation:

To set up the Virtual Whiteboard on your local machine, follow these steps:

Prerequisites:
Matplotlib
open-cv
mediapipe
numpy

Python 3. py
Pygame library

Installation Steps:
Clone the repository:

bash
Copy code
git clone https://github.com/DeepakPanneerselvam1455/virtual-whiteboard.git
cd virtual-whiteboard

Install the required library:
bash
Copy code
pip install pygame
Run the application:

bash
Copy code
python whiteboard.py
Usage
Use the left mouse button to draw on the whiteboard.
Use the right mouse button to erase.
Press C to clear the canvas.
Change colors and brush sizes through the toolbar (if implemented).
Code Structure
whiteboard.py: Main script for initializing and running the whiteboard application.
utils.py: Utility functions for handling drawing, erasing, and UI elements.
assets/: Folder for storing images, icons, or additional assets.
Future Enhancements
Shape Drawing: Add options to draw basic shapes like circles, rectangles, and lines.
Save/Load Canvas: Save the current state of the whiteboard as an image file and load it later.
Collaborative Mode: Enable multiple users to draw on the same whiteboard remotely.
Text Tool: Add a tool for typing text onto the whiteboard.
Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
