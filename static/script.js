function buscar() {
    let humor = document.getElementById('humor').value;
    let musica1 = document.getElementById('t1').value;
    let musica2 = document.getElementById('t2').value;
    let musica3 = document.getElementById('t3').value;

    let gostos = [musica1, musica2, musica3].filter(m => m !== '');

    fetch('/buscar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ humor: humor, gostos: gostos })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('resultado').style.display = 'block';
        document.getElementById('capa').src = data.capa;
        let partes = data.nome.split(' - ');
        document.getElementById('artista').textContent = partes[0];
        document.getElementById('nome').textContent = partes[1];
        document.getElementById('audio').src = data.preview;
        
        document.getElementById('play').innerText = '▶';
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const botao = document.getElementById('play');
    const audio = document.getElementById('audio');

    if (botao) {
        botao.addEventListener('click', () => {
            if (audio.paused) {
                audio.play();
                botao.innerText = '⏸';
            } else {
                audio.pause();
                botao.innerText = '▶';
            }
        });
    }
});