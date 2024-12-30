from app import db, Article, Comments, app  # Імпортуйте ваш додаток Flask

# Створіть контекст додатку
with app.app_context():
    # Видаліть всі записи в таблиці Article
    db.session.query(Article).delete()
    db.session.query(Comments).delete()

    # Застосуйте зміни
    db.session.commit()
    print("База даних очищена.")
