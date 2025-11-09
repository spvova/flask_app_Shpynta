from flask import Flask # З модуля flask import class Flask
app = Flask (__name__)   # Створення екземпляра класу Flask для нашої веб-програми

@app.route('/')         # URL '/' для обробки обробником маршруту main()
def main():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True) # Запуск вбудованого веб-сервера та запуску цієї веб-програми Flask