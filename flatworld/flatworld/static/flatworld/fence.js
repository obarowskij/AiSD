import {getCookie} from './flatworld.js';

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generateFence').addEventListener('click', fence);
});

function fence(){
    let url = new URL(window.location.href);
    let params = new URLSearchParams(url.search.slice(1));

    params.append('fence', '');

    url.search = params.toString();

    fetch(url)
    .then(response => response.json())
    .then(data =>{
        const img = document.createElement('img'); 
        img.src = data.fence_url; 
        const pageElement = document.querySelector('.page');
        img.style.width = '800px';
        pageElement.appendChild(img); 
        img.onload = () => console.log('Image loaded');
        img.onerror = () => console.log('Image load error');
    })
    .catch(error => console.error('Error:', error));
}