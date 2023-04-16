#!/usr/bin/env python
# coding: utf-8

# # Case Study: VaSyR 2018
# 
# In this section, we present an end-to-end example using a sample dataset. Information about the dataset can be found on [this page](https://microdata.unhcr.org/index.php/catalog/189).
# 
# ## Query generation
# 
# For the sample dataset, the six query formulations returned between one and 18 potentially relevant papers.
# 
# |  	| **Query String** 	| **Number of results** | 
# |---	|:---:	|:---:	|
# | 1 	| 'UNHCR Lebanon 2018 VASYR'	| 18	|
# | 2 	| 'UNHCR Lebanon 2018 Vulnerability Assessment of Syrian 0Refugees (VASYR)' | 5 |
# | 3 	| 'UNHCR Lebanon 2018 VASYR Vulnerability Assessment of Syrian efugees (VASYR)'	| 2	|
# | 4 	| 'UNHCR, WFP, UNICEF Lebanon 2018 VASYR'	| 6	|
# | 5 	| 'UNHCR, WFP, UNICEF Lebanon 2018 Vulnerability Assessment of Syrian Refugees (VASYR)' | 2 |
# | 6 	| 'UNHCR, WFP, UNICEF Lebanon 2018 VASYR Vulnerability Assessment of Syrian Refugees (VASYR)' 	|1	|

# In[1]:


import pandas as pd
df = pd.read_csv("data/semantic_scholar_query_results_with_web_count.csv")
print(df[df["id"] == 189])


# ## Semantic Search
# For query 1, below is the output returned from Semantic Scholar for 18 potentially relevant papers

# In[2]:


#df  = pd.read_csv("data/dataset189_query1.csv")
#glue("df_tbl", df)

w = observable_jupyter_widget.ObservableWidget(
    '@microdata-citation-explorer/query-generation',
    cells=['viewof table','typed_entry'], # optional
    inputs={'typed_entry': 189},  # optional
    outputs=['viewof table','typed_entry']  # optional
)
w


# ## Topic Modeling
# Out of the XX papers returned across the six query types, YYY had abstracts available in either the NLP4Dev or Semantic Scholar corpuses, and ZZZ had full body text available.
# 
# These were used as inputs to the NLP4Dev API, as described in [Section 3.5](methods/topic-modeling-and-sentiment-analysis.md).
# 
# XXX were defined as relevant.
# 
# ## Model Output
# Following manual review of the papers identified automatically, XXX were confirmed as relevant. Of these XXX, YYY had previously been identified through the manual procedure, and ZZZ were new.
# 
# This represents a XXX percent improvement over the baseline.
# 
# ## Evaluating Model Performance
# Based on our selected evaluation metric, Query X performed most effectively
# 
# ## Network analysis
# Of the papers that referenced this dataset, XYZ came from ABC geographies and ABC instutions.
