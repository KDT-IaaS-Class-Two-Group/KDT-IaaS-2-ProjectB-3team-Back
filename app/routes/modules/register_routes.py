# Flask 앱에 여러 블루프린트를 등록하는 함수
register_routes = lambda app, *blueprints: [app.register_blueprint(bp) for bp in blueprints]