#!/usr/bin/env python
# coding: utf-8

# # Dataset selection

# In[1]:


#from glueviz import glue
from myst_nb import glue
import ipywidgets as widgets
from IPython.display import display

latest_data_with_categories = pd.read.csv("data/latest_data_with_categories.csv")

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


# # Model output
# Each model returns a list of papers with the following information:
# 
# * Dataset Title
# * Paper Title
# * Binary relevance
# * Continunous relevance score
# * Number of JDC tags mentioned
# * Percentage of paper dedicated to forced displacement
