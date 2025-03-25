# Real Estate Machine Learning Analysis

## Description
The real estate ML analysis project attempts to create a recommendation system of the top places people should live after it has been fed a couple of parameters by a user. The consumer appeal comes from the ability to accurately suggest the best places to live using a neural network. The machine learning innovation of this project is the model's ability to predict other parameters not inputted by a user based on the parameters that they have input.

## Project Setup

- Setup [Docker](docs/docker-setup.md)

### Development Workflow - Best Practices
Create a seperate branch to develop new features or to investigate an issue. Please follow the branch naming scheme so that the linear history for the project is kept organized. Your branch names should be in the following format:

```
[GitHub Username]/[Issue ID #]-[Issue Title]
```

Write good quality commit messages shorter than 100 characters long that describe what you did in the present tense. Do not use past tense in commit messages, i.e. "Completed...," "Fixed...," "Updated." Instead, say "Complete...," "Fix...," "Update." Please read this [article about writing good commit messages.]((https://cbea.ms/git-commit/))

Before any push up to GitHub, please review your diffs and ensure that you aren't uninentionally pushing anything that isn't supposed to be on the repository.

On making amendments to your PR reviewer's comments, you should practice linking to the commit that specifically addresses the reviewer's comments before requesting a re-review. This helps keep everything running fast and smooth with no hiccups.

Once your branch has been reviewed and merged, you should delete the branch you were working on from the github remote to keep our branch history clean. Do not leave merged branches up on the remote please.

Happy coding!

## 3 Datasets

#### [Household Income Analysis](https://www.kaggle.com/datasets/stealthtechnologies/regression-dataset-for-household-income-analysis)

#### [Housing Features Regressional Analysis](https://www.kaggle.com/datasets/denkuznetz/housing-prices-regression)

#### [Housing Prices Regressional Analysis](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)

### Get Programming

#### Installing Dependencies
Run the following commands:

1. `cd frontend`
2. `npm install` to install React dependencies
3. `cd ../backend`
4. `python3 -m pip install -r requirements.txt` to install FastAPI & SQLModel dependencies (This must be run every time the container is rebuilt)
5. `python3 -m backend.scripts.reset_database` to create the database and load in fake data. This can be run as many times as possible to reset the databse.

### Running the Development Server

1. Run `honcho start`
2. Open `http://localhost:2000` to view the application

## Development Concerns

### Backend

To help with backend implementation, you can reference the `count` demo feature. 

#### FastAPI

When creating FastAPI routes, make sure to define the routes in a feature file named corresponding to the feature inside of the `api` directory.
This file should look similar to the example one in `api/count.py`. You will need to import the file in `main.py` and
add it to the `feature_apis` list as well as the tags in the `openapi_tags` list in the `FastAPI()` constructor.

#### SQLModel

Define all SQLModels in the `models` folder in a file named according to the feature. Make sure to add this file to the `__all__` list inside
of the `__init__.py` file in the `models` folder. This will allow it to be imported by default inside of the `create_database` script.

In the future we will support adding fake data inside of the `create_database` script.
