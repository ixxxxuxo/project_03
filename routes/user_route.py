from flask import Blueprint, request, redirect, url_for, Response
from myapp.services import tweepy_api, emotion_predictor
from myapp.models import user_model, tweet_model

bp = Blueprint('user', __name__)


@bp.route('/user', methods=['POST'])
def add_user():
    """
    add_user 함수는 JSON 형식으로 전달되는 폼 데이터로 유저를 트위터에서 조회한 뒤에
    해당 유저와 해당 유저의 트윗들을 벡터화한 값을 데이터베이스에 저장합니다.

    요구사항:
      - HTTP Method: `POST`
      - Endpoint: `api/user`
      - 받는 JSON 데이터 형식 예시:
            ```json
            {
                "username":"업데이트할 유저의 username",
                "new_username":"새로 업데이트할 username"
            }
            ```

    상황별 요구사항:
      - 주어진 데이터에 `username` 키가 없는 경우:
        - 리턴값: "Needs username"
        - HTTP 상태코드: `400`
      - 주어진 데이터의 `username` 에 해당하는 유저가 트위터에 존재하지 않은 경우:
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `400`
     - 주어진 데이터의 `username` 을 가지고 있는 데이터가 이미 데이터베이스에 존재하는 경우:
        - 해당 유저의 트윗 값들을 업데이트 합니다.
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `200`
      - 정상적으로 주어진 `username` 을 트위터에서 가져오고 해당 유저의 트윗 또한 가져화 벡터화해서 데이터베이스에 기록한 경우:
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `200`
    """

    # tweepy 파일에서 함수를 불러옴 
    # tweepy_api.get_tweets(screen_name)
    
    # 다양하게 구현 가능

    # 구현 방법 1) for 문을 돌려서 tweets 하나마다 데이터베이스 추가

      # 편리함 -> 각 트윗마다 그대로 임베딩 서버로 보낼 수 있다.
      # 100개의 트윗 => 100개의 for문 => 100개의 임베딩

    # 구현 방법 2) 요청 한개로 따로 텍스트 리스트를 모아서 보낼 것인지 
    user_add = request.get_json()
    if not user_add:
      return "Needs username", 400
    elif 
    return redirect(url_for('main.user_index', msg_code=0), code=200)


@bp.route('/user/')
@bp.route('/user/<int:user_id>', methods=['GET'])
def delete_user(user_id=None):
    """
    delete_user 함수는 `user_id` 를 엔드포인트 값으로 넘겨주면 해당 아이디 값을 가진 유저를 데이터베이스에서 제거해야 합니다.

    요구사항:
      - HTTP Method: `GET`
      - Endpoint: `api/user/<user_id>`

    상황별 요구사항:
      -  `user_id` 값이 주어지지 않은 경우:
        - 리턴값: 없음
        - HTTP 상태코드: `400`
      - `user_id` 가 주어졌지만 해당되는 유저가 데이터베이스에 없는 경우:
        - 리턴값: 없음
        - HTTP 상태코드: `404`
      - 주어진 `username` 값을 가진 유저를 정상적으로 데이터베이스에서 삭제한 경우:
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `200`
    """
    user_id = request.args.get('user.id')
    if not user_id:
      return None, 400
    
    return redirect(url_for('main.user_index', msg_code=3), code=200)
