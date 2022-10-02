# Do I cope with regulation? - tumai-makeathon22
description todo

## How to run 
TODO

## Results
TODO

## Makeathon storyline

**Friday**

We developed 2 different approaches to directly classify the description as a low/high risk. One was using the deberta model on binary classification, the second one tried to use simple KNearestNeighbours classifier on advanced sentence-transformers embeddings. However, we discovered that we have too little & unrepresentative data (only 4 out of 10 classes....).

**Saturday**

To deal with lack of useful data, we decided that instead of directly classifying as low/high risk, we will try to associate some critical topic from the regulation itself. As the presence of the critical topics directly implies the high-risk. However, we did not have any training data for that. To obtain them we tried 2 different approaches: 1) find some available datasets and 2) generate the descriptions by GPT3. The 1) was not possible. The 2) generated surprisingly nice startups descriptions from the highly critical topics.

We have again used deberta and sentence-transformers models for multilabel classification into classes corresponding to the critical topics or low-risk class. Despite being able to teach the model to distinguish well the topics on the generated data, when tested on these few high-risk examples we have been provided, it was not doing much good.

So, finally, in the deepest desperation on Saturday night we decided to try one more approach called semantic search against the regulation annex document. The first idea was to use GPT3 again, Rob went for that. But it showed just mediocre results. Michal followed different path and used sentence-transformers to embed the regulations sections/critical topics and also the descriptions. At this moment, Michal got incredibly good results. It looked too good to be true, but we checked it also on some descriptions imagined by Moritz and it still worked well. So Rob stopped doing on the GPT3 and move on to human involvement prediction. And Michal moved on to host the frontend and finish the backend.

**Sunday**

In the morning the nasty bug was discovered in Michal's too good to be true approach. It basically just said that the more descriptions you gimme me, the lower risk each one has. Anyway it was far from working good. So, Michal went for combining the previously developed methods to get the best out of them. However, due to slow update rate of docker hub, these changes would be never uploaded on time. Fortunately, Rob managed to somehow finish the GPT3 semantic search, so it was eventually running as workhorse for the risk estimation. The bad thing is that it was not really good. 

So, despite several methods developed, no satisfiable results were achieved. Still, the proposed results are often orthogonal and may work much better when combined in a hybrid fashion. 
