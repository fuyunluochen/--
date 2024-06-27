let text=document.querySelector('ul li a').forEach(text=>{text.innerHTML=text.innerText.split('').map((letters,i)=>'<span>${letters}</span>').join('');
})