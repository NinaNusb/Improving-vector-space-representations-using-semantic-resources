## Program Name: Word Retrofitting Tool

### Overview:
The Word Retrofitting Tool is a command-line program that performs retrofitting on word vectors using a lexicon of word relations. Retrofitting aims to improve the quality and semantic coherence of word vectors by incorporating information from the lexicon.

### Prerequisites:
- Python 3.x
- Required Python packages: numpy, pandas

### Requirements:
In order to run the Word Retrofitting Tool, make sure you have the following models and libraries downloaded:
#### For French:
##### Pre-trained Word Vectors:
- Download `vecs100-linear-frwiki.zip` or `vecs50-linear-frwiki.bz2` file for French word vectors trained on a Wikipedia dump.
  - Training on a dump of Wikipedia (frwiki-20140804-corpus.xml.bz2 downloaded [here](http://linguatools.org/tools/corpora/wikipedia-monolingual-corpora/))
  - Preprocessing:
    - Use `xml2txt.pl` to remove XML tags.
    - Tokenize the text using `sxpipe-light` (e.g., `perl ~/installation/melt-2.0b7/sxpipe-melt/segmenteur.pl < frwiki_raw.txt > frwiki_tokenized.txt`).
  - The word vectors are trained using `vecs100` or `vecs50` with the following command:
    - `./word2vec -train frwiki_tokenized.txt -output vecs50 -threads 2 -min-count 100 -cbow 0 -negative 10`
- Alternatively, you can use other word embeddings such as the `cc.fr.300.vec` embeddings. Refer to [fastText documentation](https://fasttext.cc/docs/en/crawl-vectors.html) for more details.

##### Semantic Resources:
- Download WOLF (WordNet-LMF) from [here](http://almanach.inria.fr/software_and_resources/downloads/wolf-1.0b4.xml.bz2).

##### Evaluation Dataset:
- For lexical similarity evaluation, use the `rg65_french.txt` file.
- For sentiment analysis evaluation, you can use any benchmark dataset you find online. Please cite the source of the dataset in your report.

#### For English:
##### Pre-trained Word Vectors:
- Download `vectors_datatxt_250_sg_w10_i5_c500_gensim_clean.tar.bz2` file for English word vectors.
- The word vectors are trained using the `gensim` library with the following configuration:
  - `gensim.models.Word2Vec(size=250, min_count=500, window=8, sample=1e-3, workers=8, sg=1, hs=0, negative=10, iter=5)`

##### Semantic Lexicons:
- Download the PPDB (Paraphrase Database) lexical resource from [here](http://paraphrase.org/#/download) and use the `ppdb lexical xl` size.
- Use WordNet for semantic relations.

##### Evaluation Dataset:
- For lexical similarity evaluation, use the `ws353.txt` file.
- For sentiment analysis evaluation, use the `stanford_sentiment_analysis.tar.gz` file from [Stanford NLP](https://nlp.stanford.edu/sentiment/).


### Usage:
1. Open the command-line interface (CLI) or terminal.
2. Navigate to the directory where the Word Retrofitting Tool is located.
3. Run the following command to execute the program:
    'python retrofit_tool.py -input <input_file> -lexicon <lexicon_file> -output <output_file>'
    Replace `<input_file>` with the path to the file containing the original word vectors.
    Replace `<lexicon_file>` with the path to the file containing the lexicon of word relations.
    Replace `<output_file>` with the desired path and filename for the output file.
    
4. The program will start executing and perform retrofitting on the word vectors using the specified lexicon.
5. Once the process is completed, the retrofitted word vectors will be saved in the specified output file.

### Optional Arguments:
- `-input <input_file>`: Specifies the path to the file containing the original word vectors. Default: `vectors.txt`.
- `-lexicon <lexicon_file>`: Specifies the path to the file containing the lexicon of word relations. Default: `lexicon.txt`.
- `-output <output_file>`: Specifies the path and filename for the output file to save the retrofitted word vectors. Default: `output_vectors.txt`.

### Example:
To retrofit word vectors using a custom input file, lexicon file, and output file, use the following command:
python retrofit_tool.py -input input_vectors.txt -lexicon my_lexicon.txt -output retrofitted_vectors.txt


### Notes:
- Ensure that the input file, lexicon file, and output file paths are correctly specified and accessible.
- The program may take some time to complete retrofitting, depending on the size of the word vectors and the lexicon.

### Authors:
- Nina alias NinaNusb
- Deeksha alias deekode99
- Iness alias IAiness
