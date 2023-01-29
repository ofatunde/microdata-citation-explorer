---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Query Generation
We begin by generating a set of search queries based on the 
Here is the query creation notebook: https://github.com/ofatunde/mdl-explorer-app/blob/main/notebooks/Semantic_Scholar_NLP4DEV.ipynb 

### Import modules
```{code-cell}
import numpy as np
import pandas as pd
from semanticscholar import SemanticScholar
import re
from collections import Counter
import preprocessor as p
import pickle
import requests
import time
```

### import data dump and query building data
```{code-cell}
sample_metadata = pd.read_json(r"Downloads\sample_metadata.json", lines = True)
sample_pdf_parses = pd.read_json(r"Downloads\pdf_parses_sample.json", lines = True)
data = pd.read_excel(r"Downloads\overview_all_datasets_2022_categorized.xlsx",sheet_name = "Categorized")
df = pd.read_csv(r"Downloads\mdl_baseline_summary.csv")

```


### Build queries.
```{code-cell}
data["fullname_shortcode"] = data["Category"]+ " "+ data["abbreviation"]
```
```{code-cell}
dfq = pd.DataFrame()
```
```{code-cell}
dfq["fau_short"] = pd.DataFrame(df.full_query).applymap(lambda x: x.split()[0]) # Authoring entity short
dfq["fau_long"] = df["authoring_entity"] #Authoring entity long
dfq["name"] =df["nation"] # Extract nation
dfq["year"]= df["full_query"].str.extract('(\d+)', expand=False) # extract year
```

### fau = First Authoring Organization
```{code-cell}
dfq["short_code"] = data["abbreviation"]
dfq["full_name"] =  data["Category"]
dfq["shortcode_fullname"] =  data["abbreviation"]+ " "+  data["Category"]

```

### Queries
Query type 1: fau_short+year+name+shortcode
Query type 2: fau_short+year+name+full_name
Query type 3: fau_short+year+name+shortcode_fullname
Query type 4: fau_long+year+name+shortcode
Query type 6: fau_long+year+name+shortcode_fullname

```{code-cell}
dfq["query_type1"] = dfq["fau_short"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["short_code"] #type 1
dfq["query_type2"] = dfq["fau_short"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["full_name"] #2
dfq["query_type3"] = dfq["fau_short"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["shortcode_fullname"] #3
dfq["query_type4"] = dfq["fau_long"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["short_code"] # 4
dfq["query_type5"] = dfq["fau_long"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["full_name"] # 5
dfq["query_type6"] = dfq["fau_long"]+ " "+ dfq["name"]+ " "+dfq["year"]+" "+dfq["shortcode_fullname"] #6
dfq['id']  = data['id']
#dfq.to_excel(r"Downloads\semantic_scholar_queries.xlsx", index = False)-> Save dataset
```

### Use query type 1 to query ss API

```{code-cell}
query_finder(dfq, 189,1)
```
```{code-cell}
#sch = SemanticScholar()
#results = sch.search_paper(query_finder(dfq, 189,1))
title = []
abstract = []
results
for item in results:
     title.append(item.title)
for item in results:
    abstract.append(item.abstract)    
```
```{code-cell}
data = pd.DataFrame(list(zip(title,abstract)), columns = ['title', 'abstract'])
```
```{code-cell}
data["dataset_number"] =189
```
```{code-cell}
data["query_number"] =1
```
```{code-cell}
data.to_excel(r"downloads\streamlitdemo.xlsx", index =False)
```
```{code-cell}
# This function takes in the name of our dataframe, the id of the data set and the query number and returns the query.
def query_finder(df_name: pd.DataFrame, dataset_id: int = 189, query_number:int =1 )->str:
    """ Function takes in the query dataframe, the dataset ID and the query type number and retuns the query itself"""
    df_indexid = df_name.set_index('id')
    query = df_indexid.loc[189][f"query_type{query_number}"]
    return query 
```
### Query type1 for all data sets
## Pausing

## An example cell

With MyST Markdown, you can define code cells with a directive like so:

```{code-cell}
print(2 + 2)
```

When your book is built, the contents of any `{code-cell}` blocks will be
executed with your default Jupyter kernel, and their outputs will be displayed
in-line with the rest of your content.

```{seealso}
Jupyter Book uses [Jupytext](https://jupytext.readthedocs.io/en/latest/) to convert text-based files to notebooks, and can support [many other text-based notebook files](https://jupyterbook.org/file-types/jupytext.html).
```

## Create a notebook with MyST Markdown

MyST Markdown notebooks are defined by two things:

1. YAML metadata that is needed to understand if / how it should convert text files to notebooks (including information about the kernel needed).
   See the YAML at the top of this page for example.
2. The presence of `{code-cell}` directives, which will be executed with your book.

That's all that is needed to get started!

## Next steps
After generating these queries, we run the queries we created from the raw file (“overview_all_datasets_2022_categorized.xlsx") through the semantic scholar API. See [the next section](methods/semantic-search.md) for more detailes.


## Citations

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
this: {cite}`holdgraf_evidence_2014`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.
For example, if the references for your book are stored in `references.bib`,
then the bibliography is inserted with:

```{bibliography}
```
