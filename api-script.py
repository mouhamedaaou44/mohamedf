import requests

def get_answer(question):
    url = 'https://api-samir.onrender.com/api/bard?question=' + question
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        answer = data.get('response', '')
        image_url = data.get('imgUrl', '')
        return answer, image_url
    else:
        return None, None

# استخدم الدالة للحصول على الإجابة ورابط الصورة
question = input('أدخل السؤال: ')
answer, image_url = get_answer(question)
print('الإجابة:', answer)
print('رابط الصورة:', image_url)
