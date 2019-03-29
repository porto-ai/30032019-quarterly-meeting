# portoai-nlp
## Introduction
In this workshop you will have the opportunity to work directly with real-world problem by exploring 
different approaches to the Kaggle competition: [Jigsaw Toxic Comment Classification challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge).
The competition had the objective of developing a model capable of predicting a probability of six different types of toxicity for Wikipedia comments.
The types of toxicity are:
- toxic
- severe_toxic
- obscene
- threat
- insult
- identity_hate
Any of the comments can have more than one type of toxicity (or none at all) so we consider this a multi-label classification problem.
Before digging deeper, **make sure you understand what is the difference between multi-class and multi-label classification**. 
## Instructions
### 1 - Install Python dependencies

For completing all the proposed exercises, you'll need to clone this repository and install the required dependencies. We recommend using [Miniconda](https://docs.conda.io/en/latest/miniconda.html), if you're new to package manager systems, which allow you to create a separate development environment, isolated for your own convenience and safety :) Feel free to use any other tools, like pipenv or pure virtualenv.

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
5. Run your python scripts or jupyter-notebook as usual
   + `jupyter-notebook`
6. Deactivate the environment, once you're done for the day
   + Windows: `deactivate test_env`
   + Linux/macOS: `source deactivate test_env`
7. You can remove the environment for once and for all
   + `conda remove -n test_env -all`

### 2 - Download Kaggle dataset
Go to https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge , sign in (or create an account first) and then download the data for the Kaggle challenge. If you can not find it, try downloading it directly using [this link](https://www.kaggle.com/c/8076/download-all).
Extract the csv files inside the `portoai-nlp` directory.
You should also [download the fastText embeddings](https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M.vec.zip) that willbe later used in the notebooks.
### 3 - Run Jupyter notebooks
```
jupyter-notebook
```
Follow the notebooks' order and try to complete the exercises (we will provide these later).
