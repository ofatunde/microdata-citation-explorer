# Semantic search

We made use of the [Semantic Scholar API](https://www.semanticscholar.org/product/api). For each of the query strings generated in the last section, we pass them to the ["Paper Lookup" API endpoint](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data), which we access through the [SemanticScholar Python library](https://github.com/danielnsilva/semanticscholar) using the following call:

```{code-cell}
sch = SemanticScholar()
query_type1 = []
for i in dfq["query_type1"]:
    results = sch.search_paper(i)
    query_type1.append(results)
```
The output is an object containing the following information:
* Paper IDs (includes SS's internal ID, as well as external IDs such as DOI, arXiv, Pubmed, etc. where available)
* Title
* Authors
* Publicaiton venue
* Publication year
* Field of Study
* PDF availability (indi)


From the Semantic Scholar API, we get the datasets labeled **“query_typex_abs,”** where the x  in the name = 1,2,3,4,5,6 refers to the query type. These datasets contain the following variables: **paper title, abstract, corpus ID (also called paper ID), author IDs, Digital Object identifiers (DOIs), publication year,** the **journal**  where the paper was published, and the **dataset ID**. These metadata datasets will be merged with the metadata datasets we get from the NLP4DEV API website.

## Citations

The following papers informed our approach: {cite}`Fast2016`,{cite}`Chen2006`.


```{bibliography}
```