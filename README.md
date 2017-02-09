Minnal Kunnan
Cody Thompson
Lab 2

For EBC Mode
0. Run Server
1. Run cookiecrack.py (Registers and logs in a user)
2. View the cookie. The repeating portion will be the portion we need.
3. Register a user with username length of 15 (adminadminadmin)
4. Log in with the new user
5. Replace the last 32 characters of the auth_token with the repeating portion found above
6. Deal with it

For CBC Mode (in seperate CBC-Cookies folder)
0. Run Server
1. Register user 'aaaaaaaaaaaa' (12 'a's)
2. Login with user 'aaaaaaaaaaaa' (12 'a's). Note the cookie
3. Open cbcCookieCrack.py and change the task3B(x) function call to use x = the cookie you just got
4. Run cbcCookieCrack.py and note the new cookie
5. Replace the old cookie with the new cookie in the browser
6. Deal with it