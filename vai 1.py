from flask import Flask, render_template_string
app = Flask(__name__)
@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Delicious desserts for every occasion. Find recipes, buy treats, and explore our blog.">
        <title>Sweet Treats Bakery</title>
        <style>
            /* Basic Reset */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            /* Body and Font Styling */
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                background-color: #f5f5f5;
                color: #333;
            }

            /* Header and Navigation */
            header {
                background-color: #ff6f61;
                padding: 1rem;
            }

            nav ul {
                list-style: none;
                display: flex;
                justify-content: center;
            }

            nav ul li {
                margin: 0 20px;
            }

            nav ul li a {
                text-decoration: none;
                color: white;
                font-weight: bold;
            }

            /* Hero Section */
            .hero-banner {
                background: url('https://via.placeholder.com/1500x600.png?text=Dessert+Banner') no-repeat center center/cover;
                text-align: center;
                padding: 100px 20px;
                color: white;
            }

            .hero-banner h1 {
                font-size: 3rem;
                margin-bottom: 20px;
            }

            .hero-banner p {
                font-size: 1.2rem;
                margin-bottom: 30px;
            }

            .cta-button {
                background-color: #ffcc00;
                color: #333;
                padding: 10px 20px;
                text-decoration: none;
                font-weight: bold;
                border-radius: 5px;
            }

            /* Gallery */
            .gallery {
                display: flex;
                justify-content: space-around;
                margin: 40px 0;
            }

            .gallery .item {
                text-align: center;
                width: 30%;
            }

            .gallery .item img {
                width: 100%;
                border-radius: 10px;
            }

            /* Blog Posts */
            .blog-posts {
                display: flex;
                justify-content: space-around;
                margin: 40px 0;
            }

            .blog-posts .post {
                width: 45%;
                margin: 20px 0;
            }

            .blog-posts .post h3 {
                margin-bottom: 10px;
            }

            .blog-posts .post p {
                color: #555;
            }

            /* Contact Form */
            form {
                display: flex;
                flex-direction: column;
                max-width: 600px;
                margin: 40px auto;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            form input,
            form textarea {
                margin-bottom: 15px;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }

            form button {
                background-color: #ff6f61;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                cursor: pointer;
            }

            form button:hover {
                background-color: #ff3f2e;
            }

            /* Footer */
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 20px;
                margin-top: 40px;
            }
        </style>
    </head>
    <body>

        <!-- Header -->
        <header>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#recipes">Recipes</a></li>
                    <li><a href="#shop">Shop</a></li>
                    <li><a href="#blog">Blog</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </header>

        <!-- Main Section (Hero Banner) -->
        <section id="home">
            <div class="hero-banner">
                <h1>Welcome to Sweet Treats!</h1>
                <p>Your go-to place for the most delicious desserts</p>
                <a href="#shop" class="cta-button">Shop Now</a>
            </div>
        </section>

        <!-- Dessert Gallery -->
        <section id="recipes">
            <h2>Our Delicious Desserts</h2>
            <div class="gallery">
                <div class="item">
                    <img src="https://via.placeholder.com/300x200.png?text=Chocolate+Cake" alt="Chocolate Cake">
                    <h3>Chocolate Cake</h3>
                    <p>Delicious, rich chocolate cake topped with creamy frosting.</p>
                </div>
                <div class="item">
                    <img src="https://via.placeholder.com/300x200.png?text=Sugar+Cookies" alt="Sugar Cookies">
                    <h3>Sugar Cookies</h3>
                    <p>Soft, buttery cookies with a sweet, delicate flavor.</p>
                </div>
                <div class="item">
                    <img src="https://via.placeholder.com/300x200.png?text=Cupcakes" alt="Cupcakes">
                    <h3>Vanilla Cupcakes</h3>
                    <p>Light, fluffy cupcakes with a smooth vanilla frosting.</p>
                </div>
            </div>
        </section>

        <!-- Blog Section -->
        <section id="blog">
            <h2>Latest Blog Posts</h2>
            <div class="blog-posts">
                <div class="post">
                    <h3>How to Make Perfect Chocolate Chip Cookies</h3>
                    <p>Learn the secret to baking soft, chewy chocolate chip cookies every time!</p>
                </div>
                <div class="post">
                    <h3>Seasonal Desserts You Need to Try</h3>
                    <p>From pumpkin pies to gingerbread, check out these must-try seasonal treats!</p>
                </div>
            </div>
        </section>

        <!-- Contact Form -->
        <section id="contact">
            <h2>Get In Touch</h2>
            <form action="#" method="POST">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <textarea placeholder="Your Message" required></textarea>
                <button type="submit">Send Message</button>
            </form>
        </section>

        <!-- Footer -->
        <footer>
            <p>&copy; 2025 Sweet Treats Bakery</p>
        </footer>

        <script>
            // Optional JavaScript (for interactivity, like scroll-to-top button or form validation)
            window.onscroll = function() {
                const scrollButton = document.getElementById('scrollToTop');
                if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
                    scrollButton.style.display = 'block';
                } else {
                    scrollButton.style.display = 'none';
                }
            };

            function scrollToTop() {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        </script>

    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)

