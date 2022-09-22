class HomePage():

    mainurl = "https://betpassionfun.draft10.com/"

    tournamentbutton_xpath = '//*[@id="root"]/div/div[1]/ul/li[1]/a'
    tournamentpage_url = f"{mainurl}tournament"

    guidebutton_xpath = '//*[@id="root"]/div/div[1]/ul/li[2]/a'
    guidepage_url = f"{mainurl}guide"

    newsbutton_xpath = '//*[@id="root"]/div/div[1]/ul/li[3]/a'
    newspage_url = f"{mainurl}news"

    rulesbutton_xpath = '//*[@id="root"]/div/div[1]/ul/li[4]/a'
    rulespage_url = f"{mainurl}rules"

    homelogo_xpath = '//*[@id="root"]/div/div[1]/div[1]/div/img'
    homepage_url = f"{mainurl}"

    loginbutton_xpath = '//*[@id="root"]/div/div[1]/div[2]/button[1]'
    loginpage_url = f"{mainurl}login"

    registerbutton_xpath = '//*[@id="root"]/div/div[1]/div[2]/button[2]'
    registerpage_url = f"{mainurl}register"

    suggest1000pp_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/button'
    suggest1000pp_classname = 'home-page__greeting-content--sign-in-button selectorgadget_selected'
    "//button[@class='home-page__greeting-content--sign-in-button']"

    facebookicon_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]'
    facebookpage_url = "https://www.facebook.com/NoiSiamoPassione"

    instaicon_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[2]'
    instapage_url = "https://www.instagram.com/betpassion.it/"

    telegramicon_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[3]'
    telegrampage_url = "https://t.me/betpassionofficial"

    youtubeicon_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[4]'
    youtubepage_url = "https://www.youtube.com/results?search_query=betpassion.info"

    """futer legal aspects"""
    cookie_policy_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/span[1]/a'
    cookie_policy_url = "https://www.iubenda.com/privacy-policy/30380830/cookie-policy"

    privacy_policy_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/span[2]/a'
    privacy_policy_url = "https://www.iubenda.com/privacy-policy/30380830"

    terms_and_conditions_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/span[3]/a'
    terms_and_conditions_url = "https://www.iubenda.com/termini-e-condizioni/30380830"

    """futer menu elements"""
    menu_tournamentbutton_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]/span'
    menu_guidebutton_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a[2]/span'
    menu_newsbutton_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a[3]/span'
    menu_rulesbutton_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a[4]/span'

    login2_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div/form/div[4]/button'