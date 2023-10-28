#!/usr/bin/env python3
from server.database import SessionLocal
from server.models import User, Recipe, Rating, Favourite, Comment

if __name__ == "__main__":
    session = SessionLocal()

    session.query(User).delete()
    session.query(Recipe).delete()
    session.query(Rating).delete()
    session.query(Favourite).delete()
    session.query(Comment).delete()

    users = [
        User(
            first_name="John",
            last_name="Maluki",
            username="john-maluki",
            email="john@test.com",
            profile_photo="https://media.istockphoto.com/id/1477514412/photo/black-woman-facial-profile-and-beauty-in-studio-isolated-white-background-and-mockup-female.webp?b=1&s=170667a&w=0&k=20&c=5VSnoJBGP-Strmklde3JX9lOdbyRdRECfVQ-sXRcllw=",
            country="Kenya",
            phone_number="0700000000",
            password="john@123",
        )
    ]
    for user in users:
        session.add(user)
    session.commit()

    recipes = [
        Recipe(
            name="Ugali",
            recipe_image="https://netstorage-tuko.akamaized.net/images/9019461c20257dd3.jpg?imwidth=720",
            ingredients="Maize flour,Water",
            procedure="Boil water in a deep pan or a sufuria until it boils.\nAdd the maize meal and keep on stirring with a strong wooden spoon.\nKeep stirring and pressing the mixture against the sides of the pan to break up the lumps.\nKeep adding the flour as you continue mixing.\nCook until it is firm enough. The ugali should not be too hard or too soft.\nAllow it to cook for 2-3 minutes.\nTurn the ugali over onto a plate and serve.",
            number_of_people_served=3,
            time_in_minutes=5,
            country="Kenya",
            user_id=1,
        )
    ]

    for recipe in recipes:
        session.add(recipe)
    session.commit()

    comments = [Comment(comment="Its good looking and sweet", user_id=1, recipe_id=1)]
    for comment in comments:
        session.add(comment)
    session.commit()

    ratings = [Rating(rating=3, user_id=1, recipe_id=1)]
    for rating in ratings:
        session.add(rating)
    session.commit()

    favourites = [Favourite(user_id=1, recipe_id=1)]
    for favourite in favourites:
        session.add(favourite)
    session.commit()
