# LSMDC-Context

Instructions and code to generate the Large Scale Movie Description Challenge (LSMDC) - Context dataset used in the paper
[Enriching Video Captions With Contextual Text](https://arxiv.org/abs/2007.14682). This is an augmented version of the original 
dataset with movie scripts as contextual text. The source code of the model described in the paper can be found in the 
[S2VT-Pointer](https://github.com/primle/S2VT-Pointer) repository.

## Disclaimer
The source code was written for my master thesis with limited time, without the intention to publish it. Because of legal
reasons, the dataset used in the publication cannot be shared. This repository contains the steps to create the dataset
and store it in a tokenized format used in [S2VT-Pointer](https://github.com/primle/S2VT-Pointer).

## Usage
1) Download the [LSMDC](https://sites.google.com/site/describingmovies/download) 2019 dataset. (access request needed)
   * Task 1: Training, validation and test annotations with "SOMEONE"-s
   * The additionally provided training and validation annotations with original character names
   * The precomputed I3D features (4.7G) pretrained on Imagenet and Kinetics, and Resnet152 features (9.9G) pretrained on Imagenet. 
   ```bash
   
   ```