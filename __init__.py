from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)

    # if app.config["ENV"] == "production":
    #     app.config.from_object("config.ProductionConfig")
    # else:
    #     app.config.from_object("config.DevelopmentConfig")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.sqlte3"  # 연결 설정 해줘야함

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from myapp.routes import main_route, user_route

    app.register_blueprint(main_route.bp)
    app.register_blueprint(user_route.bp, url_prefix="/api")

    return app


# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True)
"""
app.config 에서 db를 알려줘야함
CLI 상에서 
1) export FLASK_APP=myapp.py 환경변수로 등록
2) flask run 바로 실행 가능
3) flask db init # migrations 생성
3) flask db migrate # db에 변경사항 있으면 commit
4) flask db upgrade # db에 push 하는 개념
"""