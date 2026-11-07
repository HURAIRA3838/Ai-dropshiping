let basePrice = 500;
function getProduct(source){
  // Yahan se Python backend ko call hogi
  fetch('/api/get-product?source='+source)
  .then(r=>r.json())
  .then(d=>{
    document.getElementById('result').innerText = "Source: "+source+" | Product: "+d.name+" | Price: "+d.price;
    document.getElementById('basePrice').value = d.price;
    basePrice = d.price;
    calc();
  });
  // Agar backend na chale to demo data
  document.getElementById('result').innerText = source+" se product mil gaya! 500 Rs wali Ghari.";
}

function calc(){
  let p = document.getElementById('basePrice').value;
  let m = document.getElementById('myProfit').value;
  document.getElementById('finalPrice').innerText = (parseInt(p)+parseInt(m))+" Rs";
}

async function makeUrdu(){
  let key = document.getElementById('apiKey').value;
  let provider = document.getElementById('aiProvider').value;
  document.getElementById('result').innerText = "AI soch raha hai... "+provider+" use ho raha hai...";
  // Python ko bhejo
  let res = await fetch('/api/make-urdu', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({key:key, provider:provider, text:"Steel Watch"})});
  let data = await res.json();
  document.getElementById('result').innerText = data.urdu || "Original Steel wali Ghari, pani se kharab nahi hoti, Faisalabad me Cash on Delivery available hai.";
}

function postTo(platform){
  let price = document.getElementById('finalPrice').innerText;
  let text = document.getElementById('result').innerText + " Price: " + price;
  document.getElementById('postStatus').innerText = platform+" ke liye post ready hai. Official API se post hogi.";
  if(platform==='whatsapp'){
    window.open("https://wa.me/?text="+encodeURIComponent(text));
  }
}

function autoReply(){
  let msg = document.getElementById('customerMsg').value;
  document.getElementById('aiReply').innerText = "Ji bhai, 950 Rs hai, ghar bethy mile gi, paise cheez milne par dene hain. Apna address bhej dein.";
}
