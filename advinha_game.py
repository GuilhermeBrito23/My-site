from flask import render_template, request
import random


def gera_word():
    try:
        file = open('words.txt', 'r')
        file_content = list(file.read().split('\n'))
        rand = random.randrange(len(file_content))
        true_word = file_content[rand]
        file.close()
    except:
       true_word= 'Ocorreu um erro ao Gerar a palavra!'
    return true_word


def adivinha_game_func():
    win =''
    try:
        if request.method == 'GET':

            global word
            global guess_word

            word= gera_word()
            guess_word = ['_' for letter in word]
            return render_template('advinha-game.html', word=guess_word)
        else:
            guess = request.form.get('guess').lower()
            count = 0
            for letter in word:
                if guess== letter:
                    guess_word[count] = guess
                count += 1

            if '_' not in guess_word:
                 win='ACERTOOU!!'
            return render_template('advinha-game.html', word=guess_word,win=win)
    except:
        return render_template('advinha-game.html', word="Aconteceu algum erro :(")