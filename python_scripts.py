
### categorize polarity
pol = dataset['Polarity']
sentiment = []
for p in pol:

    if p > 0.7:
        sentiment.append('highly positive')
    elif p > 0.5:
        sentiment.append('positive')
    elif p > 0.2:
        sentiment.append('somewhat positive')
    elif p > -0.2:
        sentiment.append('neutral')
    elif p > -0.5:
        sentiment.append('somewhat negative')
    elif p > -0.7:
        sentiment.append('negative')
    else:
        sentiment.append('very negative')

dataset['sentiment'] = sentiment

### categorize subjectivity
sub = dataset['Subjectivity']
subjectivity = []
for p in sub:

    if p > 0.7:
        subjectivity.append('highly subjective')
    elif p > 0.5:
        subjectivity.append('subjective')
    elif p > 0.2:
        subjectivity.append('somewhat subjective')
    else:
        subjectivity.append('not subjective')

dataset['Sujective_cat'] = subjectivity

#plot histogram on powerBI
import matplotlib.pyplot as plt

plt.hist(dataset['Value.Polarity'])
plt.title('Distribution of the Polarity')
plt.show()