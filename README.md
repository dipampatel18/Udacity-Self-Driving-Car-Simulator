# Udacity-Self-Driving-Car
Training Udacity's Self-driving Car using the Unity Simulator

<p align="center">
  <img width="720" height="400" src="/files/Final_Run.gif">
</p>

### Getting Started

Clone the repository to your local directory

```git clone https://www.github.com/dipampatel18/Udacity-Self-Driving-Car.git```

### Install the Dependencies

Run the following command to install the dependencies

```sudo pip3 install -r requirements.txt```

### Download the Simulator
[Download](https://github.com/udacity/self-driving-car-sim)

## Training

To train your own model, first, data collection is required. If you wish to collect your own data, delete all the files from the folder named data inside the src folder. Now, run the simulator from the beta simulator using the following command-

Make it executable

```chmod a+x beta_simulator.x86_64```

Running the application

```./beta_simulator.x86_64```

- The simulator will start running
- Select the desired scene and start the training mode
- Press 'r' to start the recording and navigate to the ```Udacity-Self-Driving-Car/src/data``` folder
- Press 'r' again and start driving the car around
- The simulator is continuously recording center, left and right images, along with the steering angle, speed, throttle and brake
- All the collected data will be stored in the data folder with the images in IMG folder and the data in driving_log.csv format

Begin training using the following command

```python3 train.py```

## Testing

The trained model has its weights saved in the model.h5 file which can be directly loaded during the testing phase

Now, just like before, launch the simulation. Only this time, select the Autonomous Mode and then run the following command to start the testing of our trained model.

```python3 test.py model.h5```

## Saving Test Run

In order to save the FPV frames of the agent and later convert it to a video, run the following command with the desired name of the folder-

```python3 test.py test_run```

To convert those frames into a video, run the following command-

```python3 video.py test_run``` 

This will save a video in the current directory with the name- test_run.mp4 at 60 fps. To change the fps, feed the above command with an argment-

```python3 video.py test_run --fps 30``` 


### References


- [Udacity Self-Driving Car](https://github.com/udacity/CarND-Behavioral-Cloning-P3)

- [Udacity Self-Driving Car Simulator](https://github.com/udacity/self-driving-car-sim)

- [Tutorial - Siraj Raval](https://github.com/llSourcell/How_to_simulate_a_self_driving_car)

- [Tutorial - Naoki Shibuya](https://github.com/naokishibuya/car-behavioral-cloning)
