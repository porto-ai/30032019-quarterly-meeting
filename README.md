# Quarterly Meeting #1 - 30-03-2019

## Dataset

In the practical component of the event, we will use the [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) dataset:
1. You'll need to create a Kaggle account, in case you don't have one already, and log in
2. Go to the *Data* tab, and click on *Download all*

## Project Dependencies

For completing all the proposed exercises, you'll need to clone this repository and install the required dependencies. We recommend using [Miniconda](https://docs.conda.io/en/latest/miniconda.html), if you're new to package manager systems, which allows you to create a separate development environment, isolated for your own convenience and safety :) Feel free to use any other tools, like pipenv or pure virtualenv.

Just make sure you are using Python3.6 or newer.

### Using Miniconda

1. Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Create a virtual environment (we will name it test_env, but you can call it whatever you want)
   + `conda create --name test_env python=3.6`
3. Activate the environment
   + Windows: `activate test_env`
   + Linux/macOS: `source activate test_env`
4. Go to your cloned project folder and install the requirements on you newly created environment
   + `conda install --file requirements.txt`
5. Run your python scripts as usual
   + `python your_own_script.py`
6. Deactivate the environment
   + Windows: `deactivate test_env`
   + Linux/macOS: `source deactivate test_env`
7. You can remove the environment for once and for all
   + `conda remove -n test_env -all`



