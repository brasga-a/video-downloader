document.getElementById('download_button').addEventListener('click', function() { // ID corrigido para download_button
    const videoUrl = document.getElementById('video-url').value;

    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: videoUrl }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch((error) => {
        console.error('Erro:', error);
    });
});
