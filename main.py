import base64
import random

from PIL import Image


def combine_images(image_paths, number):
    first_image_path = image_paths[0]
    first_image = Image.open(first_image_path).convert("RGBA")
    combined_image = Image.new("RGBA", first_image.size)
    combined_image.paste(first_image, (0, 0))

    for image_path in image_paths[1:]:
        image = Image.open(image_path).convert("RGBA")
        combined_image = Image.alpha_composite(combined_image, image)

    save_path = f'results/StampRock{number}.png'
    combined_image.save(save_path)

    image64_txt = image_to_base64(save_path)
    save_path64 = f'results64/StampRock{number}.txt'
    save_base64_to_txt(image64_txt, save_path64)


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base64_encoded = base64.b64encode(binary_data).decode('utf-8')
        return base64_encoded


def save_base64_to_txt(base64_data, txt_file_path):
    with open(txt_file_path, "w") as txt_file:
        txt_file.write(base64_data)


def select_base(image_paths):
    body_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_value = random.choices(body_list, weights=[0.3, 0.25, 0.3,
                                                      0.3, 0.3, 0.2, 0.25,
                                                      0.15, 0.1, 0.05], k=1)[0]
    path = f"sandbox/base/base{random_value}.png"
    image_paths.append(path)
    return random_value


def select_head(image_paths):
    head_list = ["bandana", "capforward", "cowboyhat",
                 "crazyhair", "headband", "hoodie",
                 "knittedcap", "mohawk", "tiara"]

    random_value = random.choices(head_list, weights=[0.3, 0.25, 0.1,
                                                      0.3, 0.3, 0.2, 0.25,
                                                      0.4, 0.05], k=1)[0]
    path = f"sandbox/head/{random_value}.png"
    image_paths.append(path)
    return random_value


def select_eyes(image_paths):
    eyes_list = ["shades", "red", "blue",
                 "green"]
    random_value = random.choices(eyes_list, weights=[0.3, 0.05, 0.1,
                                                      0.2], k=1)[0]
    path = f"sandbox/eyes/{random_value}.png"
    image_paths.append(path)
    return random_value


def select_mouth(image_paths):
    mouth_list = ["cigarette", "medicalmask", "pipe"]
    random_value = random.choices(mouth_list, weights=[0.8, 0.1, 0.35], k=1)[0]
    path = f"sandbox/mouth/{random_value}.png"
    image_paths.append(path)
    return random_value


def select_acc(image_paths):
    path = f"sandbox/acc/earring.png"
    image_paths.append(path)
    return 'earring'


if __name__ == "__main__":
    combinations = []
    for i in range(1, 334):
        existing = True
        while existing:
            combination = ""
            image_paths = []
            # select base
            base = select_base(image_paths)
            combination += str(base)
            # select head
            head_chance = random.uniform(0, 100)
            if head_chance >= 62:
                head = select_head(image_paths)
                combination += head
            # select eyes
            eyes_chance = random.uniform(0, 100)
            if eyes_chance <= 23:
                eyes = select_eyes(image_paths)
                combination += eyes
            # select mouth
            mouth_chance = random.uniform(0, 100)
            if mouth_chance <= 17:
                mouth = select_mouth(image_paths)
                combination += mouth
            # acc chance
            acc_chance = random.uniform(0, 100)
            if acc_chance <= 5:
                acc = select_acc(image_paths)
                combination += acc

            if combination not in combinations:
                combinations.append(combination)
                combine_images(image_paths, i)
                existing = False
            else:
                existing = True

