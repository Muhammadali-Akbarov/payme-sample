# Payme Implementation

Support Group - <a href="https://t.me/+bYouuOlqt1c3NmYy">Telegram</a><br>
YouTube - <a href="https://youtu.be/r2RO3kJVP7g"> Watch Video</a><br>
This MVP project helps to implement <a href="https://github.com/PayTechUz/payme-pkg">payme-pkg</a>.

<a href="https://youtu.be/r2RO3kJVP7g">
<img width="70%" src="https://i.postimg.cc/5NRRSHXp/homemuhammadali-Downloads-Telegram-Desktop-Closer-Li-QWYD-No-Copyright-Music-Audio-Library-Music-m4a.gif">
</a>

### API Endpoints <br>

Pay link is a simple interface that provides pay-link functionality.

- `/shop/pay-link/` POST: Get a pay link for pay each order.

### Merchant endpoint

- `/payments/merchant/` includes all merchant methods that tests on <a href="https://test.paycom.uz/">Payme Sandbox</a>

# Installation
* 1 - clone repo 
   - ```git clone https://github.com/PayTechUz/payme-sample.git```
* 2 - create a virtual environment and activate
  - ```pip3 install virtualenv```
  - ```virtualenv venv```
  - ```venv\Scripts\activate```(windows) or ```source venv/bin/activate```(unix-based systems)
* 3 - cd into project "cd payme-sample"
* 4 - Install dependencies
  - ```pip3 install -r requirements.txt```
* 5 - Set your environment variables
  - ```cp .env-sample .env```
* 6 - Run tests and app
  - ```python3 manage.py test```
  - ```python3 manage.py migrate```
  - ```python3 manage.py runserver```
