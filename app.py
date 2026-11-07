from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# YAHAN APNI 6 API KEYS DALO - FREE WALI
API_KEYS = {
    "gemini1": "APNI_GEMINI_KEY_1_YAHAN",
    "gemini2": "APNI_GEMINI_KEY_2_YAHAN",
    "groq1": "APNI_GROQ_KEY_1_YAHAN",
    "groq2": "APNI_GROQ_KEY_2_YAHAN",
    "hugging1": "APNI_HUGGINGFACE_KEY_1",
    "openai1": "APNI_OPENAI_KEY_1"
}

# MARKAZ, DARAZ SE PRODUCT NIKALNA
@app.route('/api/get-product')
def get_product():
    source = request.args.get('source')
    # Demo data - Asli me yahan Markaz API lagay gi
    products = {
        "markaz": {"name": "Steel Watch", "price": 500},
        "daraz": {"name": "Earbuds Pro", "price": 650},
        "priceoye": {"name": "Mobile Cover", "price": 300},
        "goto": {"name": "Shoes", "price": 1200},
        "temu": {"name": "LED Light", "price": 400}
    }
    return jsonify(products.get(source, {"name": "Watch", "price": 500}))

# AI SE URDU BANANA - 6 API KA SYSTEM
@app.route('/api/make-urdu', methods=['POST'])
def make_urdu():
    data = request.json
    provider = data.get('provider')
    key = data.get('key') or API_KEYS.get(provider)
    
    prompt = "Is product ko asaan urdu me bechne wali description banao: Steel Watch, Faisalabad COD"
    
    # 1. GEMINI
    if 'gemini' in provider:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
            r = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]})
            text = r.json()['candidates'][0]['content']['parts'][0]['text']
            return jsonify({"urdu": text})
        except: pass
    
    # 2. GROQ
    if 'groq' in provider:
        try:
            r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers={"Authorization": f"Bearer {key}"}, json={"model": "llama-3.1-8b-instant", "messages": [{"role": "user", "content": prompt}]})
            return jsonify({"urdu": r.json()['choices'][0]['message']['content']})
        except: pass

    # 3. HUGGING FACE
    if 'hugging' in provider:
        try:
            r = requests.post("https://api-inference.huggingface.co/models/google/gemma-2-2b-it", headers={"Authorization": f"Bearer {key}"}, json={"inputs": prompt})
            return jsonify({"urdu": str(r.json())})
        except: pass

    return jsonify({"urdu": "Original Steel wali Ghari, pani se kharab nahi hoti, Faisalabad me ghar bethy mile gi, Cash on Delivery hai."})

if __name__ == '__main__':
    app.run(debug=True)
