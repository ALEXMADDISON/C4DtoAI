import c4d
import requests
import json
import base64
from c4d import documents

def render_with_stable_diffusion():
    # Путь к рендеру в Cinema 4D
    render_path = r"C:\Users\import.png"  # Укажите путь к рендеру
    output_path = r"C:\Users\AITextureRender.png"  # Укажите путь для сохранения обработанного изображения

    # Запрос у пользователя текста для prompt
    prompt = c4d.gui.InputDialog("Какую текстуру вы хотите создать? (prompt):")
    if not prompt:
        c4d.gui.MessageDialog("Prompt не может быть пустым!")
        return

    negative_prompt = c4d.gui.InputDialog("Введите негативный prompt (необязательно):", "blurry, low quality")
    if not negative_prompt:
        negative_prompt = "blurry, low quality"

    # Загрузите изображение и закодируйте его в Base64
    try:
        with open(render_path, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        c4d.gui.MessageDialog(f"Не удалось найти файл для рендера: {render_path}")
        return

    # Настройте запрос к Stable Diffusion API
    url = "http://127.0.0.1:7860/sdapi/v1/img2img"  # Путь к API
    payload = {
        "init_images": [image_base64],
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "denoising_strength": 0.5,
        "cfg_scale": 11,
        "steps": 40
,
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        c4d.gui.MessageDialog(f"Ошибка при запросе: {e}")
        return

    # Декодируйте результат
    try:
        result = response.json()["images"][0]
        output_image = base64.b64decode(result)

        with open(output_path, "wb") as output_file:
            output_file.write(output_image)

        c4d.gui.MessageDialog(f"Рендер завершен! Результат сохранен в {output_path}")
    except (KeyError, json.JSONDecodeError) as e:
        c4d.gui.MessageDialog(f"Ошибка при обработке ответа API: {e}")

if __name__ == "__main__":
    render_with_stable_diffusion()
