#!/usr/bin/env python
# coding: utf-8

# # Query Generation
# We begin by generating a set of search queries based on the metadata for each dataset.
# 
# The full query creation notebook can be found at this link: 
# [1]: https://github.com/ofatunde/mdl-explorer-app/blob/main/notebooks/Semantic_Scholar_NLP4DEV.ipynb "Query notebook"
# 
# We start with simple methods of combining the metadata. The key metadata components that we use as an input into queries are:
# * Core survey name
# * Survey abbreviation (e.g., VaSyR)
# * Lead organization (e.g., UNHCR) - short or long versions may be used
# * Category (e.g., Socioeconomic Asessment of Refugees)
# * Country
# * Year 
# 
# For our initial exploration, we define six simple query types which represent different combinations of the information above :
# 
# * Query type 1: lead_org_short + year + name + shortcode
# * Query type 2: lead_org_short + year + name + full_name
# * Query type 3: lead_org_short + year + name + shortcode_fullname
# * Query type 4: lead_org_long + year + name + shortcode
# * Query type 6: lead_org_long + year + name + shortcode_fullname
# 
# Defining query structure is an important step, as the search output can be sensitive to the contents of the query used for the search. For example, the six queries above return different number of results if entered into Semantic Scholar. 
# 
# The table below shows the number of results returned by Semantic Scholar for each dataset.

# In[1]:


import pandas as pd
df = pd.read_csv(r"data\semantic_scholar_query_results_with_web_count.csv")
print(df)


# {::comment}
# (### Import modules

# In[ ]:


import numpy as np
import pandas as pd
from semanticscholar import SemanticScholar
import re
from collections import Counter
import preprocessor as p
import pickle
import requests
import time


# ### import data dump and query building data

# In[ ]:


sample_metadata = pd.read_json(r"Downloads\sample_metadata.json", lines = True)
sample_pdf_parses = pd.read_json(r"Downloads\pdf_parses_sample.json", lines = True)
data = pd.read_excel(r"Downloads\overview_all_datasets_2022_categorized.xlsx",sheet_name = "Categorized")
df = pd.read_csv(r"Downloads\mdl_baseline_summary.csv")


# ### Build queries.

# In[ ]:


data["fullname_shortcode"] = data["Category"]+ " "+ data["abbreviation"]


# In[ ]:


dfq = pd.DataFrame()


# In[ ]:


dfq["fau_short"] = pd.DataFrame(df.full_query).applymap(lambda x: x.split()[0]) # Authoring entity short
dfq["fau_long"] = df["authoring_entity"] #Authoring entity long
dfq["name"] =df["nation"] # Extract nation
dfq["year"]= df["full_query"].str.extract('(\d+)', expand=False) # extract year


# ### fau = First Authoring Organization

# In[ ]:


dfq["short_code"] = data["abbreviation"]
dfq["full_name"] =  data["Category"]
dfq["shortcode_fullname"] =  data["abbreviation"]+ " "+  data["Category"]


# ### Queries
# Query type 1: fau_short+year+name+shortcode
# Query type 2: fau_short+year+name+full_name
# Query type 3: fau_short+year+name+shortcode_fullname
# Query type 4: fau_long+year+name+shortcode
# Query type 6: fau_long+year+name+shortcode_fullname

# In[ ]:


dfq["query_type1"] = dfq["fau_short"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["short_code"] #type 1
dfq["query_type2"] = dfq["fau_short"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["full_name"] #2
dfq["query_type3"] = dfq["fau_short"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["shortcode_fullname"] #3
dfq["query_type4"] = dfq["fau_long"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["short_code"] # 4
dfq["query_type5"] = dfq["fau_long"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["full_name"] # 5
dfq["query_type6"] = dfq["fau_long"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["shortcode_fullname"] #6
dfq['id']  = data['id']
#dfq.to_excel(r"Downloads\semantic_scholar_queries.xlsx", index = False)-> Save dataset


# ### Use query type 1 to query ss API

# In[ ]:


query_finder(dfq, 189,1)


# In[ ]:


#sch = SemanticScholar()
#results = sch.search_paper(query_finder(dfq, 189,1))
title = []
abstract = []
results
for item in results:
     title.append(item.title)
for item in results:
    abstract.append(item.abstract)    


# In[ ]:


data = pd.DataFrame(list(zip(title,abstract)), columns = ['title', 'abstract'])


# In[ ]:


data["dataset_number"] =189


# In[ ]:


data["query_number"] =1


# In[ ]:


data.to_excel(r"downloads\streamlitdemo.xlsx", index =False)


# In[ ]:


# This function takes in the name of our dataframe, the id of the data set and the query number and returns the query.
def query_finder(df_name: pd.DataFrame, dataset_id: int = 189, query_number:int =1 )->str:
    """ Function takes in the query dataframe, the dataset ID and the query type number and retuns the query itself"""
    df_indexid = df_name.set_index('id')
    query = df_indexid.loc[189][f"query_type{query_number}"]
    return query 


# ### Query type1 for all data sets
# ## Pausing
# {:/comment}
# ## Next steps
# After generating these queries, we run the queries we created from the raw file (“overview_all_datasets_2022_categorized.xlsx") through the semantic scholar API. See [the next section](methods/semantic-search.md) for more details.
# 
# 
# ## Citations
# 
# The following papers informed our approach: {cite}`Bakke2016`.
# 
# 
# ```{bibliography}
# ```
