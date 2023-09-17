# import the libraries

import undetected_chromedriver as uc
import time
import random
from fp.fp import FreeProxy
from selenium.common.exceptions import NoSuchElementException
from undetected_chromedriver.webelement import By

print("This bot is coded and developed by Mr.SAFEER ABBAS. \n https://safeerabbas624.github.io/safeerabbas/"
      "\n https://github.com/SafeerAbbas624")

print("""

 _______  _  _     _______         _      ____          _   
|__   __|(_)| |   |__   __|       | |    |  _ \        | |  
   | |    _ | | __   | |     ___  | | __ | |_) |  ___  | |_ 
   | |   | || |/ /   | |    / _ \ | |/ / |  _ <  / _ \ | __|
   | |   | ||   <    | |   | (_) ||   <  | |_) || (_) || |_ 
   |_|   |_||_|\_\   |_|    \___/ |_|\_\ |____/  \___/  \__|


""")


# Sleep function.
def sleep(sleep_min, sleep_max):
    time.sleep(random.uniform(sleep_min, sleep_max))


# Proxy from Free-Proxy library
PROXY = FreeProxy(timeout=1, https=True, ).get()
print(PROXY)

# Set Chrome Options
options = uc.ChromeOptions()
# options.add_argument(f'--proxy-server={PROXY}')

# Create Undetected Chromedriver with Proxy
driver = uc.Chrome(options=options)

# These username and passwords are the list of accounts already on TikTok, which will follow, like, view, and comment
# on username given. These can work good if in bulk. Try to arrange these in bulk.
usernames = [ # put usernames here

]
passwords = [ # Put passwords here
]
# username to be followed on TikTok
print("What is your username for TikTok?")
user_username = input()


# Make the TikTok follow function.
def tiktok_follow():
    # username and password loop
    for i in range(len(usernames)):

        driver.delete_all_cookies()
        # opening TikTok page
        driver.get("https://www.tiktok.com/login/phone-or-email/email")
        sleep(10, 20)
        # finding email or username input box
        user = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input')
        # Sending username or email keys
        user.click()
        for character in usernames[i]:
            user.send_keys(character)
            sleep(0.1, 0.2)

        time.sleep(5)
        # finding password input box
        passw = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input')
        # Sending password keys
        passw.click()
        for character in passwords[i]:
            passw.send_keys(character)
            sleep(0.1, 0.2)
        try:
            sleep(1, 3)
            # Clicking on Signin button
            signin = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button')
            signin.click()


        except NoSuchElementException as error:
            print(error)
            print('There is Maximum attempts reached. waiting for 6 mins and try again')
            time.sleep(360)
            signin = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button')
            signin.click()
            driver.implicitly_wait(20)
            sleep(3, 10)
        finally:
            sleep(3, 10)
            driver.implicitly_wait(20)
            # Put the user input's username in the search bar.
            search = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/input')
            search.click()
            for char in user_username:
                search.send_keys(char)
                sleep(0.1, 0.2)
            # Clicking search button
            search_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/button')
            search_btn.click()
            driver.implicitly_wait(20)
            sleep(5, 15)
            # clicking on accounts tab
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]').click()
            sleep(5, 15)

            # Compare the user input and top 10 search results. If they are the same, click on the user's profile.
            for line in range(1, 10):
                try:
                    search_results = driver.find_element(By.XPATH,
                                                         f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[{line}]/a['
                                                         f'2]/p[1]')
                    if search_results.text == user_username:
                        # Clicking on profile to go profile page
                        driver.find_element(By.XPATH,
                                            f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[{line}]').click()
                        sleep(5, 15)
                        break
                    else:
                        pass
                except:
                    # Printing output for unsuccessful
                    print(f"Could not find username: '{user_username}'.")

        # Clicking on Follow button
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/button').click()
        sleep(2, 3)
        driver.quit()
        sleep(5, 10)
    # Printing output for success.
    print(f"Followed {user_username}!")


# Make the Tiktok Like & Views function.
def tiktok_like_view():
    # username and password loop
    for i in range(len(usernames)):
        try:
            driver.delete_all_cookies()
            # opening TikTok page
            driver.get("https://www.tiktok.com/login/phone-or-email/email")
            sleep(10, 20)
            # finding email or username input box
            user = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input')
            # Sending username or email keys
            user.click()
            for character in usernames[i]:
                user.send_keys(character)
                sleep(0.1, 0.2)

            time.sleep(5)
            # finding password input box
            passw = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input')
            # Sending password keys
            passw.click()
            for character in passwords[i]:
                passw.send_keys(character)
                sleep(0.1, 0.2)

            sleep(1, 3)
            # Clicking on Signin button
            signin = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button')
            signin.click()
            driver.implicitly_wait(20)
            sleep(3, 10)
        except NoSuchElementException as error:
            print(error)
            print('There is Maximum attempts reached. waiting for 5 mins and try again')
            time.sleep(360)
            signin = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button')
            signin.click()
            driver.implicitly_wait(20)
            sleep(3, 10)
        finally:

            # Put the user input's username in the search bar.
            search = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/input')
            search.click()
            for char in user_username:
                search.send_keys(char)
                sleep(0.1, 0.2)
            # Clicking search button
            search_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/button')
            search_btn.click()
            driver.implicitly_wait(20)
            sleep(5, 15)
            # clicking on accounts tab
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]').click()
            sleep(5, 15)

            # Compare the user input and top 10 search results. If they are the same, click on the user's profile.
            for line in range(1, 10):
                try:
                    search_results = driver.find_element(By.XPATH,
                                                         f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[{line}]/a['
                                                         f'2]/p[1]')
                    if search_results.text == user_username:
                        # Clicking on profile to go profile page
                        driver.find_element(By.XPATH,
                                            f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[{line}]').click()
                        sleep(5, 15)
                        break
                    else:
                        pass
                except:
                    # Printing output for unsuccessful
                    print(f"Could not find username: '{user_username}'.")

        for vid in range(1, 10):
            # clicking on video to view
            driver.find_element(By.XPATH,
                                f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[{vid}]/div[1]/div/div/a/div').click()
            # waiting for 30 seconds to watch video
            time.sleep(30)

            # for heart/like click
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/div[1]/div[1]/button[1]/span').click()
            sleep(2, 5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div[1]/button[1]').click()
            sleep(2, 5)
        sleep(2, 3)
        driver.quit()
    print(f"Liked & Viewed {user_username}!")


def tiktok_comment():
    # username and password loop
    for i in range(len(usernames)):
        try:
            driver.delete_all_cookies()
            # opening TikTok page
            driver.get("https://www.tiktok.com/login/phone-or-email/email")
            sleep(10, 20)
            # finding email or username input box
            user = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input')
            # Sending username or email keys
            user.click()
            for character in usernames[i]:
                user.send_keys(character)
                sleep(0.1, 0.2)

            time.sleep(5)
            # finding password input box
            passw = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input')
            # Sending password keys
            passw.click()
            for character in passwords[i]:
                passw.send_keys(character)
                sleep(0.1, 0.2)

            sleep(1, 3)
            # Clicking on Signin button
            signin = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button')
            signin.click()
            driver.implicitly_wait(20)
            sleep(3, 10)
        except NoSuchElementException as error:
            print(error)
            print('There is Maximum attempts reached. waiting for 6 mins and try again')
            time.sleep(360)
            signin = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button')
            signin.click()
            driver.implicitly_wait(20)
            sleep(3, 10)
        finally:

            # Put the user input's username in the search bar.
            search = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/input')
            search.click()
            for char in user_username:
                search.send_keys(char)
                sleep(0.1, 0.2)
            # Clicking search button
            search_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/button')
            search_btn.click()
            driver.implicitly_wait(20)
            sleep(5, 15)
            # clicking on accounts tab
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]').click()
            sleep(5, 15)

            # Compare the user input and top 10 search results. If they are the same, click on the user's profile.
            for line in range(1, 10):
                try:
                    search_results = driver.find_element(By.XPATH,
                                                         f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[{line}]/a['
                                                         f'2]/p[1]')
                    if search_results.text == user_username:
                        # Clicking on profile to go profile page
                        driver.find_element(By.XPATH,
                                            f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[{line}]').click()
                        sleep(5, 15)
                        break
                    else:
                        pass
                except:
                    # Printing output for unsuccessful
                    print(f"Could not find username: '{user_username}'.")

        for vid in range(1, 10):
            # clicking on video
            driver.find_element(By.XPATH,
                                f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[{vid}]/div[1]/div/div/a/div').click()
            # waiting for 30 seconds to watch video
            time.sleep(10)
            # Comments list to get random comments
            comments = ['Good', 'Very nice' 'brilliant', 'fantastic', 'thumbup for this one bro', 'wow excellent',
                        'I like it.',
                        'lovely']
            # Commenting in below line
            time.sleep(15)
            comnt = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[4]/div/div[1]/div/div['
                                        '1]/div/div/div[2]/div/div/div/div')
            # Random comment
            comnt.send_keys(random.choice(comments))
            # clicking on  post button
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[4]/div/div[2]').click()

            time.sleep(2)
            # closing video here
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div[1]/button[1]').click()
            time.sleep(5)
        driver.quit()
        print(f"Commented on {user_username} video!")


while True:

    # Get the user input for what they need.
    user_input = int(input(
        "What do you need? \n [1] Followers \n[2] likes & views \n[3] comments? \n please give answer in number\n"))

    if user_input == 1:
        tiktok_follow()
    elif user_input == 2:
        tiktok_like_view()
    elif user_input == 3:
        tiktok_comment()
    else:
        print('Sorry please input numbers only')
    for_cont = input("Do You want To continue???\n yes or no \n").lower()
    if for_cont == 'yes':
        pass
    else:
        break
