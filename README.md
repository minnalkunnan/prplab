Minnal Kunnan
Cody Thompson
Lab 2

Task 1 Padding
Look in 'pad.py'

Task 2 ECB
A: Look in 'ecb.py'
B: Run task2B in 'ecb.py' (Ensure a file Lab2.TaskII.B.txt exists. The second one given to us was not included due to the size.)

C: Cookies v
For EBC Mode
0. Run Server
1. Run cookiecrack.py (Registers and logs in a user. The username will be one that fills the second and third blocks with "admin" and correct ANSI padding)
2. View the cookie. The repeating portion (blocks 2 and 3) will be the portion we need.
3. Register a user with username length of 15 (adminadminadmin) (to ensure the end "user" in "role=user" is in its own block)
4. Log in with the new user
5. Replace the last 32 characters of the auth_token with the repeating portion found above (block 2 or 3)
6. Deal with it

Task 3 CBC
A: Look in 'cbc.py'

B: Cookies v
For CBC Mode (in seperate CBC-Cookies folder)
0. Run Server
1. Register user 'aaaaaaaaaaaa' (12 'a's)
2. Login with user 'aaaaaaaaaaaa' (12 'a's). Note the cookie
3. Open cbcCookieCrack.py and change the task3B(x) function call to use x = the cookie you just got
4. Run cbcCookieCrack.py and note the new cookie
5. Replace the old cookie with the new cookie in the browser
6. Deal with it
