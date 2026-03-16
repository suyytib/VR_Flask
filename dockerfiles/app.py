from flask import Flask
from flask import render_template  
from blueprints.root import bp as root_bp  
    
app = Flask(__name__)  
app.register_blueprint(root_bp)      

@app.route('/')  
def rot():  
    return render_template("root.html")  
if __name__ == '__main__':  
    # 运行 Flask 应用程序，如果 debug=True，则应用程序将在调试模式下运行，并自动重新加载代码更改  
    app.run(host='0.0.0.0',port=5002,debug=True)