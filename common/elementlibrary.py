from common.common_fun import Common, By


# 登录操作
class Login(Common):
    iframe =(By.TAG_NAME, "iframe")
    # 登录文案
    login = (By.CSS_SELECTOR, 'button.el-button.loginBtn.el-button--default')
    #密码登录页面
    password = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.loginDialog > div > div.el-dialog__body > '
                                'div > div.loginMain > div:nth-child(1) > div.tabs > div:nth-child(3)')
    # 账号输入框
    username_type = (By.CSS_SELECTOR,  '.el-input__inner[placeholder="请输入账号"]')
    # 密码输入框
    password_type =(By.CSS_SELECTOR,  '.el-input__inner[placeholder="请输入密码"]')
    #勾选协议
    agree = (By.CSS_SELECTOR, '.bottomRadio .icon-sohu-danxuanweixuanzhong')
    # 登录按钮
    loginBtn = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.loginDialog > div > div.el-dialog__body > div > div.loginMain > button')



class fontpage (Common):
    video =(By.CSS_SELECTOR, '#app > section > section > main > div > div > div.leftMainBox > div.videoContainer > div.videoList > div:nth-child(1) > div.maskBox')
    all_videos = (By.CSS_SELECTOR, '#app > section > section > main > div > div > div.leftMainBox > div.videoContainer > div.videoList > div')
    like = (By.CSS_SELECTOR, '#app > section > section > main > div > div > div.leftMainBox > div.videoContainer > div.videoList > div:nth-child(1) > '
                             'div:nth-child(3) > div > div.btn-box > div.btns-main > div:nth-child(3) > i')
    comment = (By.CSS_SELECTOR, '#app > section > section > main > div > div > div.leftMainBox > div.videoContainer > div.videoList > div:nth-child(1) > '
                                'div:nth-child(3) > div > div.btn-box > div.btns-main > div:nth-child(4) > i')
    comment_type = (By.CSS_SELECTOR, 'body > div.el-drawer__wrapper > div > div > section > div > div > div:nth-child(2) > div > div > input')
    comment_submit =  (By.CSS_SELECTOR, 'body > div.el-drawer__wrapper > div > div > section > div > div > div:nth-child(2) > div > p')
    commentcls = (By.CSS_SELECTOR, '#el-drawer__title > button > i')