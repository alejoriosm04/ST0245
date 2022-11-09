<h1 align = "center">Street Harassment in Medellin</h1>

Research of an algorithm able to provent the street harassment in Medellin combining distance and harassment risk.

Project for the second-semester course "Data Structures and Algorithms I" (ST0245) taught at EAFIT University (Medellín, Colombia) by prof [Mauricio Toro](https://github.com/mauriciotoro).

## Contents
- [Project Structure](#project-structure)
- [Motivation](#motivation)
- [Documentation](#documentation)
    - [Caveats](#caveats)
- [Install](#install)
- [Demo](#demo)
- [Contribute](#contribute)
- [Authors](#authors)
- [License](#license)

## Project Structure

    ├── CITATION.cff
    ├── README.md               <- Details about the project.
    ├── .gitignore         
    │ 
    ├── code                    <- Folder containing all the development stages of the project in code.
    │   ├── delivery1     
    │   ├── delivery2
    │   └── final-delivery      <- Folder containing the final results of this project.
    │       └── src/data        <- Datasets used and collected for this project.
    │   
    └── docs                    <- Folder to store all documentation of the project.
        │
        ├── reports
        │   ├── delivery1     
        │   ├── delivery2
        │   └── final-delivery  <- Folder containing the final Report of this project.
        │   
        └── presentations
            ├── delivery1     
            ├── delivery2
            └── final-delivery  <- Folder containing the final Presentation of this project.
--------

## Motivation

Sexual harassment is a problem women experience in their daily life, this can include verbal and non-verbal abuse, and can take place everywhere. Due to this, in order to make women feel more safe, this project and research is about using an algorithm that is able to calculate different paths depending on the distance and the sexual harassment of Medellin streets.

In the Reports of the project, you will find the reasons for the development of this project and the proposed solutions. Also, how all the authors of this, made possible the final results.

## Documentation
**Note:** Please read the [Project Structure](#project-structure) at the start and the documentation in [docs](https://github.com/alejoriosm04/ST0245/tree/master/docs) folder.

This project had a special development and documentation process, according to the course instructions. In the [docs](https://github.com/alejoriosm04/ST0245/tree/master/docs) folder, you will find two folders with documentation. 

The first one, [reports](https://github.com/alejoriosm04/ST0245/tree/master/docs/reports), has all the Technical Reports about the project, there you will know how the problem was studied, what were factors taken into account, and how we created the solution. And the second one, [presentations](https://github.com/alejoriosm04/ST0245/tree/master/docs/presentations), has the Presentations used in class to explain the project.

This research is in a [OSF repository](https://osf.io/wxe4v).

For the development of the algorithm, we used Dijkstra Algorithm[^definition_dijkstra] to calculate the Shortest and Safest Path in Medellin, reading a starting point and a target point. To plot the map and see the generated paths, was used the Google Maps API.

### Caveats

- The program is not user-friendly. For default, when the program is executed, calculate three paths between the National University of Colombia and EAFIT University. Thus, if you want to calculate another path, you have to manually search for the coordinates and added them to the function.

- To plot the map, you need an API Key from Google Cloud to read the information from the official data of Google Maps.

- The installation process could be difficult, in this project, many libraries were used, thus, you need to have the correct environment to run the program on your console.

- Be aware that the program breaks in certain cases, where the coordinates are wrong. However, in future adaptations of the project this can be improved. See [Contribute](#contribute).

## Install

**Note:** This project was not develop with a Python Virtual Environment.

- In the [final-delivery](https://github.com/alejoriosm04/ST0245/tree/master/code/final-delivery/src) code folder, you will find a `requirements.txt` file with the requirements to run this program with the respective Python Libraries.

- Run:
    
        git clone git@github.com:alejoriosm04/ST0245.git

- Do not modify the file structure, it could lead to problems with execution.

- To see the map plot, the program will open automatically your default browser, if this does not happen, open the `map.html` file on your browser and you will see the paths in the **Google Maps** map.

## Demo
- A screenshot of the generated paths plotted on Google Maps by the algorithm
<div align="center">
  <img src='https://i.imgur.com/J8WpETs.png' height='400px'/>
</div>

## Contribute

Since this is the authors' coursework, we will not review pull requests. However, this project has a great future and each of the authors plans to improve this project in different ways in the development of the program at EAFIT University.

We want anyone who sees this project and the research done to continue developing solutions and use this progress as a basis for developing a better product. See [License](#license).

## Authors
- Thanks to the collaboration of all authors, who made the development of this project possible🤝.

<a href="https://github.com/alejoriosm04/ST0245/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=alejoriosm04/ST0245" />
</a>

## License
This software project is licensed under the CC-By Attribution 4.0 International[^license].

Copyright (c) 2022, Alejandro Ríos-Muñoz, Marcela Londoño-León, Juan Alejandro Osorno-Bustamante.

[^definition_dijkstra]: [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm): "Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph".

[^license]: [Creative Commons](https://creativecommons.org/licenses/by/4.0/deed.es).