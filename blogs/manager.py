import uuid
from .models import Blog

class BlogManager:    
    def __init__(self, db):
        self.blog_db = db
    
    def create_blog(self, title, content, author_id):
        
        blog = Blog(
            id=str(uuid.uuid4()),
            title=title,
            content=content,
            author_id=author_id
        )
        
        self.blog_db.session.add(blog)
        self.blog_db.session.commit()
        return blog

    def get_all_blogs(self):
        return Blog.query.all()

    def get_blog_by_id(self, blog_id):
        return Blog.query.get(blog_id)

    def update_blog(self, blog_id, new_data):
        blog = self.get_blog_by_id(blog_id)
        if blog:
            if 'title' in new_data:
                blog.title = new_data['title']
            if 'content' in new_data:
                blog.content = new_data['content']
            self.blog_db.session.commit()
            return blog
        return None

    def delete_blog(self, blog_id):
        blog = self.get_blog_by_id(blog_id)
        if blog:
            self.blog_db.session.delete(blog)
            self.blog_db.session.commit()
            return True
        return False
