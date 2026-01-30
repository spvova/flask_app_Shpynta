from app import create_app
from app.posts.models import Post

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)