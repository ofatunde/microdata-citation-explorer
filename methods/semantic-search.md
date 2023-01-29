# Semantic search

We made use of the Semantic Scholar API.

From the Semantic Scholar API, we get the datasets labeled “query_typex_abs,” where the x  in the name = 1,2,3,4,5,6 refers to the query type. These datasets contain the following variables: paper title, abstract, corpus ID (also called paper ID), author IDs, Digital Object identifiers (DOIs), publication year, the journal where the paper was published, and the dataset ID. These metadata datasets will be merged with the metadata datasets we get from the NLP4DEV API website.

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