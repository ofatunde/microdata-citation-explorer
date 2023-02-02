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

# Semantic search

We made use of the [Semantic Scholar API](https://www.semanticscholar.org/product/api). For each of the query strings generated in the last section, we pass them to the ["Paper Lookup" API endpoint](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data), which we access through the [SemanticScholar Python library](https://github.com/danielnsilva/semanticscholar) using the following call:

```{code-cell}
sch = SemanticScholar()
query_type1 = []
for i in dfq["query_type1"]:
    results = sch.search_paper(i)
    query_type1.append(results)
```
The output is an object which includes (among others) the following information:
* Dataset ID
* Paper IDs (includes SS's internal ID, as well as external IDs such as DOI, arXiv, Pubmed, etc. where available)
* Title
* Authors
* Publication venue
* Publication year
* Field of Study
* Count of inbound and outbound citations
* URL
* Abstract
* PDF availability (indicates whether the full PDF is included in the corpus, and whether the abstract, body, and bibliographic entries are available in parsedt format)

We extract abstracts from this output, giving us an abstract for each dataset-query-paper combination where an abstract is available. The abstract, together with the indicator of PDF availability, serves as an input into our topic modeling procedure (see the next section.)

```{code-cell}
def semantic_search(query:str)->pd.DataFrame:
    """ This function takes in a query (from the query_finder function) and returns a dataframe of abtracts and corpus IDS"""
    sch = SemanticScholar()
    results = sch.search_paper(query)
    
    #metadata
    ### Add title
    abstracts = [item.abstract for item in results]
    identifiers =  [item.externalIds for item in results]
    API_corpus_ID = [i.get("CorpusId") for i in identifiers] # we can return whatever we want here.     
    return pd.DataFrame(list(zip(abstracts, API_corpus_ID)), columns = ['abstract', 'corpus_id'])
```

Where available, we also parse PDF content. When we parse a PDF, the output is an object which includes (among others) the following information:
* Paper ID
* PDF hash
* Abstract (if available)
* Body text (if available)
* Bibliographic entries

% From the Semantic Scholar API, we get the datasets labeled **“query_typex_abs,”** where the x  in the name = 1,2,3,4,5,6 refers to the query type. These datasets contain the following variables: **paper title, abstract, corpus ID (also called paper ID), author IDs, Digital Object identifiers (DOIs), publication year,** the **journal**  where the paper was published, and the **dataset ID**. These metadata datasets will be merged with the metadata datasets we get from the NLP4DEV API website.

## Citations

The following papers informed our approach: {cite}`Fast2016`,{cite}`Chen2006`.


```{bibliography}
```