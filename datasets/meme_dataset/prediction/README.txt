These are the training and testing datasets used in the prediction experiments in:

William Yang Wang and Miaomiao Wen, "I Can Has Cheezburger? A Nonparanormal Approach to Combining Textual and Visual Information for Predicting and Generating Popular Meme Descriptions", to appear in the 2015 Conference of the North American Chapter of the Association for Computational Linguistics – Human Language Technologies (NAACL HLT 2015), long paper, Denver, CO., USA, May 31-June 5, ACL.

train.feat: training data. 
test.feat: test data.
VisionFeatures.txt: the extracted vision features for each image. 

Data format for feature files:
the image name, the reciprocal rank of the popular votes (label), the unigram of the meme description, bigram, named entities (if any),
part of speech features, dependency triples, and semantic features. 

Example:
Y-U-No,0.0526315789473684 amy whinehouse y u no go to rehab? . <start>_amy amy_whinehouse whinehouse_y y_u u_no no_go go_to to_rehab? rehab?_. ._<end> amy/person whinehouse/person amy_nnp whinehouse_nnpww no_dt go_nn to_to rehab_vb aux_to_rehab dep_go_whinehouse infmod_rehab_go prep_whinehouse_amy null_amy_root FE_Quantity_no FE_Goal_to_rehab

Y-U-No: the name of the image.
0.0526315789473684: the reciprocal rank of the votes.
amy whinehouse y u no go to rehab?: the unigrams of this meme description.
 <start>_amy amy_whinehouse whinehouse_y y_u u_no no_go go_to to_rehab? rehab?_. ._<end>: the bigrams of the description.
amy/person whinehouse/person: named entities.
amy_nnp whinehouse_nnpww no_dt go_nn to_to rehab_vb: part of speech tags.
aux_to_rehab dep_go_whinehouse infmod_rehab_go prep_whinehouse_amy null_amy_root: dependency triples.
FE_Quantity_no FE_Goal_to_rehab: semantic features.
