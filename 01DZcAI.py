# Шаг 1: Импортируем библиотеку requests
import requests

# Шаг 2: Формируем URL для поиска репозиториев с кодом "html"
# GitHub API: https://docs.github.com/en/rest/search/search#search-repositories
url = "https://api.github.com/search/repositories"

# Параметры запроса: ищем репозитории, где встречается слово "html"
params = {
    "q": "html",  # поисковый запрос
    "sort": "stars",  # сортировать по звёздам
    "order": "desc",  # по убыванию (сначала самые популярные)
    "per_page": 5  # вернуть только 5 результатов (чтобы не перегружать вывод)
}

# Важно: GitHub требует указывать заголовок User-Agent
headers = {
    "User-Agent": "MyPythonApp/1.0"  # можно указать своё название
}

# Отправляем GET-запрос
response = requests.get(url, params=params, headers=headers)

# Шаг 3: Печатаем статус-код ответа
print(f"📡 Статус-код: {response.status_code}")

# Шаг 4: Печатаем содержимое ответа в формате JSON
data = response.json()

# Выводим всё, что пришло от сервера (может быть много текста!)
# print("📦 Полный ответ:", data)

# 🔍 Или выведем только полезную информацию — названия репозиториев:
print("\n🔎 Найдено репозиториев:", data.get("total_count", 0))
print("\n📋 Топ-5 по популярности:")

for repo in data.get("items", []):
    name = repo.get("full_name")  # имя владельца + название репо
    stars = repo.get("stargazers_count")  # количество звёзд
    desc = repo.get("description") or "без описания"  # если нет описания — пишем "без описания"

    print(f"⭐ {stars} | {name} | {desc[:60]}...")