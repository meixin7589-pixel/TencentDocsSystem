from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>腾讯文档同步系统</h1>

    <p>企业内部测试环境</p>

    <p>测试账号：</p>

    <p>test001</p>

    <p>密码：</p>

    <p>123456</p>

    <hr>

    <button onclick="alert('同步成功')">
    执行同步
    </button>
    """

if __name__ == "__main__":
    app.run()