from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from ..models import Comment

class CommentRepository:
    def create_comment(db: Session, recipe_id: int, comment: str, user_id: int):
        new_comment = Comment(recipe_id=recipe_id, comment=comment, user_id=user_id)
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return new_comment
    
    def get_comment_by_id(comment_id: int, db: Session):
        return db.query(Comment).filter(Comment.id == comment_id).first()
    
    def delete_comment(comment_id: int, db: Session):
        comment = CommentRepository.get_comment_by_id(comment_id, db)
        if comment:
            db.delete(comment)
            db.commit()