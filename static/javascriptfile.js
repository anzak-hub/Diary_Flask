function sendSelectedItem(item) {
    fetch('/selected-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ selectedItem: item })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function handleClick(event) {
    const selectedItem = event.target.innerText;
    sendSelectedItem(selectedItem);
}

document.addEventListener('DOMContentLoaded', () => {
    const listItems = document.querySelectorAll('li');
    listItems.forEach(item => {
        item.addEventListener('click', handleClick);
    });
});

function handleDoubleClick(itemId) {
    fetch(`/doubleclick/${itemId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: itemId , selectedItem: event.target.innerText})
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert(`Item ${itemId} was double-clicked!`);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}