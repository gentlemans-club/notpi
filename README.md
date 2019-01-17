# notpi

A simple Sense HAT emulator using PyGame.

NotPi bases itself on the API of [sense-hat](https://github.com/RPi-Distro/python-sense-hat).
The goal is to enable users to develop software for the Sense HAT on any platform supported by PyGame,
and have that same code work as expected on the Sense HAT itself.

Currently, the plan is primarily to provide functions to draw to the 8x8 matrix, and also to handle button input.

## Installation

After cloning, run:

```sh
pip install .
```

## Usage

Only a small subset of the sense-hat library's functions has been implemented.
Here is the current status of functionality: https://github.com/gentlemans-club/notpi/projects/1

The following example shows a way in which some code can be run on `sense-hat` if it is available, while also
being able to run locally on a computer using NotPi.

```python
try:
    # use SenseHat if available
    from sense-hat import SenseHat
    sense = SenseHat()
except ImportError:
    # if not, fall back to NotPi
    from notpi import NotPi
    sense = NotPi()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)
```

## Contributing

### For gentlemans-club members
Here is an example with implementing set_pixel

1. Pick your task, and assign yourself to the issue so that people know that you will be working on it.
2. Create a branch which corresponds to the task you will work on
    * `git checkout -b set_pixel`
        * `set_pixel` here refers to the branch name
3. Implement set_pixel according to the issue, and test that it works as expected
4. Commit your changes to your local repository
    * `git add .`
    * `git commit -m "Implements #6"`
        * Note: #6 corresponds to the issue number
5. Push your changes to origin
    * `git push origin set_pixel`
        * `set_pixel` here refers to the branch name
6. Create a pull request to master, if the branch can be merged to master automatically you are free to do so.
7. Delete the branch, close the corresponding issue, and move the task in the project to completed.

### For anyone else

1. Fork the project on GitHub, and clone your own version
2. Implement a desired feature.
3. Commit your changes and push it to origin
    * `git add .`
    * `git commit -m "Implements my_feature"`
    * `git push`
4. Create a pull request to this repository!
