from PIL import Image, ImageDraw, ImageFont
import RedditScraper


def split_text_into_lines(text, lines):
    max_length = 77
    actual_line = ''
    for word in text.split():
        if len(actual_line) + len(word) + 1 <= max_length:
            actual_line += ' ' + word
        else:
            lines.append(actual_line)
            actual_line = word

    if len(actual_line):
        lines.append(actual_line)
    return lines


def img_converter(say):
    lines = []
    text = say
    x = 20
    y = 20
    line_space = 30
    print(len(text))
    lines = split_text_into_lines(text, lines)

    new = Image.new('RGB', (1000, len(lines)*line_space+50), color=(26, 26, 27))
    d = ImageDraw.Draw(new)
    fnt = ImageFont.truetype("arial.ttf", 25)

    print(lines)
    for paragraph in lines:
        d.text((x, y), paragraph, font=fnt, fill=(255, 255, 255))
        y += line_space
    print(x, y)
    print(text)
    new.save('paragraph.jpg')
    lines.clear()
    return new

