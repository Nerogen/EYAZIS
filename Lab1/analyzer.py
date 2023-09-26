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
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

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
    tokens = [i[0] for i in sorted_words]
    for i in text.split():
        if i.lower() in tokens:
            tokens[tokens.index(i.lower())] = i
    return tokens

import nltk
from nltk.corpus import wordnet

# Инициализация NLTK (один раз в начале программы)
nltk.download('wordnet')

def search_with_synonyms(query):
    # Выполните логический поиск с исходным запросом
    search_results = perform_logical_search(query)

    # Проверьте результаты поиска
    if not search_results:
        # Если результатов нет, найдите синонимы для слов в запросе
        synonym_query = get_synonym_query(query)

        # Предложите пользователю альтернативный запрос с синонимами
        user_choice = input(f"No results found for '{query}'. Try '{synonym_query}'? (y/n): ")

        if user_choice.lower() == 'y':
            # Пользователь согласился, выполните поиск с альтернативным запросом
            search_results = perform_logical_search(synonym_query)

    # Обработка результатов поиска и вывод пользователю
    process_search_results(search_results)

def get_synonym(word):
    # Разбиваем запрос на слова и находим синонимы для каждого слова

        synonyms = find_synonyms(word)
        
        while word in synonyms:
            synonyms.remove(word)
        if synonyms:
            return synonyms[0]  # Берем первый найденный синони

def find_synonyms(word):
    # Используем WordNet для поиска синонимов
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def perform_logical_search(query):
    # Здесь вы можете реализовать логику выполнения логического поиска
    # и возврата результатов в виде списка документов
    # Примечание: Этот шаг зависит от вашей спецификации поисковой системы

    # Возвращаем фиктивный результат для примера
    return ['Document1', 'Document2']

def process_search_results(results):
    # Здесь вы можете обработать результаты поиска и вывести их пользователю
    # Например, отобразить найденные документы и их содержимое

    for i, document in enumerate(results, start=1):
        print(f"Result {i}: {document}")




if __name__ == '__main__':
    analyse_text(text)
