import {getCookie} from './flatworld.js';

document.addEventListener('DOMContentLoaded', function() {
    let button = document.getElementById('generateWorld');
    if (button) {
        button.addEventListener('click', generateWorld);
        window.addEventListener('message', function(event) {
            console.log('Received message: ', event.data);
        });
    }
});

function generateWorld(){
    const inputPoints = document.getElementById('inputPoints').value;
    if (inputPoints < 3) {
        alert('Podaj liczbe punktow wieksza niz 2');
        return;
    }
    fetch('./', {
        method: 'POST',
        body: JSON.stringify({inputPoints: inputPoints}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(image => {
        const img = document.createElement('img'); 
        img.src = image.world_url;
        const pageElement = document.querySelector('.page');
        img.style.width = '800px';
        pageElement.appendChild(img); 
        img.onload = () => console.log('Image loaded');
        img.onerror = () => console.log('Image load error');

        document.getElementById('generateWorld').remove();
        document.getElementById('inputPoints').remove();
        document.getElementById('inputPointsGenerated').innerHTML = 'Kraina zostala wygenerowana z ' + inputPoints + ' punktow';
        const div = document.createElement('div');
        const h3 = document.createElement('h3');
        const button = document.createElement('button');
        button.innerHTML = 'Kontynuuj';
        h3.innerHTML = 'Zauważyłeś, że po kartkach płynie pewna melodia.\n Szczerze? Brzydka, zmieniłbyś ją. dotykasz literek palcami i majstrujesz....'.replace(/\n/g, '<br>');
        div.appendChild(h3);  
        div.appendChild(button);
        pageElement.appendChild(div);
        button.addEventListener('click', function() {
            window.location.href = 'http://127.0.0.1:8000/factory/';
        });
    })
    .catch(error => console.error(error));
}
