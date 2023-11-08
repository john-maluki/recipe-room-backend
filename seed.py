#!/usr/bin/env python3
from server.database import SessionLocal
from server.models import User, Recipe, Rating, Favourite, Comment
from server.hashing import Hash

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
            username="john@test.com",
            email="john@test.com",
            profile_photo="https://media.istockphoto.com/id/1477514412/photo/black-woman-facial-profile-and-beauty-in-studio-isolated-white-background-and-mockup-female.webp?b=1&s=170667a&w=0&k=20&c=5VSnoJBGP-Strmklde3JX9lOdbyRdRECfVQ-sXRcllw=",
            country="Kenya",
            phone_number="0700000000",
            password=Hash.bcrypt("john@123"),
        ),
        User(
            first_name="Ubah",
            last_name="Feisal",
            username="ubah@test.com",
            email="ubah@test.com",
            profile_photo="https://i.pinimg.com/564x/a7/75/c6/a775c6c41b8c6dad99755ba3c73da8d8.jpg",
            country="Kenya",
            phone_number="07222222",
            password=Hash.bcrypt("ubah@123"),
        ),
        User(
            first_name="Kiare",
            last_name="Collin",
            username="Kiare@test.com",
            email="Kiare@test.com",
            profile_photo="https://i.pinimg.com/564x/5e/a8/56/5ea856111da343eab5b148576430a109.jpg",
            country="Kenya",
            phone_number="072555555",
            password=Hash.bcrypt("kiare@123"),
        ),
        User(
            first_name="Ismail",
            last_name="Hussein",
            username="Hussein@test.com",
            email="Hussein@test.com",
            profile_photo="https://i.pinimg.com/236x/1b/16/3d/1b163d04c45ebf073ffe2c647ad95fa2.jpg",
            country="Kenya",
            phone_number="072888888",
            password=Hash.bcrypt("Hussein@123"),
        ),
        User(
            first_name="Philip",
            last_name="philip",
            username="philip@test.com",
            email="philip@test.com",
            profile_photo="https://i.pinimg.com/236x/ba/0c/57/ba0c57f0f9cb4083b1eab7f8e0a61cb1.jpg",
            country="Kenya",
            phone_number="072854545",
            password=Hash.bcrypt("philip@123"),
        ),
    ]
    for user in users:
        session.add(user)
    session.commit()

    recipes = [
        Recipe(
            name="Ugali",
            recipe_image="https://netstorage-tuko.akamaized.net/images/9019461c20257dd3.jpg?imwidth=720",
            ingredients="Maize flour\nWater",
            procedure="Boil water in a deep pan or a sufuria until it boils.\nAdd the maize meal and keep on stirring with a strong wooden spoon.\nKeep stirring and pressing the mixture against the sides of the pan to break up the lumps.\nKeep adding the flour as you continue mixing.\nCook until it is firm enough. The ugali should not be too hard or too soft.\nAllow it to cook for 2-3 minutes.\nTurn the ugali over onto a plate and serve.",
            number_of_people_served=3,
            time_in_minutes=5,
            country="Kenya",
            user_id=1,
        ),
        Recipe(
            name="Roasted Cherry Tomato Soup",
            recipe_image="https://www.allrecipes.com/thmb/NoZUw2HlyWe0FO5dBi5wnhicOLc=/0x512/filters:no_upscale():max_bytes(150000):strip_icc()/8350397_Roasted-Cherry-Tomato-Soup_TheDailyGourmet_4x3-e8efa4677d074c28b1fc5a381604a944.jpg",
            ingredients="20 ounces cherry tomatoes\n3 cloves garlic, peeled\n1 carrot, peeled and cut into 1/4-inch thick sticks\n1/2 onion, peeled\n1 red bell pepper, seeded and cut into strips\n2 tablespoons olive oil\n1/2 teaspoon salt\n1 teaspoon Italian seasoning\n1/4 cup water\n1/2 cup cream\nbasil leaves for garnish\nthyme sprigs for garnish\ncrushed red pepper flakes for garnish (optional",
            procedure="Preheat the oven to 425 degrees F (220 degrees C). Line a sheet pan with foil.\nSpread vegetables out on the prepared pan. Drizzle with olive oil; toss to coat. Sprinkle salt and Italian seasoning evenly over vegetables.\nRoast vegetables in the preheated oven for 20 minutes.\nFill a high powered blender (such as a Vitamix) halfway with roasted vegetables and any accumulated juices. Cover and hold lid down with a potholder; pulse a few times before leaving on to blend, about 45 seconds. Pour into a saucepan. Repeat with remaining roasted vegetables.\nPour water into the soup; add cream. Stir to combine and cook until heated through, about 3 minutes. Taste and adjust seasonings.\nLadle into soup bowls. Garnish with basil and thyme, and sprinkle with crushed red pepper flakes if desired. Serve immediately.",
            number_of_people_served=4,
            time_in_minutes=30,
            country="Kenya",
            user_id=2,
        ),
        Recipe(
            name="Pecan Chicken Salad",
            recipe_image="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F8223825.jpg&q=60&c=sc&orient=true&poi=auto&h=512",
            ingredients="½ cup mayonnaise\n½ cup plain Greek yogurt\n2 teaspoons white wine vinegar\n½ teaspoon garlic powder\n¼ teaspoon dried thyme\n1/2 teaspoon Park Hill maple pepper (such as Savory Spice Shop)\n2 cups chopped cooked chicken\n2 stalks celery, sliced\n⅓ cup chopped toasted pecans\n2 tablespoons minced red onion",
            procedure="Mix mayonnaise, Greek yogurt, vinegar, garlic powder, thyme, and maple pepper together in a bowl until well combined. Add chicken, celery, pecans, and red onion; stir well to incorporate.\nServe immediately or refrigerate for up to 3 days",
            number_of_people_served=4,
            time_in_minutes=20,
            country="international",
            user_id=3,
        ),
        Recipe(
            name="One pot Matoke/Plantain",
            recipe_image="https://allkenyanrecipescom.files.wordpress.com/2017/06/matoke-with-bread.jpg?w=2000&h=",
            ingredients="6 Matoke\n250g beef, cut into bite sizes\n250g beef, cut into bite sizes\n3 medium potatoes, peeled, washed and cut in quarters\n2 medium carrots, washed, peeled and cut in into sticks\n2 spring onions, chopped\n3 medium tomatoes, diced\n4 garlic cloves, minced\n1 teaspoon tomato paste\n1 teaspoon salt\n4 tablespoons vegetable oil\n1 glass of water\na bunch of fresh coriander for garnishing\na piece of bread to go with (optional)",
            procedure="Start by filling a big pot with water enough to cover the plantains and bringing it to a boil. Place the plantains in the boiling water and boil for 10 minutes. Remove from heat and set aside to cool off. Once cooled, peel of the skin and set aside\nIn a saucepan place beef, bone marrow, garlic and the glass of water and boil on medium heat for 20 minutes\nSeparate meat from broth and set aside (you’ll need the broth later)\nIn the same saucepan, heat up oil on medium heat, add onions and fry till soft and translucence. Add beef and fry till it starts to brown. Add tomatoes and tomato paste and cook until the fresh tomatoes have softened\nAdd carrots and potatoes and stir the mixture well. Let it simmer on low heat for about 5 minutes stirring in between to avoid it from burning\nAdd the broth you had set aside earlier and stir in salt to taste. Let it boil for a minute or two. Place Matoke / Plantain (you can leave them whole or cut them in half or as you desire) in the boiling broth, lower the heat to low and simmer the mixture for about 30-45 minutes or until Matoke / Plantain are done. Gently stir in between to avoid it from sticking at the bottom of the pan but also be careful not to break the Matoke / Plantain\nGarnish with fresh coriander and serve hot with a piece of bread on the side.",
            number_of_people_served=4,
            time_in_minutes=20,
            country="Kenya",
            user_id=4,
        ),
        Recipe(
            name="Mahamri",
            recipe_image="https://allkenyanrecipescom.files.wordpress.com/2013/10/mahamri.jpg",
            ingredients="3 cups of flour\n8 -10 tablespoons of brown sugar (depending on how sweet you wish your Mahamris to be)\n1 teaspoon of instant yeast\n1 teaspoon of cardamom\n1 teaspoon of ghee, butter or margarine\n1 medium Egg – (optional)\ncup of coconut milk for kneading the dough\nVegetable oil for deep frying.",
            procedure="In a mixing bowl add flour, sugar, yeast and cardamom, ghee/butter/margarine and the egg. Mix the ingredients together with either clean hands or a mixture. Slowly add coconut milk little at a time, as you knead the dough\nIf you are using your hands to knead the dough, knead it for a minimum of 15-20 minutes until it’s soft, smooth and not sticky in either your hands or the walls of your bowl Place the dough in a container and cover it with either a lid or a clean cloth. Let it rest and rise for at least    3-4 hours in room temperature. I normally leave mine overnight! The dough should double in size\nUsing a dough cutter or a knife, divide the dough into 4-5 equal balls. Coat each ball of dough with flour, cover them again with a clean cloth for 15 minutes and let them puff/rise\nSprinkle some flour on a clean surface and using a rolling pin, roll each ball of dough into a circle of about 6 inches. Move with the dough and if needed use more flour to prevent the dough from sticking on the surface and on the rolling pin\nCut each rolled dough into 4pieces\nHeat up the vegetable oil in a frying pan on a wok\nTest your oil by gently dropping a small piece of dough into the oil. If the dough stays at the bottom for a couple of seconds then rises to the surface then your oil is ready for frying but if it rises up immediately after dropping it into the oil, then your oil is too hot and you need to reduce the heat otherwise your mahamris will burn and end up not been cooked inside\nFry 4 mahamri at a time (depending on the size of your pan or wok). Use your strainer to splash oil over the top of the mahamris in order to help them puff up. As soon as you see the bottom side of the mahamris has turned light-gold brown turn them over\nKeep turning the mahamris until they have a nice golden brown colour on both sides. Remove them from the hot oil and place them in a serving plate lined with paper towels to absorb any excess oil\nRepeat this process until all the dough pieces have been fried\nAllow them to cool for a few minutes and enjoy!!\nServe for breakfast with pigeon peas cooked in coconut milk and or with a cup of typical Kenyan Chai",
            number_of_people_served=6,
            time_in_minutes=60,
            country="Kenya",
            user_id=1,
        ),
        Recipe(
            name="Pilau",
            recipe_image="https://allkenyanrecipescom.files.wordpress.com/2013/06/beef-pilau.jpg",
            ingredients="1/2 kg Basmati rice, washed (for better results I highly recommend Basmati reis)\n1/2 kg potatoes – peeled, washed and coarsely chopped\n1/2 kg beef, chicken or fish filet – cubed\n1 small cup sunflower oil (or any other liquid oil)\n4 cups of hot water or broth\n1 onion, chopped\n5 cloves of Garlic, crushed\n1 fresh Ginger, crushed\n2 fresh Tomatoes , sliced\n2-3 teaspoon Pilau spices\nSalt and pepper to taste",
            procedure="Boil beef or chicken with ginger for 10 minutes. Add potatoes and let them boil for 5 minutes then set aside (separate the cooked ingredients from the broth so you can use it later)\nHeat oil and fry onions till light brown, add garlic and Pilau spices and on a low heat, fry for 1 minute\nAdd tomatoes meat/chicken with potatoes and cook till tender\nAdd rice and ensure to mix everything very well before adding your broth or hot water then stir the mixture very well\nAdd salt and pepper to taste then cover the pot and cook on medium heat\nWhen the Food is nearly dry, lower down the heat to very low, cover your Pilau with aluminium paper (please avoid newspapers or polythene papers) and place the lid on top. Leave to cook for 10 minutes.\nServe your Pilau hot with Kachumbari and Pilipili ya Maembe",
            number_of_people_served=4,
            time_in_minutes=20,
            country="international",
            user_id=5,
        ),
        Recipe(
            name="Buttermilk Pumpkin Pancakes",
            recipe_image="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F7544835.jpg&q=60&c=sc&orient=true&poi=auto&h=512",
            ingredients="1 cup all-purpose flour\n2 tablespoons white sugar\n1 tablespoon pumpkin pie spice\n1 teaspoon baking powder\n1 teaspoon baking soda\n½ teaspoon salt\n1 cup buttermilk\n½ cup canned pumpkin\n¼ cup canola oil\n2 large eggs\n1 teaspoon vanilla extract\n1 serving nonstick cooking spray",
            procedure="Whisk flour, sugar, pumpkin pie spice, baking powder, baking soda, and salt together in a large bowl. Whisk in buttermilk, pumpkin, oil, eggs, and vanilla extract until well blended.\nSpray a large nonstick griddle or skillet with cooking spray. Heat over medium heat.\nPour batter by scant 1/3 cupfuls into the hot skillet, working in batches. Cook until bubbles form on the surface of pancakes and bottoms are lightly browned, about 1 1/2 minutes per side. Repeat with remaining batter, spraying the skillet with cooking spray between batches as needed. Serve warm.",
            number_of_people_served=8,
            time_in_minutes=15,
            country="International",
            user_id=4,
        ),
        Recipe(
            name="Waffle House-Style Waffles",
            recipe_image="https://www.allrecipes.com/thmb/aRaAaSmn6NFZxc9-x_jpYU7FhKw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/8534837-Waffle-House-Style-Waffles-4x3-1-a17b741844894e079cfcd388c21c3749.jpg",
            ingredients="1 ½ cups flour\n2 tablespoons cornstarch\n1 teaspoon salt\n½ teaspoon baking powder\n½ teaspoon baking soda\n1 large egg\n¼ cup sugar\n¼ cup salted butter, softened, plus more for serving\n1 teaspoon vanilla extract\n1 cup half-and-half\n½ cup buttermilk\ncooking spray\n\npure maple syrup, and/or chocolate chips, for serving",
            procedure="Whisk together flour, cornstarch, salt, baking powder, and baking soda in a bowl.\nWhisk together egg, sugar, butter, and vanilla in a separate large bowl until mixture is smooth. Whisk in half-and-half and buttermilk. Add flour mixture; stir until just combined and a few lumps remain. (Do not overmix.) Chill, covered, at least 1 hour or up to overnight.\nPreheat waffle iron to medium-high; lightly coat with cooking spray. Pour about 2/3 cup batter onto waffle iron. Cook until golden and crisp on edges, 4 to 6 minutes. Transfer to a plate; keep warm. Repeat with remaining batter.\nServe waffles with maple syrup, chocolate chips, and/or additional butter.",
            number_of_people_served=4,
            time_in_minutes=95,
            country="international",
            user_id=3,
        ),
        Recipe(
            name="Arugula Salad with Stone Fruit",
            recipe_image="https://www.allrecipes.com/thmb/EC7FTg4V4z3ijZyHMVmdXTlkFaQ=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/7506181-arugula-salad-with-stone-fruit-GOLDMAN-4x3-5066-df2290fa4eaf49689258d9100e1170f4.jpg",
            ingredients="2 tablespoons extra-virgin olive oil\n2 tablespoons red wine vinegar or rosé vinegar\n3/4 teaspoon salt\n1/2 teaspoon black pepper\n1 1/2 cups red cherry tomatoes, halved\n1 1/2 cups yellow cherry tomatoes, halved\n1 (5-ounce package) arugula\n3/4 cup fresh basil leaves\n2 nectarines, sliced\n1 large white peach, sliced\n1 cup Rainier or other yellow-flesh cherries, pitted and halved\n1/2 teaspoon flaky sea salt",
            procedure="Whisk together olive oil, vinegar, salt, and pepper in a small bowl for the dressing.\nArrange tomatoes, arugula, basil, nectarines, and peach slices on a large platter. Drizzle with half the dressing. Top with cherries, sea salt, and remaining dressing. Serve immediately.",
            number_of_people_served=4,
            time_in_minutes=20,
            country="international",
            user_id=5,
        ),
        Recipe(
            name="Homemade Pita Bread",
            recipe_image="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fpublic-assets.meredithcorp.io%2Faa387860990c4668c1f1e320ac93fbaf%2F1657139429image.jpg&q=60&c=sc&orient=true&poi=auto&h=512",
            ingredients="1 (.25 ounce) package active dry yeast\n1 cup warm water (90 to 100 degrees F/32 to 38 degrees C)\n1 cup all-purpose flour\n1 ½ tablespoons olive oil\n1 ¾ teaspoons salt\n1 ¾ cups all-purpose flour, or more as needed\n1 teaspoon olive oil, divided",
            procedure="Place yeast in the bowl of a stand mixer and add 1 cup warm water and 1 cup flour. Whisk together, then let sit until mixture bubbles and foams, 15 to 20 minutes.\nAdd 1 1/2 tablespoons olive oil and salt into the yeast mixture, followed by 1 3/4 cups flour. Mix at low speed, using a dough hook attachment, until dough is soft, supple, and slightly sticky. If dough sticks to the sides of the bowl, add up to 1/4 cup more flour, a little at a time.\nKnead dough with machine on low speed until slightly springy and still soft, 5 to 6 minutes. Turn dough out onto a floured work surface and form into a ball.\nWipe inside of bowl with 1/4 teaspoon olive oil. Turn dough around in bowl to cover with a thin film of oil; cover bowl with foil and let sit until dough has doubled in size, about 2 hours.\nRemove dough from bowl and place onto a floured work surface. Lightly pat into a flat shape about 1-inch thick. Use a knife to cut dough into 8 equal pieces.\nForm each piece into a small round ball with a smooth top, pulling dough from the sides and tucking the ends underneath the bottom.\nover dough balls with lightly oiled plastic wrap and let rest for 30 minutes.\nTransfer the dough balls to a lightly floured work surface and sprinkle the tops with flour. One at a time, gently pat the dough with your fingers, forming a flat, round bread about 1/4-inch thick. Let the shaped dough rest for 5 minutes.\nBrush a cast iron skillet with remaining 3/4 teaspoon olive oil and place over medium-high heat. Lay dough into the hot skillet; cook until puffy and the bottom has brown spots and blisters, about 3 minutes. Flip, cook 2 more minutes, and flip back onto original side to cook for about 30 more seconds. Pita bread will begin to puff up and fill with hot air. Stack cooked breads on a plate; when cool enough to handle, slice breads in half and open the pocket inside for stuffing.",
            number_of_people_served=8,
            time_in_minutes=155,
            country="Kenya",
            user_id=2,
        ),
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
