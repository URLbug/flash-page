from __init__ import app
import model
import blog

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)