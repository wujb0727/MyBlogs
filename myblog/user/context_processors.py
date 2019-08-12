# encoding: utf-8
# @Author: TiAmo
# @Project: MyBlogs 
# @Time: 2019/8/12 15:09

from .forms import LoginForm


def login_model_form(requests):
    return {'login_model_form': LoginForm()}
