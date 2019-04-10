Retrain GloVe:

- Clone GloVe repo inside retrain-glove: git clone http://github.com/stanfordnlp/glove
- Make it                              : cd glove && make
- Create folder "data"                 : cd ..
                                       : mkdir data
- Download and unzip data              :
- Rename posts and tags xml files      : cd data
                                       : mv ... posts.xml
                                       :
- changes to glove/demo.sh             : Remove the script from if to fi after 'make'. Replace the CORPUS name with your file name 'corpus.txt' There is another if loop at the end of file 'demo.sh':(if [ "$CORPUS" = 'text8' ]; then) -->Replace text8 with you file name.

Run the demo.sh                        : $ ./demo.sh

Notes:
Make sure your corpus file is in the correct format.You'll need to prepare your corpus as a single text file with all words separated by one or more spaces or tabs. If your corpus has multiple documents, the documents (only) should be separated by new line characters.

Load:
...
