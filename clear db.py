from app import db, Article, app  # Імпортуйте ваш додаток Flask

# Створіть контекст додатку
with app.app_context():
    # Видаліть всі записи в таблиці Article
    db.session.query(Article).delete()

    # Застосуйте зміни
    db.session.commit()
    print("База даних очищена.")
