# Topic Modeling and Sentiment Analysis

We make use of the NLP4Dev API.

We run the abstracts from the **“query_typex_abs”** through the NLP4DEV API. We convert the response objects into three types of datasets: **“NLP4DEV_qx”**, **“topic_importance_querytypex”**, and **“nlpdev_queryx"**. **“NLP4DEV_qx”** datasets contain the metadata from the NLP4DEV API: country counts, country group, JDC tags, the tag counts, the dataset ID, Corpus ID, and the country that is mentioned the most.  “nlpdev_queryx datasets containing the raw data dump from the NLP4DEV API. Basically, “nlpdev_queryx is the raw version of NLP4DEV_qx. These datasets can be found in the NLP4DEV datasets folder on the cloud. 

“topic_importance_querytypex” datasets contain the topic importance. The default number of topics returned from the NLP4DEV API is 10.


We merge the semantic scholar metadata(**“query_typex_abs.csv”**) and the metadata (**“NLP4DEV_qx”**) files we get from running the abstracts through the NLP4DEV API. The datasets labeled **“ss_NLP4_queryx_merge”** and **“qx_ss_nlpdev_master”** are the results of different types or merges from the two metadata sources. If in doubt, use the **“qx_ss_nlpdev_master”** datasets.

**“qx_datasets”** contain the  datasets that returned queries from the NLP4DEV API for each query. This returns the datasets that do not have HTML tags. 
**“qx_qx_sample_streamlit_demo”** and **"qx_qx_demo_short"** contain the following variables: **title**, **abstract**, **dataset number**, and **query number**.
**“qx_qx_sample_results”** datasets contain the information we need to display in the app. It contains the following variables: **dataset title**, **paper title**, **relevance**, **JDC tags**, **value**, and **topic percentages**.

## Citations

## Citations

The following papers informed our approach: {cite}`Fast2016`,{cite}`Chen2006`.


```{bibliography}
```