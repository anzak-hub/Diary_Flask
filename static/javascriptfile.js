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
        //item.addEventListener('click', handleClick);
        item.addEventListener('dblclick', handleDoubleClick);
    });
});

function handleDoubleClick(event) {
    fetch(`/doubleclick`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: event.target.id , selectedItem: event.target.innerText})
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert(`Item ${event.target.id} was double-clicked!`);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}