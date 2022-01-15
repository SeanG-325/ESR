# Introduction

This is the code repository for the paper "Extract, Select and Rewrite: A New Modular Sentence Summarization Method".


# Code

The codes are used to create the datasets for subtasks (content selector and rewriter), including triples extraction, redundence deletion and labeling, etc.

## Subtask Datasets

To construct the subtask dataset for content selector, use 

> "python3 selector_data.py"

The created files include "_triple" , "_article" and "_label", which will be used for finetuning content selector. 

To construct the subtask dataset for rewriter, use 

> "python3 rewriter_data.py"

The created files include "_concat_triples" and "_summary", which will be used for finetuning rewriter.

## Finetuning

We used [fairseq](https://github.com/pytorch/fairseq/) for finetuning content selector and rewriter. 
The subtasks datasets need to be preprocessed under the [rules](https://github.com/pytorch/fairseq/blob/main/examples/roberta/README.custom_classification.md) before before finetuning.
The command and the hyperparameters we used are in the `selector.sh` and `rewriter.sh`.

## Inference

Using `python3 selector_data.py`. The rewrited summaries are in `rewrited`.



## Requirements
-   [PyTorch](http://pytorch.org/)  version >= 1.5.0
-   Python version >= 3.6
-   [fairseq](https://github.com/pytorch/fairseq/)
-   Rouge
-   [stanford_openie](https://github.com/philipperemy/stanford-openie-python)
-   [ollie](https://github.com/knowitall/ollie)
-    [uwopenie](https://github.com/dair-iitd/OpenIE-standalone)
