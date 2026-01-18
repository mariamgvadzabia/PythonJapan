from ext import db, app
from models import User, Product

with app.app_context():
    db.drop_all()
    db.create_all()

    admin_user = User(username="mariam", password="password123", birthday="2000-01-01", role="admin")
    db.session.add(admin_user)


    p1 = Product(name="Tokyo", category="place",
                 subtitle="A sleepless metropolis where neon skyscrapers rise above ancient shrines", img="tokyo.jpg")
    p2 = Product(name="Yokohama", category="place",
                 subtitle="A dazzling harbor city blending futuristic skylines with historic charm.",
                 img="yokohama.jpg")
    p3 = Product(name="Nara", category="place",
                 subtitle="Japan's ancient capital, where sacred deer wander freely among the temples.", img="nara.jpg")
    p4 = Product(name="Osaka", category="place",
                 subtitle="The kitchen of Japan, famous for its vibrant street food and neon nightlife.",
                 img="osaka.jpg")

    p5 = Product(name="Miyagi", category="place",
                 subtitle="Home to Matsushima Bay, known as one of Japan's three most scenic views.", img="miyagi.jpg")
    p6 = Product(name="Yamaguchi", category="place",
                 subtitle="Breathtaking red torii gates stretching down the cliffs toward the deep blue sea.",
                 img="yamaguchi.jpg")
    p7 = Product(name="Nagasaki", category="place",
                 subtitle="A beautiful harbor city where Eastern traditions and Western history uniquely blend.",
                 img="nagasaki.jpg")
    p8 = Product(name="Aomori", category="place",
                 subtitle="The snowy northern land, famous for its massive colorful lantern festivals.",
                 img="aomori.jpg")

    db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
    db.session.commit()