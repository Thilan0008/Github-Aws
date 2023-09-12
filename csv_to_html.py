import csv
from flask import Flask
from flask import send_file



app = Flask(__name__)

@app.route('/')
def index():
    return send_file('templates/output.html')


app = Flask(__name__)

def csv_to_html_table(csv_file, html_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)

    # Header code
    header_code = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">


      <!-- primary meta tag -->
      <title>EduWeb - The Best Program to Enroll for Exchange</title>
      <meta name="title" content="EduWeb - The Best Program to Enroll for Exchange">
      <meta name="description" content="This is an education html template made by codewithsadee">

      <!-- favicon -->
      <link rel="shortcut icon" href="./favicon.svg" type="image/svg+xml">

      <!-- custom css link -->
      <link rel="stylesheet" href="static/assets/css/style.css">



      <!-- google font link -->
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;500;600;700;800&family=Poppins:wght@400;500&display=swap" rel="stylesheet">

      <!-- preload images -->
      <link rel="preload" as="image" href="static/assets/images/hero-bg.svg">
      <link rel="preload" as="image" href="static/assets/images/hero-banner-1.jpg">
      <link rel="preload" as="image" href="static/assets/images/hero-banner-2.jpg">
      <link rel="preload" as="image" href="static/assets/images/hero-shape-1.svg">
      <link rel="preload" as="image" href="static/assets/images/hero-shape-2.png">
    </head>

    <body id="top" style="background-color: var(--isabelline);">

      <!-- #HEADER -->
      <header class="header" data-header>
        <div class="container">
          <a href="#" class="logo">
            <img src="static/assets/images/logo.svg" width="162" height="50" alt="EduWeb logo">
          </a>

          <nav class="navbar" data-navbar>
            <div class="wrapper">
              <a href="#" class="logo">
                <img src="static/assets/images/logo.svg" width="162" height="50" alt="EduWeb logo">
              </a>
              <button class="nav-close-btn" aria-label="close menu" data-nav-toggler>
                <ion-icon name="close-outline" aria-hidden="true"></ion-icon>
              </button>
            </div>

            <ul class="navbar-list">
              <li class="navbar-item">
                <a href="#home" class="navbar-link" data-nav-link>Home</a>
              </li>
              <li class="navbar-item">
                <a href="#about" class="navbar-link" data-nav-link>About</a>
              </li>
              <li class="navbar-item">
                <a href="#courses" class="navbar-link" data-nav-link>Courses</a>
              </li>
              <li class="navbar-item">
                <a href="#blog" class="navbar-link" data-nav-link>Blog</a>
              </li>
              <li class="navbar-item">
                <a href="#" class="navbar-link" data-nav-link>Contact</a>
              </li>
            </ul>
          </nav>

          <div class="header-actions">
            <button class="header-action-btn" aria-label="toggle search" title="Search">
              <ion-icon name="search-outline" aria-hidden="true"></ion-icon>
            </button>

            <a href="#" class="btn has-before">
              <span class="span">Try for free</span>
              <ion-icon name="arrow-forward-outline" aria-hidden="true"></ion-icon>
            </a>

            <button class="header-action-btn" aria-label="open menu" data-nav-toggler>
              <ion-icon name="menu-outline" aria-hidden="true"></ion-icon>
            </button>
          </div>

          <div class="overlay" data-nav-toggler data-overlay></div>
        </div>
         
      </header>


      <div class="container">
    '''
    table = header_code

    # Add navigation bar
    nav_bar = '''
    <nav style="margin-bottom: 50px;">
    
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          
        </ul>
        
    </nav>
    <nav style="margin-bottom: 50px;">
    <ul>
        <li>
            <h2 class="h2 section-title">Top 50 Coursera Courses!</h2>
        </li>
    </ul>
    </nav>

    '''
    table += nav_bar

    # Create table rows as cards
    cards = "<ul class='grid-list'>"
    for index, row in enumerate(rows):
        
        if len(row) >= 5:
            
            image_path = f"static/assets/images/{index + 1}.jpg"  # Assuming the image names are 1.jpg, 2.jpg, 3.jpg, and so on
            card = f'''
            <li>
                <div class='course-card'>
                <figure class='card-banner img-holder' style='--width: 370; --height: 220;'>
                    <img src='{image_path}' width='370' height='220' loading='lazy'
                        alt='Course Image' class='img-cover'>
                </figure>

                <div class='abs-badge'>
                    <ion-icon name='time-outline' aria-hidden='true'></ion-icon>
                    <span class='span'>Coursera</span>
                </div>

                <div class='card-content'>
                    <span class='badge'>{row[1]} Rating</span>

                <h3 class='h3'>
                        <a href='{row[4]}' class='card-title'>{row[0]}</a>
                </h3> 
                
                    <div class='wrapper'>
                        <div class='rating-wrapper'>
                            <ion-icon name='star'></ion-icon>
                            <ion-icon name='star'></ion-icon>
                            <ion-icon name='star'></ion-icon>
                            <ion-icon name='star'></ion-icon>
                            <ion-icon name='star'></ion-icon>
                        </div>

                        <p class='rating-text'></p>
                    </div>

                    <ul class='card-meta-list'>
                        <li class='card-meta-item'>
                            <ion-icon name='library-outline' aria-hidden='true'></ion-icon>
                            <span class='span'>{row[2]}</span>
                        </li>

                        <li class='card-meta-item'>
                            <ion-icon name='people-outline' aria-hidden='true'></ion-icon>
                            <span class='span'>{row[3]}</span>
                        </li>
                    </ul>
                </div>
              </div>
          </li>
        '''
        else:
            card = ""  # Define card as an empty string if condition is not met
    

        cards += card

        footer_code ='''
        
          <!-- 
    - #FOOTER
  -->

  <footer class="footer" style="background-image: url('static/assets/images/footer-bg.png')">

    <div class="footer-top section">
      <div class="container grid-list">

        <div class="footer-brand">

          <a href="#" class="logo">
            <img src="static/assets/images/logo-light.svg" width="162" height="50" alt="EduWeb logo">
          </a>

          <p class="footer-brand-text">
            Unlock the full potential of education with Edu-Con, your all-in-one content management solution. Seamlessly create, organize, and distribute educational materials for a dynamic learning experience.
          </p>

          <div class="wrapper">
            <span class="span">Add:</span>

            <address class="address">Edu-Con, Ingiriya Road, Padukka</address>
          </div>

          <div class="wrapper">
            <span class="span">Call:</span>

            <a href="tel:+0776534305" class="footer-link">+94 77 6534 305</a>
          </div>

          <div class="wrapper">
            <span class="span">Email:</span>

            <a href="mailto:educon721@gmail.com" class="footer-link">educon721@gmail.com</a>
          </div>

        </div>

        <ul class="footer-list">

          <li>
            <p class="footer-list-title">Online Platform</p>
          </li>

          <li>
            <a href="#" class="footer-link">About</a>
          </li>

          <li>
            <a href="#" class="footer-link">Courses</a>
          </li>

          <li>
            <a href="#" class="footer-link">Instructor</a>
          </li>

          <li>
            <a href="#" class="footer-link">Events</a>
          </li>

          <li>
            <a href="#" class="footer-link">Instructor Profile</a>
          </li>

          <li>
            <a href="#" class="footer-link">Purchase Guide</a>
          </li>

        </ul>

        <ul class="footer-list">

          <li>
            <p class="footer-list-title">Links</p>
          </li>

          <li>
            <a href="#" class="footer-link">Contact Us</a>
          </li>

          <li>
            <a href="#" class="footer-link">Gallery</a>
          </li>

          <li>
            <a href="#" class="footer-link">News & Articles</a>
          </li>

          <li>
            <a href="#" class="footer-link">FAQ's</a>
          </li>

          <li>
            <a href="#" class="footer-link">Sign In/Registration</a>
          </li>

          <li>
            <a href="#" class="footer-link">Coming Soon</a>
          </li>

        </ul>

        <div class="footer-list">

          <p class="footer-list-title">Contacts</p>

          <p class="footer-list-text">
            Enter your email address to register to our newsletter subscription
          </p>

          <form action="" class="newsletter-form">
            <input type="email" name="email_address" placeholder="Your email" required class="input-field">

            <button type="submit" class="btn has-before">
              <span class="span">Subscribe</span>

              <ion-icon name="arrow-forward-outline" aria-hidden="true"></ion-icon>
            </button>
          </form>

          <ul class="social-list">

            <li>
              <a href="#" class="social-link">
                <ion-icon name="logo-facebook"></ion-icon>
              </a>
            </li>

            <li>
              <a href="#" class="social-link">
                <ion-icon name="logo-linkedin"></ion-icon>
              </a>
            </li>

            <li>
              <a href="#" class="social-link">
                <ion-icon name="logo-instagram"></ion-icon>
              </a>
            </li>

            <li>
              <a href="#" class="social-link">
                <ion-icon name="logo-twitter"></ion-icon>
              </a>
            </li>

            <li>
              <a href="#" class="social-link">
                <ion-icon name="logo-youtube"></ion-icon>
              </a>
            </li>

          </ul>

        </div>

      </div>
    </div>

    <div class="footer-bottom">
      <div class="container">

        <p class="copyright">
          Copyright 2023 All Rights Reserved by <a href="#" class="copyright-link">Edu-Con</a>
        </p>

      </div>
    </div>

  </footer>
   
        '''

    cards += "</ul>"
    table += cards
    table += footer_code

    # Write the HTML table to a file
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(table)

@app.route('/')
def index():
    csv_file = 'top_courses.csv'
    html_file = 'output.html'
    
    
    csv_to_html_table(csv_file, html_file)
    
    return send_file(html_file)

if __name__ == '__main__':
    app.run()
