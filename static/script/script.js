document.getElementById('download-btn').addEventListener('click', function() { 
    const videoUrl = document.getElementById('video-url').value;
    const qualityUrl = document.getElementById('quality-select').value;
    const outputUrl = document.getElementById('output-select').value;

    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({url: videoUrl, quality: qualityUrl, output: outputUrl}),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch((error) => {
        console.error('Erro:', error);
            alert("Erro ao se comunicar com o servidor!");
    });
});




