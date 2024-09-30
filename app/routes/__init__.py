from ..utils.generator.bp_generator import generate_blueprint

generate_blueprint("main").add_url_rule('/', view_func=lambda: "<h1>ㅎ_ㅇ</h1>")
