import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Загрузка стоп-слов
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

# Ваш текст
text = """If you’re reading this article, it’s likely because the
number 333 seems to be popping up everywhere you look. Did
your eyes happen to drift toward the clock at exactly 3:33?
Maybe your morning coffee inexplicably cost $3.33. So, what does it mean that this number is
following you around? If you’re seeing the angel number 333, it holds a great deal of significance
for your love life, your finances, your spiritual wellbeing, and more. We’ve compiled a list of
all of the different ways to interpret the angel number 333, so you can figure out what your guardian
angels are trying to tell you...."""


def analyse_text(text):
    # Токенизация
    words = word_tokenize(text)

    # Удаление стоп-слов
    filtered_words = [word for word in words if word.isalnum() and word.lower() not in stop_words]

    # Подсчет частотности
    fdist = FreqDist(filtered_words)

    # Подготовка данных для TF-IDF
    corpus = [' '.join(filtered_words)]

    # Расчет TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Получение списка слов и их TF-IDF значений
    word_tfidf = list(zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0]))

    # Сортировка по TF-IDF
    sorted_words = sorted(word_tfidf, key=lambda x: x[1], reverse=True)

    # Вывод списка ключевых слов
    for word, tfidf in sorted_words:
        pass
        # print(f'{word}: {tfidf:.4f}')
    return [i[0] for i in sorted_words]


if __name__ == '__main__':
    analyse_text(text)
