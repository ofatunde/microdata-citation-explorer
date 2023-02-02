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
We begin by generating a set of search queries based on the metadata for each dataset.

The full query creation notebook can be found at this link: 
[1]: https://github.com/ofatunde/mdl-explorer-app/blob/main/notebooks/Semantic_Scholar_NLP4DEV.ipynb "Query notebook"

We start with simple methods of combining the metadata. The key metadata components that we use as an input into queries are:
* Core survey name
* Survey abbreviation (e.g., VaSyR)
* Lead organization (e.g., UNHCR) - short or long versions may be used
* Category (e.g., Socioeconomic Asessment of Refugees)
* Country
* Year 

For our initial exploration, we define six simple query types which represent different combinations of the information above :

* Query type 1: lead_org_short + year + name + shortcode
* Query type 2: lead_org_short + year + name + full_name
* Query type 3: lead_org_short + year + name + shortcode_fullname
* Query type 4: lead_org_long + year + name + shortcode
* Query type 6: lead_org_long + year + name + shortcode_fullname

Defining query structure is an important step, as the search output can be sensitive to the contents of the query used for the search. For example, the six queries above return different number of results if entered into Semantic Scholar. 

The table below shows the number of results returned by Semantic Scholar for each dataset.
```{code-cell} ipython3
:tags: ["output_scroll","hide-input"]
import pandas as pd
df = pd.read_csv("./jupyter_execute/data/semantic_scholar_query_results_with_web_count.csv")
df.head()
```

## Next steps
After generating these queries, we run the queries we created from the raw file (“overview_all_datasets_2022_categorized.xlsx") through the semantic scholar API. See [the next section](methods/semantic-search.md) for more details.


## Citations

The following papers informed our approach: {cite}`Bakke2016`.


```{bibliography}
```