# Petri Net State Machine in WebGME

##Work Cited

The controller, widget, and python plugin for this project are based off work done by https://github.com/kecso in the project https://github.com/kecso/StateMachineJoint


##Domain

A State Machine meta implementation in WebGME.
The petri_viz Visualizer walks through an example Petri Net implementation of the State Machine

##Use Case/How to Model/Features

To use, create an instance of the default State Machine to fid your model needs (x number of States, x number of Transitions, x number of Decisions).
The petri_viz can be used to accurately step through your model.
Start off by right clicking the ROOT node in Object Browser. Select Create Child -> StateMachine. Next, add States, Transitions, init, end as needed. Under Visualizer Selector, select petri_viz and use 'Play' button to show transition accuracy. The '?' button will show lower level details of your graph if weights are added.


## Installation

First, install the final following:
- [NodeJS](https://nodejs.org/en/) (LTS recommended)
- [MongoDB](https://www.mongodb.com/)

Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Change directory to top level of project. Run, 'npm install' and verify no errors are thrown. 

Next, run, 'npm start', verify no errors are thrown, and brows 'http://127.0.0.1:8888'
