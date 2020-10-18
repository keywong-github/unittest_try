from poium import Page,PageElement

class login_page(Page):
    login_click=PageElement(xpath='//*[@id="u1"]/a',describe='点击登录')
    
    login_exchange=PageElement(xpath='//*[@id="TANGRAM__PSP_11__footerULoginBtn"]',describe='点击切换登录方式')

    login_username=PageElement(name="userName",describe='输入账号')

    login_password=PageElement(name="password",describe='输入密码')

    login_enter=PageElement(id_="TANGRAM__PSP_11__submit",describe='点击【登录】')