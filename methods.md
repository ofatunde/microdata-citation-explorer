# Methods

This paper describes a methodology for systematically monitoring the use of UNHCR microdata. We develop a workflow for searching literature repositories with an initial focus on academic research, but with plans to include “grey literature” in the future. We take a three-step approach to producing a comprehensive and informative list of the papers that reference a particular dataset. First, for a given dataset, we begin by combining information from the metadata fields available for the study and using these terms to form multiple and overlapping search queries; these include the primary authoring organization, the year of the survey, and the country in which the study was carried out. Second, we use the generated query strings to generate sets of search results for each UNHCR microdata set from Semantic Scholar.
Third, once a list of possible references has been compiled for each dataset, we compute for each reference a measure of its relevance to the dataset in question using Natural Language Processing (NLP). We first generate a list of topics contained in each reference using the topic modeling and analysis tools made available by NLP4Dev (https://www.nlp4dev.org/). To classify each possible reference by relevance to a given dataset, we consider 1) the share of identified topics related to forced displacement, 2) the set of countries mentioned in the reference, and 3) the frequency of a curated set of key-word tags related to forced displacement. 



Below we summarize the three primary methods that were used throughout this process. Each is described in greater detail in a link on the left side of the page.

|  	| **Step** 	| **Input** 	| **Output** 	| **Benefit** 	|
|---	|:---:	|:---:	|:---:	|:---:	|
| 1 	| [Query generation](methods/query-generation.md) 	| Metadata for an individual dataset 	| List of query strings 	| Information about topics and countries included, field of study and nature of use 	|
| 2 	| [Semantic search](methods/semantic-search.md) 	| One or more query strings for each dataset 	| List(s) of citing papers 	| Information about topics and countries included, field of study and nature of use 	|
| 3 	| [Topic modeling/ sentiment analysis](methods/topic-modeling-and-sentiment-analysis.md) 	| Text of individual citing papers 	| Information about topics and countries included, field of study and nature of use 	| We can determine how the dataset is used in each matching publication without resorting to manual review/analysis 	|

## Tools
We use two external tools: APIs powered by Semantic Scholar and NLP4Dev. We load corpuses from both and store them in [Google Cloud Storage] (https://console.cloud.google.com/storage/browser/mdl-explorer-app;tab=objects?project=unhcr-microdata&prefix=&forceOnObjectsSortingFiltering=false).

## Citations

The following papers informed our approach: {cite}`Cutting1992`.


```{bibliography}
```