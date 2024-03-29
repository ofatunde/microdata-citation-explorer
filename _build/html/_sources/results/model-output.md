---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Dataset selection

First, filter by the following inputs in order to generate a set of datasets to choose from:
```{code-cell} ipython3
:tags: ["hide-input"]
#from glueviz import glue
from myst_nb import glue
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import requests
url = "https://microdata.unhcr.org/index.php/api/catalog/search?ps=2000&sort_by=created&sort_order=desc"
headers = {'Content-type': 'application/html',
           'Accept': 'application/json'
           }
r = requests.get(url, verify=False, headers = headers,stream=True)
json = r.json()
latest_data = pd.DataFrame(json['result']['rows'])
dataset_category_mapping = pd.read_csv("dataset_category_mapping.csv",encoding = "latin")
latest_data_with_categories = pd.merge(latest_data,dataset_category_mapping,how = "left",on = 'title')

#latest_data_with_categories = pd.read_csv("data/latest_data_with_categories.csv")

repository_list = latest_data_with_categories['repo_title'].unique().tolist()
category_list = latest_data_with_categories['Category'].unique().tolist()
country_list = latest_data_with_categories['nation'].unique().tolist()
year_list = latest_data_with_categories['year_end'].unique().tolist()
dataset_list = latest_data_with_categories['title'].unique().tolist()
query_type = ['1', '2', '3','4','5','6']

repo_dropdown = widgets.Dropdown(
    options=repository_list,
    value='Europe',
    description='Repository:',
    disabled=False,
)

category_dropdown = widgets.Dropdown(
    options=category_list,
    value='KAP WASH Survey',
    description='Survey Category:',
    disabled=False,
)

country_dropdown = widgets.Dropdown(
    options=country_list,
    value='Lebanon',
    description='Survey Country:',
    disabled=False,
)

year_dropdown = widgets.Dropdown(
    options=year_list,
    value=2018,
    description='Survey Year:',
    disabled=False,
)

##df  = pd.read_csv("data/dataset189_query1.csv")
#glue("df_tbl", df)

display(repo_dropdown)
display(country_dropdown)
display(category_dropdown)
display(year_dropdown)
```

# Model output
Each model returns a list of papers with the following information:

* Dataset Title
* Paper Title
* Binary relevance
* Continunous relevance score
* Number of JDC tags mentioned
* Percentage of paper dedicated to forced displacement


