Retrain GloVe on the corpus you prefer from the stackexchange archive:

- Clone GloVe repo inside retrain-glove: git clone http://github.com/stanfordnlp/glove
- Make it                              : cd glove && make
- Create folder "data"                 : cd ..
                                       : mkdir data
                                       : cd data
- Download and unzip data              : wget https://archive.org/download/stackexchange/"dataset".7z
                                       : 7za e "dataset".7z (eg: ai.stackexchange.com.7z)
- Create corpus.txt                    : cd glove
- Changes to demo.sh                   : Remove the script from if to fi after 'make'. Replace the CORPUS name with your file name 'corpus.txt' There is another if loop at the end of file 'demo.sh':(if [ "$CORPUS" = 'text8' ]; then) -->Replace 'text8' with 'corpus.txt'.

Run the demo.sh                        : ./demo.sh

Notes:
- Make sure your corpus file is in the correct format.You'll need to prepare your corpus as a single text file with all words separated by   one or more spaces or tabs. If your corpus has multiple documents, the documents (only) should be separated by new line characters.

- corpus.txt is created from Posts.xml and Tags.xml : Please check that they exist and are extracted from the desired "dataset"

Load trained model:
...
