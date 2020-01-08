# JEOPARDY! by Team Saturated Sidewalks

## Roster
* Peihua Huang : Project Manager
* Alice Ni : Frontend/APIs
* Jacob Olin : Databases
* Hilary Zen : Python

## Description
Our project allows users to create their own Jeopardy boards or use randomly generated ones (with data from APIs) and play. Users' game history will be stored, along with the boards that they create. They can also search for boards that other users created. Each game can have up to 5 teams and scores will be tallied at the bottom of the jeopardy board. Go wild and have fun!

## APIs Used:
  (no keys required!!!)
* [Open Trivia](https://docs.google.com/document/d/1yp2nicOExDYlrEfdvqspD17Kz5c-xMSWHudfmNjJgQ4/edit)
* [PokeAPI](https://docs.google.com/document/d/1hMbL36d5qqFLfufHOqUMWwraWFudfJdekqp6urex0KU/edit)
* [REST Countries](https://docs.google.com/document/d/1C-umxnBAIUzQI9kLDaXG4-YbFsiOwwRTJ5c-DXAHTRM/edit)
* [Rick and Morty](https://docs.google.com/document/d/1oK0klhp__LHP9kxb3D70cbbI46i1mMnmDMI4y1XS3B4/edit)

### How to run this project
1. Create and run a virtual environment with the following commands:
   ```
   python3 -m venv <name of virtual environment>    # creates a virtual environment named <name of virtual environment>
   .<name of virtual environment>/bin/activate      # activates the virtual environment
   ```
2. Clone and change into our repository:
   ```
   git clone https://github.com/phuang00/P02_softdev.git
   cd P02_softdev/
   ```
3. Install all the needed packages using the following command in a terminal:
   ```
   pip3 install -r doc/requirements.txt
   ```
4. Once all the packages are install, run the project:
   ```
   python3 app.py
   ```
   Once the Flask is running, open http://127.0.0.1:5000/ in the browser
5. When you are finished, deactivate it by entering `deactivate` into the command line.

---
