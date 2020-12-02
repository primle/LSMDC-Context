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
1) Download the [LSMDC](https://sites.google.com/site/describingmovies/download) 2019 dataset (access request needed):
   * The precomputed I3D features (4.7G) pretrained on Imagenet and Kinetics, and Resnet152 features (9.9G) pretrained on Imagenet.
   * The Task 1: Training, validation and test annotations with "SOMEONE"-s
   * The additionally provided training and validation annotations with original character names
   * The Standard LSMDC 2016/17 version. Has to be done with the provided script and valid username/password. 
   Uncomment the download video section, as only the captions are needed.
   * The following files should be present (both from the 2019 and 2017 challenge):
   
       ```bash
       ./lsmdc2019/task1/LSMDC16_annos_training_someone.csv
       ./lsmdc2019/task1/LSMDC16_annos_val_someone.csv
       ./lsmdc2019/task1/LSMDC16_annos_test_someone.csv
       ./lsmdc2019/ner_coref/LSMDC16_annos_training.csv
       ./lsmdc2019/ner_coref/LSMDC16_annos_val.csv
       ./lsmdc2017/annotations-original.csv
       ./lsmdc2017/annotations-someone.csv
       ```
     
2) Download the movie scripts from imsdb with *download_moviescripts.py*. It stores the html pages as well as the extracted movie script texts.