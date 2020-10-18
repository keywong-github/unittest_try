from poium import Page,PageElement
class PageSa(Page):
    username_input=PageElement(id_="username",describe="登录名输入框")
    password_input=PageElement(id_="password",describe="密码输入框") 
    loginin=PageElement(xpath='//*[@id="form1"]/div/table/tbody/tr[4]/td/input',describe="登录按钮") 