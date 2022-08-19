from flask import render_template, request
import random
import string


def GeraSenha():
    if request.method == "POST":
        try:
            size = int(request.form.get('pwd_size'))
            pwd_list = []
            a_to_z_lower = list(string.ascii_lowercase)
            a_to_z_upper = list(string.ascii_uppercase)
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            all_char = a_to_z_lower + a_to_z_upper + numbers

            for num in range(size):
                rand = random.randrange(0, len(all_char))
                pwd_list.append(all_char[rand])

            pwd = ''.join(pwd_list)
        except:
            pwd = 'Ocorreu um erro!'

        return render_template('passgen.html', pwd=pwd)
    else:
        return render_template('passgen.html', pwd=None)
