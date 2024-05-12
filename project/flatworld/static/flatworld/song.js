import {createPopup} from './flatworld.js';
import {getCookie} from './flatworld.js';

document.addEventListener('DOMContentLoaded', function() {
    let buttons = document.querySelectorAll('.btn');
    if (buttons) {
        buttons.forEach((button) => {
            button.addEventListener('click', change);
        });
    }
});

function change() {
    let windowPopup, overlay;
    ({ windowPopup, overlay } = createPopup("Czy to jest słowo, które zostało zmienione?"));
    windowPopup.style.zIndex = 1001;

    let yesButton = document.createElement("button");
    yesButton.textContent = "Yes";
    let noButton = document.createElement("button");
    noButton.textContent = "No";
    let word_to_change = this.textContent;
    yesButton.addEventListener('click', function() {
        fetch('./', {
            method: 'POST',
            body: JSON.stringify({ 'word_to_change': word_to_change }),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            document.body.removeChild(windowPopup);
            ({ windowPopup, overlay } = createPopup(data.message));
            windowPopup.style.zIndex = 1001;
            document.body.appendChild(windowPopup);
        });
    });

    noButton.addEventListener('click', function() {
        document.body.removeChild(windowPopup);
        document.body.removeChild(overlay);
    });

    windowPopup.appendChild(yesButton);
    windowPopup.appendChild(noButton);
    document.body.appendChild(windowPopup);
    document.body.appendChild(overlay);
}