# Copyright 2023 Elijah Gordon (SLcK) <braindisassemblue@gmail.com>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import pygame
import random


def initialize_pygame():
    pygame.init()
    pygame.mixer.init()


def initialize_characters():
    return [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'ァ', 'ア', 'ィ', 'イ', 'ゥ', 'ウ', 'ェ', 'エ', 'ォ',
        'オ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ', 'ケ', 'ゲ',
        'コ', 'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ', 'セ',
        'ゼ', 'ソ', 'ゾ', 'タ', 'ダ', 'チ', 'ヂ', 'ッ', 'ツ',
        'ヅ', 'テ', 'デ', 'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ',
        'ノ', 'ハ', 'バ', 'パ', 'ヒ', 'ビ', 'ピ', 'フ', 'ブ',
        'プ', 'ヘ', 'ベ', 'ペ', 'ホ', 'ボ', 'ポ', 'マ', 'ミ',
        'ム', 'メ', 'モ', 'ャ', 'ヤ', 'ュ', 'ユ', 'ョ', 'ヨ',
        'ラ', 'リ', 'ル', 'レ', 'ロ', 'ヮ', 'ワ', 'ヰ', 'ヱ',
        'ヲ', 'ン', 'ヴ', 'ヵ', 'ヶ', 'ヷ', 'ヸ', 'ヹ', 'ヺ',
        '・', 'ー', 'ヽ', 'ヾ'
    ]


def initialize_fonts_and_chars(characters):
    font = pygame.font.Font('../font/MS Mincho.ttf', 35)
    color = (0, 255, 0)
    chars = [font.render(char, True, color) for char in characters]
    return font, chars


def initialize_display():
    caption = pygame.display.set_caption('(Matorikkusu)')
    screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
    display = pygame.Surface((1920, 1080))
    display.set_alpha(random.randrange(30, 40, 5))
    pygame.display.set_icon(pygame.image.load('../logo/logo.png'))
    return screen, display


def initialize_audio():
    pygame.mixer.music.load('../audio/audio.wav')
    pygame.mixer.music.play(loops=-1)


class Matorikkusu:
    def __init__(self, x, y, screen, chars):
        self.x = x
        self.y = y
        self.screen = screen
        self.chars = chars
        self.color = (0, 255, 0)

    def draw(self):
        char = random.choice(self.chars)
        if self.y < 1080:
            self.y = self.y + 30
        else:
            self.y = -40 * random.randrange(1, 5)

        colored_char = pygame.Surface(char.get_size(), pygame.SRCALPHA)

        colored_char.blit(char, (0, 0))
        for y in range(colored_char.get_height()):
            for x in range(colored_char.get_width()):
                a = colored_char.get_at((x, y))[3]
                if a > 0:
                    colored_char.set_at((x, y), (*self.color, a))

        self.screen.blit(colored_char, (self.x, self.y))

    def set_color(self, color):
        self.color = color


def change_color(key):
    global color
    colors = {
        pygame.K_b: (0, 0, 255),
        pygame.K_c: (0, 255, 255),
        pygame.K_d: (110, 75, 38),
        pygame.K_e: (255, 121, 77),
        pygame.K_f: (246, 74, 138),
        pygame.K_g: (0, 255, 0),
        pygame.K_h: (223, 115, 255),
        pygame.K_r: (255, 0, 0),
        pygame.K_w: (255, 255, 255),
        pygame.K_y: (255, 255, 0),
        pygame.K_m: (255, 0, 255),
        pygame.K_o: (128, 128, 0),
        pygame.K_t: (0, 128, 128),
    }
    if key in colors:
        color = colors[key]


def main_loop(screen, display, symbols, font, chars):
    global color
    run = True
    delay = 0

    color = (0, 255, 0)
    change_color(pygame.K_g)

    while run:
        screen.blit(display, (0, 0))
        display.fill(pygame.Color('black'))

        for symbol in symbols:
            symbol.draw()

        pygame.time.delay(delay)
        pygame.display.update()
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_LEFT and delay > 0:
                    delay -= 15
                if event.key == pygame.K_RIGHT and delay < 150:
                    delay += 15
                if event.key in [pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e,
                                 pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_r,
                                 pygame.K_w, pygame.K_y, pygame.K_m, pygame.K_o,
                                 pygame.K_t]:
                    change_color(event.key)

                    for symbol in symbols:
                        symbol.set_color(color)

                if event.key == pygame.K_p:
                    pygame.mixer.music.pause()
                if event.key == pygame.K_u:
                    pygame.mixer.music.unpause()


def main():
    initialize_pygame()
    characters = initialize_characters()
    font, chars = initialize_fonts_and_chars(characters)
    screen, display = initialize_display()
    symbols = [Matorikkusu(i, random.randrange(-1020, 0), screen, chars) for i in range(0, 1920, 15 * 2)]
    initialize_audio()
    main_loop(screen, display, symbols, font, chars)


if __name__ == "__main__":
    main()
