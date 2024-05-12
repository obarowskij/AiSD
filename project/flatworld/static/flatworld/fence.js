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
        

        document.getElementById('generateFence').remove();
        
    })
    .catch(error => console.error('Error:', error));
}