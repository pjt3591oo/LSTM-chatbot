# 심플챗봇

해당 프로젝트는 LSTM을 이용한 간단한 챗봇입니다.

# 프로젝트 구조

* convert.py
* botengine.py
* create_models.py
* slack.py


* `convert.py`

해당 파일은 카카오톡 대화내용을 이용하여 챗팅 훈련에 필요한 데이터로 만들어 줍니다. 한 유저가 끊어서 채팅 한 경우 하나의 문장으로 만들어 줍니다.

카카오 파일은 kakao.csv로 같은 디렉터리에 넣어주면 됩니다.

해당 파일을 실행하면 `converted.txt` 파일 생성



* `create_model.py`

convert.py로 생성된 converted.txt를 LSTM을 이용하여 훈련 후 모델을 만든다.

훈련결과를 `mnist_mlp_model.h5`의 파일로 만든다.


* `slack.py`

슬랙 봇 메인 프로그램

```python
slack_token = '슬랙토큰'
channel = '#채널명'
```

해당 팀에 맞는 토큰과 채널을 넣어주면 됨.  