Retrain GloVe on the corpus you prefer from the stackexchange archive (https://archive.org/download/stackexchange/):

- Clone GloVe repo inside retrain-glove: git clone http://github.com/stanfordnlp/glove
- Make it                              : cd glove && make
- Create folder "data"                 : cd ..
                                       : mkdir data
                                       : cd data
- Download and unzip data              : wget https://archive.org/download/stackexchange/stackoverflow.com-Posts.7z
                                       : 7za e "dataset".7z (eg: stackoverflow.com-Posts.7z)
- Create corpus.txt                    : cd glove
- Changes to demo.sh                   : Remove the script from if to fi after 'make'. Replace the CORPUS name with your file name 'corpus.txt' 

Run the demo.sh                        : ./demo.sh

Notes:
- Make sure your corpus file is in the correct format.You'll need to prepare your corpus as a single text file with all words separated by   one or more spaces or tabs. If your corpus has multiple documents, the documents (only) should be separated by new line characters.

- corpus.txt is created from ./data/Posts.xml : Please check that it exists and comes from the desired "dataset"

Load trained model:
...
