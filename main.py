import sys
import customtkinter
from customtkinter import CTkSwitch
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

languages = {
    "русский(английский)": "ru,en;q=0.9",
    "русский(белорусский)": "ru,be;q=0.9",
    "русский(испанский)": "ru,es;q=0.9",
    "английский(русский)": "en,ru;q=0.9",
    "английский(белорусский)": "en,be;q=0.9",
    "английский(испанский)": "en,es;q=0.9",
    "белорусский(русский)": "be,ru;q=0.9",
    "белорусский(английский)": "be,en;q=0.9",
    "испанский(русский)": "es,ru;q=0.9",
    "испанский(английский)": "es,en;q=0.9",
}
user_agents = {
    "chrome_1": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "chrome_2": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "chrome_3": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "chrome_4": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "chrome_5": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.1.468 Yowser/2.5 Safari/537.36",
    "yandex_1": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 YaBrowser/20.12.2.105 Yowser/2.5 Safari/537.36",
    "yandex_2": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 YaBrowser/20.12.2.108 Yowser/2.5 Safari/537.36",
    "yandex_3": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.165 Yowser/2.5 Safari/537.36",
    "yandex_4": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "yandex_5": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "firefox_1": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "firefox_2": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "firefox_3": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "firefox_4": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "firefox_5": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "safari_1": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:84.0) Gecko/20100101 Firefox/84.0",
    "safari_2": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)",
    "safari_3": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "safari_4": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.112 Yowser/2.5 Safari/537.36",
    "safari_5": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
    "headless_chrome_1": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/88.0.4298.0 Safari/537.36",
    "duckduckgo_bot_1": "Mozilla/5.0 (compatible; DuckDuckGo-Favicons-Bot/1.0; +http://duckduckgo.com)",
    "other_1": "CCBot/2.0 (https://commoncrawl.org/faq/)",
    "other_2": "Mozilla/5.0 (compatible; proximic; +http://www.proximic.com/info/spider.php)"
}


def get_info(obj):
    if obj == 'webrtc':
        return 'WebRTC потенциально раскрывает реальные локальные и \n' \
               'общедоступные IP-адреса пользователя, даже при \n' \
               'использовании VPN или прокси-сервера. Этот инструмент \n' \
               'предотвратит утечку реального общедоступного IP-адреса.'
    elif obj == 'webgl':
        return 'Информация о включении или выключении \n' \
               'поддержки WebGL в браузере.\n' \
               'WebGL позволяет веб-сайтам собирать подробную \n' \
               'информацию о видеокарте и хэш отчетах данных WebGL'
    elif obj == 'canvas':
        return 'Информация о включении или выключении \n' \
               'поддержки HTML5 Canvas в браузере.\n' \
               'Canvas раскрывает информацию о различиях \n' \
               'отображения изображения холста, а также об \n' \
               'уникальной подписи Canvas, что используется для \n' \
               'создания fingerprints'
    elif obj == 'javascript':
        return 'Информация о включении или выключении \n' \
               'поддержки JavaScript в браузере.С помощью \n' \
               'JavaScript веб-ресурсы получают информацию \n' \
               'о разрешении экрана устройства, местном времени \n' \
               'и исходном ресурсе (URL источнику запроса). '
    elif obj == 'incognito':
        return 'Режим инкогнито (инкогнито-режим) позволяет вам \n' \
               'пользоваться браузером приватно, не сохраняя историю \n' \
               'посещений и личные данные в процессе сеанса. В этом \n' \
               'режиме браузер не сохраняет файлы cookie, данные \n' \
               'ввода на веб-страницах, а также временные файлы \n' \
               'временного интернет-файла.'
    elif obj == 'languages':
        return 'Стандартный язык браузера.'
    elif obj == 'user_agent':
        return 'Текущий агент пользователя.'
    elif obj == 'proxy':
        return 'Текущий прокси.'
    else:
        return 'Нет информации для указанного объекта.'


chrome_options = Options()


def get_info_to_browser(obj):
    with open("res/config.txt", "r") as user_file:
        lines = user_file.readlines()
        for line in lines:
            line = line.strip()
            if str(obj) in line:
                return str(line.split("$")[1].strip())


def get_status(obj):
    with open("res/config.txt", "r") as user_file:
        lines = user_file.readlines()
        for line in lines:
            line = line.strip()
            if str(obj) in line:
                return str(line.split("$")[1].strip())


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, name=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("+{}+{}".format((self.winfo_screenwidth() - 500) // 2, (self.winfo_screenheight() - 300) // 2))
        self.minsize(500, 300)
        self.maxsize(500, 300)
        self.label = customtkinter.CTkLabel(self, text=get_info(name), font=("arial", 16))
        self.label.pack(padx=20, pady=20)
        self.after(200, lambda: self.iconbitmap('res/i.ico'))
        self.title("Подробнее")



class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Конфигурация браузера")

        top_frame_for_webrtc = customtkinter.CTkFrame(self, fg_color="transparent")
        top_frame_for_webrtc.pack(side="top", pady=15)

        top_frame_for_webgl = customtkinter.CTkFrame(self, fg_color="transparent")
        top_frame_for_webgl.pack(side="top", pady=15)

        top_frame_for_canvas = customtkinter.CTkFrame(self, fg_color="transparent")
        top_frame_for_canvas.pack(side="top", pady=15)

        top_frame_for_javascript = customtkinter.CTkFrame(self, fg_color="transparent")
        top_frame_for_javascript.pack(side="top", pady=15)

        top_frame_for_incognito = customtkinter.CTkFrame(self, fg_color="transparent")
        top_frame_for_incognito.pack(side="top", pady=15)

        top_frame_for_languages = customtkinter.CTkFrame(self, fg_color="transparent")
        top_frame_for_languages.pack(side="top", pady=15)

        top_frame_for_user_agent = customtkinter.CTkFrame(self, fg_color="transparent")
        top_frame_for_user_agent.pack(side="top", pady=15)

        proxy_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        proxy_frame.pack(side="top", pady=15)

        #  webrtc
        switch_var_webrtc = customtkinter.IntVar(value=int(get_status("webrtc")))
        self.switch_webrtc = CTkSwitch(master=top_frame_for_webrtc, text="webrtc", variable=switch_var_webrtc)
        self.switch_webrtc.pack(side="left", padx=20)
        self.button_more_info_webrtc = customtkinter.CTkButton(top_frame_for_webrtc, text="Подробнее",
                                                               command=lambda: self.open_info(name="webrtc"))
        self.button_more_info_webrtc.pack(side="right", padx=0)

        # webgl
        switch_var_webgl = customtkinter.IntVar(value=int(get_status("webgl")))
        self.switch_webgl = CTkSwitch(master=top_frame_for_webgl, text="webgl", variable=switch_var_webgl)
        self.switch_webgl.pack(side="left", padx=20)
        self.button_more_info_webgl = customtkinter.CTkButton(top_frame_for_webgl, text="Подробнее",
                                                              command=lambda: self.open_info(name="webgl"))
        self.button_more_info_webgl.pack(side="right", padx=0)

        # canvas
        switch_var_canvas = customtkinter.IntVar(value=int(get_status("canvas")))
        self.switch_canvas = CTkSwitch(master=top_frame_for_canvas, text="canvas", variable=switch_var_canvas)
        self.switch_canvas.pack(side="left", padx=20)
        self.button_more_info_canvas = customtkinter.CTkButton(top_frame_for_canvas, text="Подробнее",
                                                               command=lambda: self.open_info(name="canvas"))
        self.button_more_info_canvas.pack(side="right", padx=0)

        # javascript
        switch_var_javascript = customtkinter.IntVar(value=int(get_status("javascript")))
        self.switch_javascript = CTkSwitch(master=top_frame_for_javascript, text="javascript",
                                           variable=switch_var_javascript)
        self.switch_javascript.pack(side="left", padx=20)
        self.button_more_info_javascript = customtkinter.CTkButton(top_frame_for_javascript, text="Подробнее",
                                                                   command=lambda: self.open_info(name="javascript"))
        self.button_more_info_javascript.pack(side="right", padx=0)

        # incognito
        switch_var_incognito = customtkinter.IntVar(value=int(get_status("incognito")))
        self.switch_incognito = CTkSwitch(master=top_frame_for_incognito, text="incognito",
                                          variable=switch_var_incognito)
        self.switch_incognito.pack(side="left", padx=20)
        self.button_more_info_incognito = customtkinter.CTkButton(top_frame_for_incognito, text="Подробнее",
                                                                  command=lambda: self.open_info(name="incognito"))
        self.button_more_info_incognito.pack(side="right", padx=0)

        # languages
        self.label_languages = customtkinter.CTkLabel(top_frame_for_languages, text="Язык")
        self.label_languages.pack(side="left", padx=10)

        selected_language = customtkinter.StringVar(value=str(get_status("language")))  # Set a default language
        self.combobox_languages = customtkinter.CTkComboBox(top_frame_for_languages, values=list(languages.keys()),
                                                            width=200, )
        self.combobox_languages.set(selected_language.get())  # Set the default value
        self.combobox_languages.pack(side="left", padx=10)
        self.button_more_info_languages = customtkinter.CTkButton(top_frame_for_languages, text="Подробнее",
                                                                  command=lambda: self.open_info(name="languages"))
        self.button_more_info_languages.pack(side="bottom", padx=10)

        # user agents
        self.label_user_agent = customtkinter.CTkLabel(top_frame_for_user_agent, text="Агент пользователя")
        self.label_user_agent.pack(side="left", padx=20)

        selected_user_agent = customtkinter.StringVar(value=str(get_status("user_agent")))  # Set a default user agent
        self.combobox_user_agent = customtkinter.CTkComboBox(top_frame_for_user_agent,
                                                             values=list(user_agents.keys()), width=150)
        self.combobox_user_agent.set(selected_user_agent.get())  # Set the default value
        self.combobox_user_agent.pack(side="left", padx=10)
        self.button_more_info_user_agent = customtkinter.CTkButton(top_frame_for_user_agent, text="Подробнее",
                                                                   command=lambda: self.open_info(name="user_agent"))
        self.button_more_info_user_agent.pack(side="bottom", padx=10)

        # Proxy 
        self.label_proxy = customtkinter.CTkLabel(proxy_frame, text="Прокси")
        self.label_proxy.pack(side="left", padx=20)

        selected_proxy_ip = customtkinter.StringVar(value=str(get_status("proxy_ip")))  # Set a default user agent
        self.entry_proxy_ip = customtkinter.CTkEntry(proxy_frame, width=175,
                                                     textvariable=selected_proxy_ip)  # Adjust the width as needed
        self.entry_proxy_ip.pack(side="left", padx=10)

        selected_proxy_port = customtkinter.StringVar(value=str(get_status("proxy_port")))  # Set a default user agent
        self.entry_proxy_port = customtkinter.CTkEntry(proxy_frame, width=100,
                                                       textvariable=selected_proxy_port)  # Adjust the width as needed
        self.entry_proxy_port.pack(side="left", padx=10)

        self.button_more_info_proxy = customtkinter.CTkButton(proxy_frame, text="Подробнее",
                                                              command=lambda: self.open_info(name="proxy"))
        self.button_more_info_proxy.pack(side="bottom", padx=10)

        # -------------------------------

        bottom_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        bottom_frame.pack(side="bottom", pady=30)
        self.button_open_browser = customtkinter.CTkButton(bottom_frame, text="Запуск браузера",
                                                           command=self.launch_browser,
                                                           height=50,
                                                           width=200,
                                                           font=("", 16))
        self.button_save_changes = customtkinter.CTkButton(bottom_frame, text="Сохранить изменения",
                                                           command=self.save_changes,
                                                           height=50,
                                                           width=200,
                                                           font=("", 16))
        self.button_open_browser.pack(side="right", padx=10)
        self.button_save_changes.pack(side="left", padx=10)

        self.new_window = None

    def open_info(self, name):
        if self.new_window is None or not self.new_window.winfo_exists():
            # создание нового окна
            self.new_window = ToplevelWindow(self, name=name)
        else:
            # фокус на окне
            self.new_window.focus()

    def save_changes(self):
        config_data = [
            f"webrtc${self.switch_webrtc.get()}",
            f"webgl${self.switch_webgl.get()}",
            f"canvas${self.switch_canvas.get()}",
            f"javascript${self.switch_javascript.get()}",
            f"incognito${self.switch_incognito.get()}",
            f"language${self.combobox_languages.get()}",
            f"user_agent${self.combobox_user_agent.get()}",
            f"proxy_ip$ {self.entry_proxy_ip.get()}",
            f"proxy_port$ {self.entry_proxy_port.get()}"
        ]

        print(config_data)  

        with open("res/config.txt", "w") as config_file:
            for status in config_data:
                config_file.write(f"{status}\n")

        print("Changes saved.")

    def launch_browser(self):

        argument_webgl = None
        argument_canvas = None
        argument_incognito = None
        argument_user_agent = None
        argument_proxy = None
        preferences = {}

        print(get_info_to_browser("webrtc"))
        print(get_info_to_browser("webgl"))
        print(get_info_to_browser("canvas"))

        if get_info_to_browser("webrtc") == "0":
            preferences["webrtc.ip_handling_policy"] = "disable_non_proxied_udp"
            preferences["webrtc.multiple_routes_enabled"] = False
            preferences["webrtc.nonproxied_udp_enabled"] = False
        if get_info_to_browser("webgl") == "0":
            argument_webgl = "--disable-webgl"
        if get_info_to_browser("canvas") == "0":
            argument_canvas = "--disable-reading-from-canvas"
        if get_info_to_browser("javascript") == "0":
            preferences["profile.managed_default_content_settings.javascript"] = 2
        if get_info_to_browser("user_agent") is not None:
            argument_user_agent = f"user-agent={user_agents[get_info_to_browser('user_agent')]}"
        if get_info_to_browser("incognito") == "1":
            argument_incognito = "--incognito"
        if get_info_to_browser("proxy_ip") != "" and get_info_to_browser("proxy_port") != "":
            argument_proxy = f"--proxy-server=http://{get_info_to_browser('proxy_ip')}:{get_info_to_browser('proxy_port')}"
            print("=" + get_info_to_browser("proxy_ip") + "=")
            print("=" + get_info_to_browser("proxy_port") + "=")
        else:
            print("proxy_ip or proxy_port not found")

        preferences["intl"] = {"accept_languages": languages[get_info_to_browser("language")]}

        # Изменение аргументов

        if argument_webgl is not None:
            chrome_options.add_argument(str(argument_webgl))
        if argument_canvas is not None:
            chrome_options.add_argument(str(argument_canvas))
        if argument_incognito is not None:
            chrome_options.add_argument(str(argument_incognito))
        if argument_user_agent is not None:
            chrome_options.add_argument(str(argument_user_agent))
        if argument_proxy is not None:
            chrome_options.add_argument(str(argument_proxy))

        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # - плашка
        chrome_options.add_argument('--start-maximized')  # Запуск в полный экран
        chrome_options.add_experimental_option("prefs", preferences)

        try:
            self.destroy()

            x = Browser()

        except FileNotFoundError:
            print("Error: The 'browser.py' script was not found.")


class Browser:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        driver = webdriver.Chrome(options=chrome_options)

        # закрузка сайта
        url_0 = "https://google.com/"
        url_1 = "https://browserleaks.com/"
        url_2 = "https://fingerprintjs.github.io/fingerprintjs/"
        with open("res/index.txt", "r") as url_file:
            url = url_file.readlines()[0].strip()
        try:
            driver.get(url)
        except Exception as e:
            print(e)

        # ожидание закрытия окна
        while True:
            if driver.window_handles:
                continue
            else:
                break
        driver.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.iconbitmap("res/i.ico")
    # создание окна
    app.update_idletasks()
    width = 600
    height = 700
    x = (app.winfo_screenwidth() // 2) - (width // 2)
    y = (app.winfo_screenheight() // 2) - (height // 2)
    app.geometry(f"{width}x{height}+{x}+{y}")

    # старт окна
    app.mainloop()
