# Training_A_Smart_Cab
## Reinforcement Learning
### Project: Train a Smartcab How to Drive

A Smartcab was trained to follow US Traffic Laws. Its efficiency was measured based on the number of times in reached the goal within time or number of accidents it got involved in. The project uses Q Learning algorithm to find optimal utility of each state to find the optimal policy.

The optimal policy is the action which car takes to navigate complex situations which it encounters while driving a car. 

### Install

This project requires **Python 2.7** with the [pygame](https://www.pygame.org/wiki/GettingStarted
) library installed

### Code

Template code is provided in the `smartcab/agent.py` python file. Additional supporting python code can be found in `smartcab/enviroment.py`, `smartcab/planner.py`, and `smartcab/simulator.py`. Supporting images for the graphical user interface can be found in the `images` folder. While some code has already been implemented to get you started, you will need to implement additional functionality for the `LearningAgent` class in `agent.py` when requested to successfully complete the project. 

### Run

In a terminal or command window, navigate to the top-level project directory `smartcab/` (that contains this README) and run one of the following commands:

```python smartcab/agent.py```  
```python -m smartcab.agent```

This will run the `agent.py` file and execute your agent code.


## Results
The Q Learning Model has successfully learned the laws of the US Traffic after enough trial runs. The safety rating is A+ and Reliability Rating is A+

A+ means that the car reaches the destination 100% of time within time limit and without any traffic violation and always chooses correct action.