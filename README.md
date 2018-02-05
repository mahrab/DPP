# DPP

This is the source code for a project to automatically label data in an unsupervised fashion, for use in training a supervised machine learning algorithm. The unlabeled data in question is a set of consumer reviews of a laptop, focussing on a number of different aspects of the product. It does so using a Large Margin Determinental Point Process (DPP).

DPP is an unsupervised method that, given a ground set of objects, Y, selects a subset, y, that is maximally diverse. Traditional DPP methods rely on a symmetric, positive semi-definite matrix, L, used to define the pairwise similarity between any two elements, i and j, sampled from Y. Large Margin DPP calculates the kernel matrix L in a manner that takes both the quality and the pairwise similarity of the elements i and j into account. Large Margin DPP therefore takes both quality and diversity into account when selecting an optimal subset. The quality and pairwise similarity are measured using metrics proveded by the user. In this case, quality is measured using LexRank scores, and pairwise similarity is measure using vectors assigned to each review by an LSTM.

When running the code, run Similarity.py and Quality.py first, to generate matlab files containing the similarity and quality matrices respectively. Afterward, run DPP.m to generate the matrix, L, and select the subset, y. Finally, run Summary.py to generate a JSON file containing the selected reviews for each aspect.

Large Margin DPP - Gong et al. https://arxiv.org/pdf/1411.1537v2.pdf
