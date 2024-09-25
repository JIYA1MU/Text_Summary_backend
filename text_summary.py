import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text = """OpenAI’s text-to-video generator AI model Sora will be available to the public in the coming months. Chief technology officer of OpenAI, Mira Murati, in an interview with The Wall Street Journal said that the AI powered video generation model will be made available to the public “definitely this year”, likely in “a few months.”
Responding to a question related to computational power required for Sora in comparison to company’s other products like ChatGPT and DALL-E, Murati said that the video generation model is currently a “research output” and is “much more expensive”. She added, the company is currently working on optimising Sora so that it could be made available to the public “at similar cost eventually to what we saw with DALL-E.”
Murati said that the company is considering “the issues of misinformation and harmful bias” that the video generator might cause, especially with the US election in November. “We will not be releasing anything that we don't feel confident on when it comes to how it might affect global elections,” she added.
Sora is currently under the “Red Teaming” process, which is the testing stage where the AI tool is tested by people to identify vulnerabilities, biases and other harmful issues. Responding to questions regarding the limits of the model, Murati said that the company wants to keep consistency on their platform. She said that just like with the company’s image generator model DALL-E, Sora will likely have “a similar policy” such as restrictions on generating images of public figures.
 Murati confirmed that “publicly available” videos and licensed video from Shuttershock were used as part of the training data for the video generation model. However, when asked if videos from YouTube, Facebook and Instagram were used in training, Murati said that if they were publicly available to use, they might have, but she cannot say with certainty.
"""
def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    #print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    #print(doc)
    tokens = [token.text for token in doc]
    #print(tokens)
    wordfreq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in wordfreq.keys():
                wordfreq[word.text] = 1
            else:
                wordfreq[word.text] += 1
    #print(wordfreq)
    max_freq = max(wordfreq.values())
    #print(max_freq)
    for word in wordfreq.keys():
        wordfreq[word] = wordfreq[word]/max_freq
    #print(wordfreq)
    sent_tokens = [sent for sent in doc.sents]
    #print(sent_tokens)
    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in wordfreq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = wordfreq[word.text]
                else:
                    sent_scores[sent] += wordfreq[word.text]
    #print(sent_scores)
    select_len = int(len(sent_tokens) * 0.3)
    #print(select_len)
    summary = nlargest(select_len,sent_scores, key = sent_scores.get)
    #print(summary)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print(f"Text :: {text}")
    # print(f"Summary:: {summary}")
    # print(f"Length of original text:: {len(text.split(' '))}")
    # print(f"Length of Summary:: {len(summary.split(' '))}")
    # return summary,doc, len(rawdocs.split(' ')), len(summary.split(' '))
    return summary