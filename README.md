![Cariprazine](https://bipolarnews.org/wp-content/uploads/2014/06/cariprazine-potw-01.jpg)

<h1 align="center">Cariprazine Dataset</h1>
<p align="center"><b>A Cariprazine User Review Dataset</b></p>

<p align="center"><img src="https://img.shields.io/github/issues/YuvalBogachev/cariprazine-dataset"> <img src="https://img.shields.io/github/forks/YuvalBogachev/cariprazine-dataset"> <img src="https://img.shields.io/github/stars/YuvalBogachev/cariprazine-dataset"> <img src="https://img.shields.io/github/license/YuvalBogachev/cariprazine-dataset?style=flat"></p>

<p align="center">
  <a href="#about">About</a> •
  <a href="#how-to-get">How To Get</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#dependencies">Dependencies</a> •
  <a href="#contributing">Contirbuting</a> •
  <a href="#license">License</a>
</p>

## About
- This dataset is a collection of user reviews for the anipsychotic Cariprazine from the website drugs.com. The main goal for collecting this data is to better understand the effects the drug has on its user, not from a clinician perspective, but rather from a consumer perspective ('rating'), backed by crowd consensus ('likes').
    - I decided to create a project to collect some data to be used in creative ways (text mining, sentiment analysis and more).
- In this repository is the code required to scrape drugs.com to obtain all user reviews (but can be used for any other drug).

## How To Get

```
# Clone the repository
git clone https://github.com/YuvalBogachev/cariprazine-dataset
```
- After succesfuly cloning the repository, you can do whatever you would like with the files.

## How To Use
- To run the scrapper, issue the command `python data.py`.
- You can change the URL of the DrugsCom iterator object (in data.py) to scrape any other drug.


## Dependencies
- BeautifulSoup4 (to scrape the web pages)
- requests (http requests)
- pandas (Dataframes)

## Contributing
- The dataset is freely available on Kaggle, so there is no need to actually run the script to obtain the data, the repository is strictly for educational purposes.

## License
- This program is licensed under the GPL V3.
