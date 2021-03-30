from flask import Blueprint, render_template, request
from myapp.utils import main_funcs
from myapp.models.user_model import User

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")  # index page


@bp.route("/compare", methods=["GET", "POST"])
def compare_index():
    """
    users 에 유저들을 담아 넘겨주세요. 각 유저 항목은 다음과 같은 딕셔너리
    형태로 넘겨주셔야 합니다.
     -  {
            "id" : "유저의 아이디 값이 담긴 숫자",
            "username" : "유저의 유저이름 (username) 이 담긴 문자열"
        }
    prediction 은 다음과 같은 딕셔너리 형태로 넘겨주셔야 합니다:
     -   {
             "result" : "예측 결과를 담은 문자열입니다",
             "compare_text" : "사용자가 넘겨준 비교 문장을 담은 문자열입니다"
         }
    """
    users = None
    prediction = None

    q_users = User.query.all()

    if q_users is None:
        return render_template("compare_user.html", users=users, prediction=prediction)
    users = []
    for user in q_users:
        users.append({"id": user.id, "username": user.username})

    if request.method == "POST":
        user_1_id = request.form.get("user_1")  # form data 에서 name으로 지정된게 key
        user_2_id = request.form.get("user_2")
        compare_text = request.form.get("compare_text")
        # 전부다 text로 넘어옴, type이 지정되 있음
        print(user_1_id, user_2_id, compare_text)

        user_list = [
            User.query.filter(User.id == int(user_1_id)).one_or_none(),
            User.query.filter(User.id == int(user_2_id)).one_or_none(),
        ]
        print(user_list)
        result = main_funcs.predict_text(user_list, compare_text)
        prediction = {"result": result, "compare_text": compare_text}
        # 여기서 post인 경우 넘어오는 json을 받아서
        # POST 일 경우에 필요한 코드를 작성해 주세요

    return render_template("compare_user.html", users=users, prediction=prediction)


@bp.route("/user")
def user_index():
    """
    user_list 에 유저들을 담아 템플렛 파일에 넘겨주세요
    """

    msg_code = request.args.get("msg_code", None)

    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None
    # /user 앤드 포인트에서 ADD 버튼과 delet 버튼에 request 세팅이 되어있고
    # 해당 버튼으로 request가 들어가면 user_route에 있는 함수가 실행된 후
    # redirect로 여기로 돌아와서
    # user.html에 다시 랜더링 해줌
    user_list = User.query.all()

    return render_template("user.html", alert_msg=alert_msg, user_list=user_list)
