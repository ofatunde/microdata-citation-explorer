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

# Topic Modeling and Sentiment Analysis

We imported the documents available in the Semantic Scholar and NPL4Dev corpuses.

We make use of the [NLP4Dev API] (https://www.nlp4dev.org/content-api). Depending on whether the paper contents are available in parsed or PDF formay, we use either the "Analyze Text" or the "Analyze File" endpoint. In both cases we make use of the Mallet topic model, which allows us to use the abstract or full text of a paper as an input and retrieve information about the paper content as an output.

% ```{code-cell}
% def analyze_text(input_text:str)->pd.DataFrame:
%    url = "https://www.nlp4dev.org/nlp/models/mallet/analyze_text"
%    text = input_text
%    payload = { "model_id": "6fd8b418cbe4af7a1b3d24debfafa1ee", "text": text }
%    headers = { 'Content-Type': 'application/x-www-form-urlencoded',}
%    response = requests.request("POST", url, headers=headers, data=payload) # This returns a dictionary in string form
%
%    # Get metadata from the NLP4DEV API
%    resp = eval(response.text) # this is how we recover the dictionary from the string
%
%    #use the keys of the dictionaries to get the metadata. We have a problem here because the values are lists of different 
%    #lengths which is hard to convert to dataframes.
%
%    dataframe = pd.DataFrame(resp.get('doc_topic_words'))
%    country_counts = resp.get('country_counts')
%    country_details = resp.get('country_details')
%    country_groups = resp.get('country_groups')
%    tag_counts = resp.get('jdc_tag_counts')
%    return dataframe, list([country_counts, country_details, country_groups, tag_counts])
% ```

We run the abstracts or PDF text from the Semantic Scholar results through the NLP4DEV API, which returns the following information:
%We convert the response objects into three types of datasets: **“NLP4DEV_qx”**, **“topic_importance_querytypex”**, and **“nlpdev_queryx"**. **“NLP4DEV_qx”** datasets contain the metadata from the NLP4DEV API: 
* country counts
* country group
* JDC tags (a list of phrases defined by NLP4Dev as being related to forced displacement)
* the tag counts
* dataset ID
* Corpus ID 
* the country that is mentioned the most. 

The JDC tags include the following: 
* "asylum seeker"
* "climate refugee"
* "country of asylum"
* "exile"
* " forced displacement"
* "host community"
* "internally displaced population"
* "ocha", "population of concern"
* "refugee"
* " refugee camp"
* "repatriate"
* "resetlement area"
* "returnee"
* "stateless"
* "unhcr"

% **“nlpdev_queryx"** datasets containing the raw data dump from the NLP4DEV API. Basically, **“nlpdev_queryx"**is the raw version of **"NLP4DEV_qx"**. These datasets can be found in the NLP4DEV datasets folder on the cloud.



```{code-cell}

def NLP4Dev(abstract_or_fulltext,text_source):

    if(abstract_or_fulltext == 'PDF'):
        #extract output using "Analyze_file" endpoint
        url = "https://www.nlp4dev.org/nlp/models/mallet/analyze_file"
        payload={"model_id": "6fd8b418cbe4af7a1b3d24debfafa1ee"}
        files=[('file',('mdl-explorer-app/data/02637758211070565.pdf',open('data/02637758211070565.pdf','rb'),'application/pdf'))]
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        resp = eval(response.text)
        topic_distribution = resp.get('doc_topic_words')
        country_distribution = resp.get('country_details')
        tag_distribution = resp.get('jdc_tag_counts')
    elif(abstract_or_fulltext == 'parsed_PDF'):
        #extract output using "Analyze_text" endpoint on full extracted text
        url = "https://www.nlp4dev.org/nlp/models/mallet/analyze_text"
        payload = { "model_id": "6fd8b418cbe4af7a1b3d24debfafa1ee", "text": text_source }
        headers = { 'Content-Type': 'application/x-www-form-urlencoded',}
        response = requests.request("POST", url, headers=headers, data=payload)
        resp = eval(response.text)
        topic_distribution = resp.get('doc_topic_words')
        country_distribution = resp.get('country_details')
        tag_distribution = resp.get('jdc_tag_counts')
    elif(abstract_or_fulltext == 'abstract_only'):
        #extract output using "Analyze_text" endpoint on abstract text
        url = "https://www.nlp4dev.org/nlp/models/mallet/analyze_text"
        payload = { "model_id": "6fd8b418cbe4af7a1b3d24debfafa1ee", "text": text_source }
        headers = { 'Content-Type': 'application/x-www-form-urlencoded',}
        response = requests.request("POST", url, headers=headers, data=payload)
        resp = eval(response.text)
        topic_distribution = pd.DataFrame(resp.get('doc_topic_words'))
        country_distribution = pd.DataFrame(resp.get('country_details'))
        tag_distribution = pd.DataFrame(resp.get('jdc_tag_counts'))
        topic_39_percentage = abs(topic_distribution.value[2])
       
        if len(country_distribution) > 0:
            df_indexid = country_distribution.set_index('count')
            majority_country = df_indexid.loc[max(country_distribution['count'])]['name']
        else:
            majority_country = 'NONE'
        
        jdc_tag_count = len(tag_distribution)

        
        return topic_distribution , country_distribution , tag_distribution , majority_country , topic_39_percentage, jdc_tag_count
```

\[ include a sample of text showing topic distribution \]

We use the outputs from the NLP4Dev to calculate a "relevance" score for each dataset-paper compbination

```{code-cell}
def calculate_relevance(ref,dataset, topic_39_percentage, jdc_tag_count,majority_country,relevance_threshold, paper_title = None):
    #We should define ref as a global variable if the app will always be reading from that one file
    # removed the paper titles argument because we are not using it anywhere in the function. Check with Mureji.

    dataset_country = ref.loc[ref['id'] == dataset, 'nation'].iloc[0]
    dataset_title = ref.loc[ref['id'] == dataset, 'title'].iloc[0]
    if((topic_39_percentage > relevance_threshold)and (majority_country == dataset_country)):
        relevance = 1
    elif((topic_39_percentage > relevance_threshold)and (majority_country != dataset_country)):
        relevance = 0.5
    else:
        relevance = 0
        
    final_output = pd.DataFrame(list(zip([dataset_title],[relevance]
                    ,[topic_39_percentage]
                    ,[jdc_tag_count])), columns = ["Dataset Name","Relevance","topic 39 Percentage", "JDC Tag Counts"])  
    return final_output
```

% “topic_importance_querytypex” datasets contain the topic importance. The default number of topics returned from the NLP4DEV API is 10.

The outputs of this relevance function are returned to users in our [user tool](implementation-options.md).

% We merge the semantic scholar metadata(**“query_typex_abs.csv”**) and the metadata (**“NLP4DEV_qx”**) files we get from running the abstracts through the NLP4DEV API. The datasets labeled **“ss_NLP4_queryx_merge”** and **“qx_ss_nlpdev_master”** are the results of different types or merges from the two metadata sources. If in doubt, use the **“qx_ss_nlpdev_master”** datasets.

% **“qx_datasets”** contain the  datasets that returned queries from the NLP4DEV API for each query. This returns the datasets that do not have HTML tags. 
%**“qx_qx_sample_streamlit_demo”** and **"qx_qx_demo_short"** contain the following variables: **title**, **abstract**, **dataset number**, and **query number**.
%**“qx_qx_sample_results”** datasets contain the information we need to display in the app. It contains the following variables: **dataset title**, **paper title**, **relevance**, **JDC tags**, **value**, and **topic percentages**.

## Citations

The following papers informed our approach: {cite}`Fast2016`,{cite}`Chen2006`.


```{bibliography}
```