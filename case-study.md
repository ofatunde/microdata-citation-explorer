# Case Study: VaSyR 2018

In this section, we present an end-to-end example using a sample dataset.

## Query generation

Each of the six queries returned X potentially relevant papers.

```{code-cell} ipython3
:tags: ["output_scroll","hide-input"]
import pandas as pd
df = pd.read_csv("../data/semantic_scholar_query_results_with_web_count.csv")
print(df[df["id"] == 189])
```

## Semantic Search
Each of the six queries returned X potentially relevant papers.

```{code-cell} ipython3
:tags: ["output_scroll","hide-input"]
import pandas as pd
df = pd.read_csv("../data/semantic_scholar_query_results_with_web_count.csv")
print(df[df["id"] == 189])
```

## Topic Modeling
Out of the XX papers returned across the six query types, YYY had abstracts available in either the NLP4Dev or Semantic Scholar corpuses, and ZZZ had full body text available.

These were used as inputs to the NLP4Dev API, as described in [Section 3.5](methods/topic-modeling-and-sentiment-analysis.md).

XXX were defined as relevant.

## Model Output
Following manual review of the papers identified automatically, XXX were confirmed as relevant. Of these XXX, YYY had previously been identified through the manual procedure, and ZZZ were new.

This represents a XXX percent improvement over the baseline.

## Evaluating Model Performance
Based on our selected evaluation metric, Query X performed most effectively

## Network analysis
Of the papers that referenced this dataset, XYZ came from ABC geographies and ABC instutions.