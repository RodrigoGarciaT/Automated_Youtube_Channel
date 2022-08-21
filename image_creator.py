from PIL import Image, ImageDraw, ImageFont
lines = []


def split_text_into_lines(text):
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


text = "I (16m) am moving due to my mom having another kid with her husband. I was visiting the house one last time to pack some stuff up when I started crying in front of my 10 year old brother. Hard. I've hated every single part of this move since it started. Where I lived was isolated. I had a good excuse not to hang out with friends after school. I had an amazing job that let me customize my entire schedule with a great boss, and not a single co-worker I disliked. There were no messed up people in town, compared to the homeless people in the park who've tried giving me alcohol every time I've walked past them at the new place. There was a great church that let me practice my faith the way I wanted too, compared to the one who's pastor told me my autism was caused by a demon, and adviced an exorcism. But I cried over it. That's the problem. I'm the oldest of my siblings, so I'm supposed to be a man, and suck things like this up, not cry in front of my brother who feels the same way."
x = 20
y = 20
line_space = 30
print(len(text))
split_text_into_lines(text)

new = Image.new('RGB', (1000, len(lines)*line_space+50), color=(26, 26, 27))
d = ImageDraw.Draw(new)
fnt = ImageFont.truetype("arial.ttf", 25)

print(lines)
for paragraph in lines:
    d.text((x, y), paragraph, font=fnt, fill=(255, 255, 255))
    y += line_space
print(x, y)
new.save('paragraph.jpg')